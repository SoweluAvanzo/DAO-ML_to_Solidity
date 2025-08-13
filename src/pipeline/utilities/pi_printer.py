import traceback

import src.pipeline.pipeline_item as pi
import src.utilities.utils as u


class PIPrinter(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData, text="", from_input=False):
        super().__init__(pipeline_item_data)
        self.text = text
        self.from_input = from_input

    def run(self, inputs):
        t = self.get_ith_input(inputs, 0) if self.from_input else self.text
        is_string = u.is_string_or_list(t)
        print(f"printer (this key: {self.pipeline_item_data.key})")
        if is_string :
            print(f"printing: string")
            print(t)
        elif is_string != None:
            print(f"printing array ({len(t)} elements):") 
            i = 0
            for x in t:
                try:
                    print(x)
                except Exception as e:
                    print(f"ERROR while printing {i}-th element:")
                    traceback.print_exception(e)
                i += 1
        elif isinstance(t, dict):
            print(f"printing dict:")
            i = 0
            for x in t.keys():
                try:
                    print(f"{i}) {x} -> ", end="")
                    print(repr(t[x]))
                except Exception as e:
                    print(f"ERROR while printing {i}-th element:")
                    traceback.print_exception(e)
                i += 1
        else:
            print(f"printing non-str, non-list ({type(t)}):")
            print(repr(t))
        return inputs

    def repr_inner(self):
        return \
            """
                "text":"{0}"
            """.format(self.text)
