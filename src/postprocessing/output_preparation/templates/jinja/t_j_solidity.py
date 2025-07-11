import src.postprocessing.output_preparation.templates.model_to_template_mapper_base as mtt_mapper_b
import src.pipeline.pipeline_item as pi
import src.model.diagram_manager as dm
import src.model.base_entity as be
import src.postprocessing.output_preparation.templates.jinja.t_j_base as tjb
import src.postprocessing.output_preparation.templates.jinja.compiled_solidity as tcs
import src.postprocessing.model_conversion.solidity.solidity_translator_general as stg


"""
No differences at the moment from the super (Jinja Base) class.
"""
class TemplateJinjaSolidity(tjb.TemplateJinjaBase):
    """
    It fundamentally relies on an instance of ModelToTemplateMapperBase
    """
    def __init__(self, pipeline_item_data: pi.PIData, \
                optional_external_data=None, \
                key_diagram_model:str=None, \
                key_diagram_instance_data:str=None, \
                key_model_to_template_mapper:dict[str, str]=None, \
                key_template_skeletons_by_filename:str=None):
        super().__init__(pipeline_item_data, optional_external_data, None, None, None)
        self.key_diagram_model = key_diagram_model
        self.key_diagram_instance_data = key_diagram_instance_data
        self.key_model_to_template_mapper = key_model_to_template_mapper
        self.key_template_skeletons_by_filename = key_template_skeletons_by_filename

    #
    
    def get_template_filename_by_entity(self, \
            model_to_template_mapper: mtt_mapper_b.ModelToTemplateMapperBase, \
            entity: be.BaseEntity \
            ) -> str:
        """
        That's one of the core function in Jinja compilation, which relies on one of the core
        data in input
        """
        id = entity.get_id()
        if model_to_template_mapper.has_template_filename_for_key(id):
            return model_to_template_mapper.get_template_filename_by_key(id)
        name = entity.get_name()
        if model_to_template_mapper.has_template_filename_for_key(name):
            return model_to_template_mapper.get_template_filename_by_key(name)
        class_name = entity.__class__.__name__
        if model_to_template_mapper.has_template_filename_for_key(class_name):
            return model_to_template_mapper.get_template_filename_by_key(class_name)
        try:
            hopefully_a_template = model_to_template_mapper.get_template_filename_by_key(entity)
            return hopefully_a_template
        except Exception as e:
            print(e)
            return None

    #

    def compile_template(self, \
            diagram_model:dm.DiagramManager, \
            diagram_instance_data:stg.TranslatedDiagram, \
            model_to_template_mapper: mtt_mapper_b.ModelToTemplateMapperBase, \
            template_skeletons_by_filename: dict[str, list[str]] \
            ) -> tcs.CompiledSolidityDiagram:
        if not isinstance(diagram_model, dm.DiagramManager):
            raise Exception(f"The provided diagram model should be an instance of DiagramManager, but it's: {type(diagram_model)}")
        if not isinstance(diagram_instance_data, stg.TranslatedDiagram):
            raise Exception(f"The provided translated diagram should be an instance of TranslatedDiagram, but it's: {type(diagram_instance_data)}")
        
        id = diagram_model.get_id()
        diagram_i_d = diagram_instance_data.diagram_specific_data
        template_diagram_name = self.get_template_filename_by_entity(model_to_template_mapper, diagram_model) # TODO : CHI HA IL MAPPING TRA Entità DEL Modello (Diagram, DAOs, Committees, etc) E "filename" DEL TEMPLATE?
        diagram_skeleton = template_skeletons_by_filename[template_diagram_name]
        diagram_compiled = super().compile_template(template_diagram_name, diagram_skeleton, diagram_i_d)

        csd = tcs.CompiledSolidityDiagram(id, template_diagram_name, diagram_compiled)
        #get_template_name

        # TODO : continue with all DAOs and each Committees within each DAO

        return csd




    def run(self, inputs):
        return self.compile_template(\
            self.get_ith_input(inputs, 0) if self.key_diagram_model is None else inputs[self.key_diagram_model], \
            self.get_ith_input(inputs, 1) if self.key_diagram_instance_data is None else inputs[self.key_diagram_instance_data], \
            self.get_ith_input(inputs, 2) if self.key_model_to_template_mapper is None else inputs[self.key_model_to_template_mapper], \
            self.get_ith_input(inputs, 3) if self.key_template_skeletons_by_filename is None else inputs[self.key_template_skeletons_by_filename], \
            )