import model.dao as DAO

class ControlGraphGeneric:
    def __init__(self, dao):
        self.dao: DAO.DAO = dao

    def get_graph_type(self):
        raise Exception("Not implemented yet.")
    
    def is_list(self):
        raise Exception("Not implemented yet.")
