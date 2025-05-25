import src.pipeline.pipeline_item as pi
import src.utilities.utils as u


class PIPrinter(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, text="", from_input=False):
        super().__init__(pipeline_item_data)
        self.text = text
        self.from_input = from_input

    def run(self, inputs):
        t = inputs[self.get_dependencies()[0]] if self.from_input else self.text
        is_string = u.is_string_or_list(t)
        if is_string :
            print(f"printing: {t}")
        elif is_string != None:
            print(f"printing array:")
            for x in t:
                print(x)
        else:
            print(f"printing non-str, non-list:")
            print(t)
        return inputs

    def repr_inner(self):
        return \
            """
                "text":"{0}"
            """.format(self.text)
