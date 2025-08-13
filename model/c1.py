from .c_shared import CShared

class C1(CShared):
    def __init__(self, text) -> None:
        self.text = text
    def printText(self):
        super().printText()
        print(self.text)
