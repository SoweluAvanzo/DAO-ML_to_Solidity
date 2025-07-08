import src.model.diagram_manager as dm
import src.model.base_entity as be
import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.templates.jinja.t_j_base as tjb
import src.postprocessing.output_preparation.templates.jinja.compiled_solidity as tcs
import src.postprocessing.model_conversion.solidity.solidity_translator_general as stg


"""
No differences at the moment from the super (Jinja Base) class.
"""
class TemplateJinjaSolidity(tjb.TemplateJinjaBase):
    def __init__(self, pipeline_item_data: pi.PIData, \
                optional_external_data=None, \
                key_diagram_model:str=None, \
                key_diagram_instance_data:str=None, \
                key_template_filename_by_entity_idNameClassname:dict[str, str]=None, \
                key_template_skeletons_by_filename:str=None):
        super().__init__(pipeline_item_data, optional_external_data, None, None, None)
        self.key_diagram_model = key_diagram_model
        self.key_diagram_instance_data = key_diagram_instance_data
        self.key_template_filename_by_entity_idNameClassname = key_template_filename_by_entity_idNameClassname
        self.key_template_skeletons_by_filename = key_template_skeletons_by_filename

    #
    
    def get_template_filename_by_entity(self, \
            template_filename_by_entity_idNameClassname: dict, \
            entity: be.BaseEntity \
            ) -> str:
        id = entity.get_id()
        if id in template_filename_by_entity_idNameClassname:
            return template_filename_by_entity_idNameClassname[id]
        name = entity.get_name()
        if name in template_filename_by_entity_idNameClassname:
            return template_filename_by_entity_idNameClassname[name]
        class_name = entity.__class__.__name__
        return template_filename_by_entity_idNameClassname[class_name] if class_name in template_filename_by_entity_idNameClassname else ""

    #

    def compile_template(self, \
            diagram_model:dm.DiagramManager, \
            diagram_instance_data:stg.TranslatedDiagram, \
            template_filename_by_entity_idNameClassname: dict, \
            template_skeletons_by_filename: dict[str, list[str]] \
            ) -> tcs.CompiledSolidityDiagram:
        if not isinstance(diagram_model, dm.DiagramManager):
            raise Exception(f"The provided diagram model should be an instance of DiagramManager, but it's: {type(diagram_model)}")
        if not isinstance(diagram_instance_data, stg.TranslatedDiagram):
            raise Exception(f"The provided translated diagram should be an instance of TranslatedDiagram, but it's: {type(diagram_instance_data)}")
        
        id = diagram_model.get_id()
        diagram_i_d = diagram_instance_data.diagram_specific_data
        template_diagram_name = self.get_template_filename_by_entity(template_filename_by_entity_idNameClassname, diagram_model) # TODO : CHI HA IL MAPPING TRA Entità DEL Modello (Diagram, DAOs, Committees, etc) E "filename" DEL TEMPLATE?
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
            self.get_ith_input(inputs, 2) if self.key_template_filename_by_entity_idNameClassname is None else inputs[self.key_template_filename_by_entity_idNameClassname], \
            self.get_ith_input(inputs, 3) if self.key_template_skeletons_by_filename is None else inputs[self.key_template_skeletons_by_filename], \
            )