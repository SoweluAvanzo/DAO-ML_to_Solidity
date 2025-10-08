
class CompiledUnitWithID:
    def __init__(self, id:str, template_name:str, compiled):
        self.id = id
        self.template_name = template_name
        self.compiled = compiled

    def get_compiled(self):
        return self.compiled
    
    def get_template_name(self):
        """
        Override-designed
        """
        return self.template_name

    def __tojson__(self, **kwargs):
        return {
            "id": self.id,
            "template_name": self.template_name,
            "compiled": self.compiled
        }
    def to_json(self):
        return self.__tojson__()
    def toJSON(self):
        return self.to_json()
    
    def __repr__(self):
        import json
        return json.dumps(self.__tojson__())
