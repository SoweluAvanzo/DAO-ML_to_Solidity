

import src.pipeline.pipeline_item as pi
import src.generators.base_generator as bg
import src.utilities.utils as u


class XmlStringModelGenerator(bg.BaseGenerator):
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def generate(self, additional_input):
        # TODO: riciclare le cose giuste dell'attuale translator

        try:
            is_string = u.is_string_or_list(additional_input)
            if is_string:
                return json.loads(additional_input)
            elif is_string != None:
                # list
                return json.loads("".join(additional_input))
        except Exception as e:
            print(e)
        return None
