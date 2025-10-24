import xml.etree.ElementTree as etree  # ET

import src.pipeline.pipeline_item as pi

import src.validators.validation_result as validation_res


# Parsed Tree Stringer

class TestFile1_Processor_ParsedTreeStringer(pi.PipelineItem):
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def run(self, inputs):
        print("----- TestFile1_Processor_ParsedTreeStringer on going ....")
        validation_data = self.get_ith_input(inputs, 0)
        if not isinstance(validation_data, validation_res.ValidationResult):
            raise Exception(
                f"Unrecognized validation result type: expected ValidationResult, got: {type(validation_data)}.")
        # validation_result = validation_data["validation_result"]
        errors = validation_data.errors
        tree_parsed = validation_data.additional_data["tree_parsed"]
        input_string_list = validation_data.input_string_list
        input = validation_data.input
        if errors is not None and len(errors) > 0:
            print("\n\nTestFile1_Processor_ParsedTreeStringer HAS ERRORS!!!")
            for e in errors:
                print(e)
        else:
            print(f"TestFile1_Processor_ParsedTreeStringer")
            print(f"\t{input}")
            print(f"\n\nPREPROCESSOR TO STRING")
            try:
                daos = tree_parsed.xpath('//DAO')
                for dao in daos:
                    print(
                        f"\t dao ID: {dao.get('DAO_ID')}, dao name: {dao.get('DAO_name')}")
            except Exception as e:
                print(e)
        return etree.tostring(tree_parsed)
