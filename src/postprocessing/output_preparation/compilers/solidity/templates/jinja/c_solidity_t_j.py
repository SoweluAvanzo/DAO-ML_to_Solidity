from typing import Generator

import src.pipeline.pipeline_item as pi
import src.postprocessing.output_preparation.compilers.shared.templates.jinja.c_t_j_base as tjb
import src.postprocessing.output_preparation.compilers.shared.compiled_unit_with_id as cuwid
import src.postprocessing.output_preparation.compilers.solidity.compiler_solidity_base as csb
import src.postprocessing.output_preparation.compilers.solidity.templates.compiled_model_solidity_t as cmst
import src.postprocessing.output_preparation.compilers.shared.templates.compiled_model_data_templated as cmdt

import src.postprocessing.model_translation.shared.templates.translation_result_template as crt
import src.postprocessing.model_translation.shared.templates.translation_result_model_templated as trmt

import src.model.diagram_manager as dm
import src.model.dao as d
import src.model.committee as c
import src.model.role as r
import src.model.governance_area as ga
import src.model.permission as perm

import src.utilities.utils as u
import src.utilities.errors as e_c


"""
No differences at the moment from the super (Jinja Base) class.
"""


class CompilerSolidityTemplateJinja(tjb.CompilerTemplateJinjaBase, csb.CompilerSolidityBase):
    """
    It fundamentally relies on an instance of ModelToTemplateMapperBase
    """

    def __init__(self, pipeline_item_data: pi.PIData,
                 optional_external_data=None,
                 key_template_instance_data: str = None,
                 key_template_skeleton: str = None,
                 key_diagram_model: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        if not isinstance(pipeline_item_data, pi.PIData):
            raise Exception(
                f"pipeline_item_data is not a PIData: {type(pipeline_item_data)}")
        tjb.CompilerTemplateJinjaBase.__init__(self,
                                               pipeline_item_data,
                                               optional_external_data=optional_external_data,
                                               key_template_instance_data=key_template_instance_data,
                                               key_template_skeleton=key_template_skeleton,
                                               printer_debug=printer_debug
                                               )
        csb.CompilerSolidityBase.__init__(self,
                                          pipeline_item_data,
                                          optional_external_data=optional_external_data,
                                          key_template_instance_data=key_template_instance_data,
                                          printer_debug=printer_debug
                                          )
        self.key_diagram_model = key_diagram_model

    #

    def compile_governance_area(self, diagram_translated: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated, governance_area_translated: trmt.TranslatedGovernanceAreaTemplated, additional_data=None) -> cmst.CompiledSolidityGovernanceAreaTemplated | Generator[cmdt.CompiledWithOutputPath, None, None]:
        """
        Overriding the parameter type to a Template-specific subclass
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_committee(self, diagram_translated: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated, committee_translated: trmt.TranslatedCommitteeTemplated, additional_data=None) -> cmst.CompiledSolidityCommitteeTemplated | Generator[cmdt.CompiledWithOutputPath, None, None]:
        """
        Overriding the parameter type to a Template-specific subclass
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_dao(self, diagram_translated: trmt.TranslatedDiagramTemplated, dao_translated: trmt.TranslatedDAOTemplated, additional_data=None) -> cmst.CompiledSolidityDAOTemplated | Generator[cmdt.CompiledWithOutputPath, None, None]:
        """
        Overriding the parameter type to a Template-specific subclass
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_diagram(self, diagram_translated: trmt.TranslatedDiagramTemplated, additional_data=None) -> cmst.CompiledSolidityDiagramTemplated | Generator[cmdt.CompiledWithOutputPath, None, None]:
        """
        Overriding the parameter type to a Template-specific subclass
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)
