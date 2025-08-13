import src.pipeline.pipeline_item as pi
import src.files.file_utils as fu
#import src.model.diagram_manager as dm
#import src.postprocessing.output_preparation.templates.jinja.t_j_base as tjb
import src.postprocessing.output_preparation.templates.jinja.t_j_solidity as tjs
import src.postprocessing.output_preparation.templates.jinja.template_providers.template_provider_by_name as template_provider
import src.postprocessing.output_preparation.templates.jinja.compiled_solidity as tcs
import src.postprocessing.model_conversion.solidity.solidity_converter_general as stg
import src.postprocessing.model_conversion.solidity.optimized.jinja.t_o_sol_jinja_1_0_0 as conv_sol_jinja_1_0_0

class TemplateJinjaSolidity_1_0_0(tjs.TemplateJinjaSolidity):
    """
    @param key_template_skeleton_factory_by_name: key of a function that, provided a template name, returns its skeleton.
    Must be an instance of "TemplateProviderByName"
    """
    def __init__(self, pipeline_item_data: pi.PIData, \
                optional_external_data=None, \
                key_diagram_instance_data:str=None, \
                key_diagram_model:str=None, \
                key_template_skeleton_provider_by_name:str=None \
                ):
        super().__init__(pipeline_item_data, optional_external_data, \
                key_diagram_instance_data=key_diagram_instance_data, \
                key_template_skeleton=None, \
                key_diagram_model=key_diagram_model \
            )
        self.key_template_skeleton_provider_by_name = key_template_skeleton_provider_by_name

    #

    def compile_template(self, \
            diagram_instance_data:stg.TranslatedDiagram, \
            additional_data=None \
            ) -> tcs.CompiledSolidityDiagram:
        if additional_data is None:
            raise Exception(f"Compile template ({self.__class__.__name__}) needs non-None additional_data (from inputs) to get stuff")
        if not isinstance(diagram_instance_data, conv_sol_jinja_1_0_0.TranslatedDiagram_Jinja_1_0_0):
            raise Exception(f"Compile template ({self.__class__.__name__}) needs diagram_instance_data of class TranslatedDiagram_Jinja_1_0_0 (TODO: 'or subclass'), but '{type(diagram_instance_data)}' was provided")

        # diagram_model:dm.DiagramManager = self.get_ith_input(additional_data, 1) if self.key_diagram_model is None else additional_data[self.key_diagram_model], \

        tpbn = self.get_ith_input(additional_data, 2) if self.key_template_skeleton_provider_by_name is None else additional_data[self.key_template_skeleton_provider_by_name]
        if not isinstance(tpbn, template_provider.TemplateProviderByName):
            raise Exception("template provider by name needed")
        
        # 

        # TODO 2025-08-10 perform the actual compilation for each "thing" inside "diagram_instance_data"

        id = 1
        name = diagram_instance_data.entity.get_name()
        diagram_compied = "" # we don't compile the Diagram: onlu
        # so, currently (2025-08-13) there's no use of : diagram_instance_data.entity_specific_data
        # neither of: tpbn
        compilated = tcs.CompiledSolidityDiagram(
            id,
            name,
            compiled=diagram_compied
        )

        # ... and ? let's start the DAO part
        # (2025-08-13) each DAO share the same templating, so the "read" part is performed beforehand to recycle things
        template_filename_dao = "DAOOptimizedGeneric_1_0_0"
        template_filename_dao_extension = f"{template_filename_dao}.jinja"
        print(f"\n  on {type(self)} : BEFORE getting the template skeletons for DAO")
        template_skeleton_dao = tpbn.provide_template_skeleton_by_name(template_name=template_filename_dao_extension)
        print(f"\n  on {type(self)} : AFTER getting the template skeletons for DAO")
        # join the template into a single string
        if isinstance(template_skeleton_dao, list):
            template_skeleton_dao = "\n".join(template_skeleton_dao)

        # now, the CORE

        for dao_id, dao_translated in diagram_instance_data.daos_by_id.items():
            print(f"compiling DAO with ID: ({dao_id}) and Name: ({dao_translated.entity.get_name()})")
            compiled_dao = super().compile_single_template(template_skeleton_dao, dao_translated.entity_specific_data)
            compiled_dao_filename = fu.concat_folder_filename(dao_translated.entity.get_name(), f"{dao_translated.entity.get_name()}.sol")
            compiled_dao_struct = tcs.CompiledSolidityDAO(dao_id, compiled_dao_filename, compiled_dao)
            compilated.add_dao(compiled_dao_struct)

            """
            # TODO: (2025-08-13) compile each Committee
            for committee_id, committee_translated in dao_translated.committees_by_id.items():
                pass
                # lists are allowed to load sub-templates in sub-folders
                # i.e., lists are valid argument to :

                template_filename_simple_majority = ["voting_protocols", "simple_majority.sol.jinja"]
                # template_skeleton__voting__simple_majority = tpbn.provide_template_skeleton_by_name( \
                #     template_name=template_filename_simple_majority )
            """

        return compilated
        