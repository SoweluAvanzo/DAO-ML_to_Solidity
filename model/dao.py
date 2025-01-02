

class DAO:
    def __init__(self, id, name, mission_statement, hierarchical_inheritance):
        self.id = id
        self.name = name
        self.mission_statement = mission_statement
        self.hierarchical_inheritance = hierarchical_inheritance
        self.roles = {}
        self.committees = {}
    
    def add_role(self, role):
        self.roles.append(role)

    def add_committee(self, committee):
        self.committees.append(committee)
    