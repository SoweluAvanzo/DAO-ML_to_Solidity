
class TemplateProviderByName:
    """
    Provider of the template "skeleton" (the actual content of the template, the "thing" with all the placeholders
    ready to be "instantiated" or "hydratated", as one likes calling it) by a name.
    Could be a file reader (like "src.output.JinjaTextFileOutput", or a "src.input.TextFileInput"), a thing returning 
    the template skeleton as a string (or array of string), a DataBase connection, an API call, ...
    """
    def __init__(self, delegator=None):
        self.delegator = delegator

    def actual__provide_template_skeleton_by_name(self, template_name):
        raise Exception("actual__provide_template_skeleton_by_name Not implemented yet")

    def provide_template_skeleton_by_name(self, template_name):
        if self.delegator is not None:
            if isinstance(self.delegator, TemplateProviderByName):
                return self.delegator.provide_template_skeleton_by_name(template_name)
        return self.actual__provide_template_skeleton_by_name(template_name)

    def __call__(self, template_name:str):
        return self.provide_template_skeleton_by_name(template_name)
