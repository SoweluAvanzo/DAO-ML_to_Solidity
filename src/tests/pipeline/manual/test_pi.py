from enum import Enum

import src.pipeline.pipeline_manager as pmp
# import src.pipeline.pipeline_item as pip

import src.tests.pipeline.shared.pi_printer as pi_printer
import src.tests.pipeline.shared.pi_int as pi_int
import src.tests.pipeline.shared.pi_add_mul as pi_add_mul
import src.tests.pipeline.shared.pi_str as pi_str


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
        C3 = TD("C3", 7)
        M1 = TD("M1",5)
        M2 = TD("M2",3)
        M3 = TD("M4", 8)
        Neuron1 = TD("Neuron1", 100000)
        Neuron2 = TD("Neuron2", -1000)
        Neuron3 = TD("Neuron3", 0)
        # V2d = TD("V2",7)

if __name__ == "__main__":
    print("AAAAAAAAAAAAAA")

    pm = pmp.PipelineManager()

    print("\n\n 1) EMPTY")
    pm.runPipeline()
    print("DONE")

    key_p = "just a printer"
    pi = pi_printer.PIPrinter(key_p,  [], key_p)
    print("\n\n 2) JUST ONE PRINT")
    pm.addItem(pi)
    pm.runPipeline()
    print("done ... removing")
    pm.removeItem(key_p)
    print("DONE")

    print("\n\n 3) diamond - neuron graph")
    pi = pi_printer.PIPrinter(TestData.START.value.k, [], TestData.START.value.d)
    pm.addItem(pi)

    pi = pi_int.PIInt(TestData.C1.value.k, [TestData.START.value.k], TestData.C1.value.d)
    pm.addItem(pi)
    pi = pi_add_mul.PIAddMult(TestData.M1.value.k, [TestData.C1.value.k], TestData.M1.value.d, False)
    pm.addItem(pi)
    
    pi = pi_int.PIInt(TestData.C2.value.k, [TestData.START.value.k], TestData.C2.value.d)
    pm.addItem(pi)
    pi = pi_add_mul.PIAddMult(TestData.M2.value.k, [TestData.C2.value.k], TestData.M2.value.d, False)
    pm.addItem(pi)

    neuron1 = pi_add_mul.PIAddMult(TestData.Neuron1.value.k, [TestData.M1.value.k,TestData.M2.value.k], TestData.Neuron1.value.d, True)
    pm.addItem(neuron1)

    k_echo_n1 = "k_echo_n1"
    pi = pi_printer.PIPrinter(k_echo_n1, [TestData.Neuron1.value.k], None, True)
    pm.addItem(pi)

    pm.runPipeline()

    print("\n\n BBBBBBBBBBBBBB")
    

    print("\n\n 4) another neuron adjacent to the previous one")

    pi = pi_int.PIInt(TestData.C3.value.k, [], TestData.C3.value.d)
    pm.addItem(pi)
    pi = pi_add_mul.PIAddMult(TestData.M3.value.k, [TestData.C3.value.k], TestData.M3.value.d, False)
    pm.addItem(pi)
    neuron2 = pi_add_mul.PIAddMult(TestData.Neuron2.value.k, [TestData.M3.value.k], TestData.Neuron2.value.d, True)
    pm.addItem(neuron2)

    neuron3 = pi_add_mul.PIAddMult(TestData.Neuron3.value.k, [TestData.Neuron1.value.k,TestData.Neuron2.value.k], TestData.Neuron3.value.d, True)
    pm.addItem(neuron3)

    k_echo_n3 = "echo neuron 3"
    pi = pi_printer.PIPrinter(k_echo_n3, [TestData.Neuron3.value.k], None, True)
    pm.addItem(pi)

    pi = pi_printer.PIPrinter("ciao printer", [TestData.START.value.k], "ciao", False)
    pm.addItem(pi)
    k_echo_2 = "k_echo_2"
    pi = pi_printer.PIPrinter(
        k_echo_2,
        [k_echo_n1, TestData.Neuron1.value.k, TestData.Neuron2.value.k, TestData.Neuron3.value.k, k_echo_n3],
        "WEIRD PRINTER", False)
    pm.addItem(pi)

    pm.runPipeline()

    print("\n\n CCCCCCCCCCCCCC")


    print("\n\n 5) just waiting neuron 2 for a node (like a neuron 4) injecting a constant in neuron 3")

    c_after_n3 = "const after n2"
    pi = pi_int.PIInt(c_after_n3, [TestData.Neuron2.value.k], 400000)
    pm.addItem(pi)
    neuron3.add_dependency(c_after_n3)

    pi_done_txt_k = "pi_done_txt"
    pi_done_txt = pi_str.PIStr(pi_done_txt_k, [k_echo_n3], "DONE")
    pm.addItem(pi_done_txt)
    pi_done_pr = pi_printer.PIPrinter("pi_done_printer", [pi_done_txt_k], None, True)
    pm.addItem(pi_done_pr)

    pm.runPipeline()

    print("\n\n DDDDDDDD")

