import typing
import src.postprocessing.output_preparation.templates.compiled_generic_data as cgd

KEY_ID = "id"
KEY_DAO_COMMITTEES = "committees"
KEY_DAOS_BY_ID = "daos_by_id"
KEY_COMPILED = "compiled"

class CompiledSolidityCommittee(cgd.CompiledUnitWithID):
    def __init__(self, id:str, template_name:str, compiled:dict):
        super().__init__(id, template_name)
        self.compiled = compiled
        
    def get_committee_id_from_data(self, committee_data:dict) -> str:
        """
        Overridable
        """
        return committee_data[KEY_ID] if KEY_ID in committee_data else self.id
    def __to_json__(self):
        j = super().__to_json__()
        j[KEY_COMPILED] = self.compiled
        return j
    

class CompiledSolidityDAO(cgd.CompiledUnitWithID):
    def __init__(self, id:str, template_name:str, compiled:dict):
        super().__init__(id, template_name)
        self.compiled = compiled
        self.committees:dict[str, CompiledSolidityCommittee] = {}
        
    def get_dao_id_from_data(self, dao_data:dict) -> str:
        """
        Overridable
        """
        return dao_data[KEY_ID] if KEY_ID in dao_data else self.id
    def get_dao_committees_from_data(self, dao_data:dict) -> dict[str, CompiledSolidityCommittee]:
        """
        Overridable
        """
        return self.committees # dao_data[KEY_DAO_COMMITTEES]
    def get_committee_id_from_data(self, committee_data:dict):
        return typing.cast(CompiledSolidityCommittee, committee_data).get_committee_id_from_data(committee_data) \
            if isinstance(committee_data, CompiledSolidityCommittee) \
            else committee_data[KEY_ID]
    def add_committee_data_to_dao(self, committee_data:dict):
        committees = self.get_dao_committees_from_data(self.compiled)
        c_id = self.get_committee_id_from_data(committee_data)
        committees[c_id] = committee_data

    def __to_json__(self):
        j = super().__to_json__()
        j[KEY_COMPILED] = self.compiled
        j["committees"] = {
            c.id: c.__to_json__() for c in self.get_dao_committees_from_data(self.compiled).values()
        }
        return j
    

class CompiledSolidityDiagram(cgd.CompiledUnitWithID):
    def __init__(self, id:str, template_name:str, compiled:dict=None):
        super().__init__(id, template_name)
        self.diagram_data = compiled
        self.daos_data_by_id:dict[str, CompiledSolidityDAO] = {}

    def get_diagram_data(self):
        return self.diagram_data
    def get_daos_data_by_id(self):
        return self.daos_data_by_id
    
    def set_diagram_data(self, diagram_data):
        self.diagram_data = diagram_data

    def add_dao(self, dao_data:CompiledSolidityDAO):
        self.daos_data_by_id[dao_data.get_dao_id_from_data(dao_data)] = dao_data

    def get_dao_by_id(self, dao_id:str) -> dict:
        return self.daos_data_by_id[dao_id]
    
    def add_committee_data_to_dao(self, dao_id:str, committee_data:CompiledSolidityCommittee):
        dao = self.get_dao_by_id(dao_id)
        if isinstance(dao, CompiledSolidityDAO):
            dao.add_committee_data_to_dao(committee_data)

    def __to_json__(self):
        j = super().__to_json__()
        j[KEY_COMPILED] = self.compiled
        j[KEY_DAOS_BY_ID] = {
            c.id: c.__to_json__() for c in self.get_daos_data_by_id().values()
        }
        return j
    