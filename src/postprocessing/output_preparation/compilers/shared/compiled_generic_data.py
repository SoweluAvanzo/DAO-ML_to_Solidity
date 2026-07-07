
KEY_ID = "id"
KEY_OUTPUT_FULL_PATH = "output_full_path"
KEY_COMPILED = "compiled"


class CompiledUnitWithID:
    def __init__(self, id: str, output_full_path: str, compiled, suggested_output_folder_path_from_base: str = ""):
        self.id = id
        self.output_full_path = output_full_path
        self.compiled = compiled
        self.suggested_output_folder_path_from_base = suggested_output_folder_path_from_base

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
