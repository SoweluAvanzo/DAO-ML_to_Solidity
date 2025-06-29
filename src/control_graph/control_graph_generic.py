import src.model.dao as daoModule

class ControlGraphGeneric:
    def __init__(self, dao):
        self.dao: daoModule.DAO = dao

    def get_graph_type(self):
        raise Exception("Not implemented yet.")
    
    def is_list(self):
        raise Exception("Not implemented yet.")
