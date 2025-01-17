
class BaseOutput:
    def __init__(self, base_destination:str=None):
        self.base_destination = base_destination

    def to_output(self, what, destination:str=None, additional_data=None) -> bool:
        return False
