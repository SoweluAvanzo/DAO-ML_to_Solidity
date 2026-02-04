
KEY_ID = "id"
KEY_COMPILED = "compiled"


class CompiledUnitWithID:
    def __init__(self, id: str, compiled):
        self.id = id
        self.compiled = compiled

    def get_id(self):
        return self.id

    def get_compiled(self):
        return self.compiled

    def get_output_full_path(self):
        """
        Override-designed
        """
        return self.output_full_path

    def __tojson__(self, **kwargs):
        return {
            KEY_ID: self.id,
            KEY_OUTPUT_FULL_PATH: self.output_full_path,
            KEY_COMPILED: self.compiled
        }

    def to_json(self):
        return self.__tojson__()

    def toJSON(self):
        return self.to_json()

    def __repr__(self):
        import json
        return json.dumps(self.__tojson__())
