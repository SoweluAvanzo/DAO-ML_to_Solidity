import src.pipeline.pipeline_item as pi
import src.input.txt_file_input as tfi
import src.postprocessing.output_preparation.templates.jinja.template_providers.template_provider_by_name as tpbn
import src.files.file_utils as fu

class TemplateProviderFromTxtFile(tpbn.TemplateProviderByName):
    def __init__(self, base_template_folder:str):
        super().__init__(delegator=None)
        if base_template_folder is None:
            raise Exception("base_template_folder is None")
        self.base_template_folder = base_template_folder
        k_input_template_provider = "k_input_template_provider"
        self.input_template_provider = tfi.TextFileInput(pi.PIData(k_input_template_provider, None), None)

    def set_filename(self, filename:str):
        full_path = ""
        if isinstance(filename, str):
            full_path = fu.concat_folder_filename(self.base_template_folder, filename)
        elif isinstance(filename, list):
            full_path = fu.concat_folder_filename(self.base_template_folder, *filename)
        self.input_template_provider.filepath = full_path

    def actual__provide_template_skeleton_by_name(self, template_name):
        self.set_filename(template_name)
        return self.input_template_provider.run(None)
