
class CompiledUnitWithID:
    def __init__(self, id:str, template_name:str):
        self.id = id
        self.template_name = template_name
    
    def get_template_name(self):
        """
        Override-designed
        """
        return self.template_name

    def __tojson__(self, **kwargs):
        return {
            "id": self.id,
            "template_name": self.template_name
        }
    def to_json(self):
        return self.__tojson__()
    def toJSON(self):
        return self.to_json()
    
    def __repr__(self):
        import json
        return json.dumps(self.__tojson__())
