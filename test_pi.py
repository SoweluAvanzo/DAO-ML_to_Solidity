import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pip


class A:
    def __init__(self, text="", num=0):
        self.text = text
        self.num=num
    def getNum(self):
        return self.num
    def __repr__(self):
        return """{{"text": "{0}", "num": {1} }}""".format(self.text, str(self.getNum()))
    
class B(A):
    def __init__(self, text="", num=0):
        super().__init__(text, num)
    def getNum(self):
        return self.num * 1000



class PIPrinter(pip.PipelineItem):
    def __init__(self, key, dependencies=None, text="", fromInput=False):
        super().__init__(key, dependencies)
        self.text=text
        self.fromInput = fromInput
    def run(self, input):
        t = input[self.dependencies[0]] if  self.fromInput else self.text
        print(f"printing: {t}")
        return input
    def repr_inner(self):
        return """ "text":"{0}" """.format(self.text)

class PIInt(pip.PipelineItem):
    def __init__(self, key, dependencies=None, val=0):
        super().__init__(key, dependencies)
        self.val=val
    def run(self, input):
        return self.val
    def repr_inner(self):
        return """ "val": {0}""".format(str(self.val))


class PIMath(pip.PipelineItem):
    def __init__(self, key, dependencies=None, scalar=0, isAddition=True):
        super().__init__(key, dependencies)
        self.scalar=scalar
        self.isAddition=isAddition

    def run(self, input):
        if self.isAddition:
            partial = self.scalar
            for  dep in self.dependencies:
                input_data = input[dep] if dep in input else 0
                partial += input_data
            return partial
        #print(f"{ 'adding' if self.isAddition else 'multiplying'} {val} with {self.scalar}")
        return self.scalar * input[self.dependencies[0]] # input['value'] if 'value' in input else 0

    #def __repr__(self):
    def repr_inner(self):
        #return """ "val": {0}""".format(str(self.val))
        return """ "isAddition": {0}, "scalar": {1}""".format( 'true' if self.isAddition else 'false', self.scalar)


from enum import Enum

class TD:
    def __init__(self, k,d,altro=None):
        print(f"k:{k}, d: {d}")
        self.k=k
        self.d=d
        self.altro=altro
    def __repr__(self):
        return "{{ k:{0}, d: {1}, altro: {2}}}".format(self.k, self.d, str(self.altro))

class TestData(Enum):
        START = TD("START", "let's begin")
        C1 = TD("C1", 10)
        C2 = TD("C2", 8)
        M1= TD("M1",5)
        M2= TD("M2",3)
        Neuron1 = TD("Neuron1", 100000)
        # V2d = TD("V2",7)

if __name__ == "__main__":
    # a = A("aaaa", 5)
    # b = B( "BBBB", 3)
    # print(repr(a))
    # print(repr(b))

    print("AAAAAAAAAAAAAA")

    pm = pmp.PipelineManager()
    
    pi = PIPrinter(TestData.START.value.k, [], TestData.START.value.d)
    pm.addItem(pi)

    pi = PIInt(TestData.C1.value.k, [TestData.START.value.k], TestData.C1.value.d)
    pm.addItem(pi)
    pi = PIMath(TestData.M1.value.k, [TestData.C1.value.k], TestData.M1.value.d, False)
    pm.addItem(pi)
    
    pi = PIInt(TestData.C2.value.k, [TestData.START.value.k], TestData.C2.value.d)
    pm.addItem(pi)
    pi = PIMath(TestData.M2.value.k, [TestData.C2.value.k], TestData.M2.value.d, False)
    pm.addItem(pi)

    pi = PIMath(TestData.Neuron1.value.k, [TestData.M1.value.k,TestData.M2.value.k], TestData.Neuron1.value.d, True)
    pm.addItem(pi)

    pi = PIPrinter("echo", [TestData.Neuron1.value.k], None, True)
    pm.addItem(pi)

    pm.runPipeline()


    print("BBBBBBBBBBBBBB")
    
