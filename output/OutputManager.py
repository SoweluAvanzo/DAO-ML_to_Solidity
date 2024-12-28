'''
Classe generica di output
TODO: terminare il refactoring
'''
class OutputManager:

    def __init__(self, default_destination="./"):
        self.default_destination = default_destination
    
    def to_output(self, what:any, destination: any) -> any:
        pass
