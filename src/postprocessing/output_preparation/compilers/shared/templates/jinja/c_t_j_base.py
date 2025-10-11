from jinja2 import Template

import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.compilers.shared.templates.template_base as tb

JINJA_EXTENSION_DEFAULT = "jinja"


class CompilerTemplateJinjaBase(tb.TemplateBase):
    """
    Compiles a template using the Jinja package by populating it with the provided data and producing as output the lines of the compiled template
    """

    def __init__(self, pipeline_item_data: pi.PIData, optional_external_data=None,
                 key_template_instance_data: str = None,
                 key_template_skeleton: str = None
                 ):
        # super().__init__( \
        tb.TemplateBase.__init__(self,
                                 pipeline_item_data,
                                 optional_external_data=optional_external_data,
                                 key_template_instance_data=key_template_instance_data
                                 )
        self.key_template_skeleton = key_template_skeleton
        self.jinja_extension: str = JINJA_EXTENSION_DEFAULT

    def compile_single_template(self, template_skeleton, instance_data: dict):
        if not isinstance(template_skeleton, str):
            if isinstance(template_skeleton, list):
                template_skeleton = "\n".join(template_skeleton)
            else:
                try:
                    template_skeleton = "\n".join(iter(template_skeleton))
                except TypeError as te:
                    print('template_skeleton is not iterable')
                    print(te)
                    raise Exception(
                        f"The template_skeleton is not a string: {type(template_skeleton)}")

        template = Template(template_skeleton)
        return template.render(
            **instance_data
        ).splitlines()

    def compile_template(self, instance_data: dict, additional_data=None):
        if additional_data is None:
            raise Exception(
                f"Compile template ({self.__class__.__name__}) needs non-None additional_data (from input) to get stuff")
        template_skeleton = additional_data[self.key_template_skeleton]
        return self.compile_single_template(template_skeleton, instance_data)
