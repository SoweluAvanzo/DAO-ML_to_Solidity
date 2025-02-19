from .c_shared import CShared
from .c1 import C1

class C2(CShared):
    def __init__(self, text, num) -> None:
        self.c1 = C1(text)
        self.num = num
    def printText(self):
        super().printText()
        print(self.num)
        self.c1.printText()
