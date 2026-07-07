import src.pipeline.pipeline_item as pi
import src.input.txt_file_input as tfi
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as tpbn
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
            full_path = fu.concat_folder_filename(self.base_template_folder, filename).replace(f"{fu.PATH_SEPARATOR_CHAR}{fu.PATH_SEPARATOR_CHAR}", fu.PATH_SEPARATOR_CHAR)
        elif isinstance(filename, list):
            cleaned_filename_list = [f.strip() for f in filename if isinstance(f, str) and f.strip() != ""]
            if len(cleaned_filename_list) <= 0:
                full_path = self.base_template_folder
            else:
                full_path = fu.concat_folder_filename(self.base_template_folder, *cleaned_filename_list)
        self.input_template_provider.filepath = full_path

    def actual__provide_template_skeleton_by_name(self, template_name):
        self.set_filename(template_name)
        return self.input_template_provider.run(None)
