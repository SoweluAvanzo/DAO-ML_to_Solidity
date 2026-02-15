from typing import Generator

import src.pipeline.pipeline_item as pi

import src.postprocessing.model_translation.shared.translation_result_model as trm
import src.postprocessing.model_translation.shared.templates.translation_result_template as crt

import src.postprocessing.output_preparation.compilers.shared.compiled_unit_with_id as cuwid
import src.postprocessing.output_preparation.compilers.shared.templates.template_base as tb
import src.postprocessing.output_preparation.compilers.solidity.compiled_model_solidity as cms

import src.postprocessing.consts as const_t
import src.utilities.utils as u


class CompilerSolidityBase(tb.TemplateBase):

    def __init__(self, pipeline_item_data: pi.PIData,
                 optional_external_data=None,
                 key_template_instance_data: str = None,
                 printer_debug: u.PrinterDebug = None
                 ):
        # super().__init__( \
        tb.TemplateBase.__init__(self,
                                 pipeline_item_data,
                                 optional_external_data=optional_external_data,
                                 key_template_instance_data=key_template_instance_data,
                                 printer_debug=printer_debug
                                 )

    def compile_permission(self, permission_translated: crt.TranslatedSubpartTemplated, additional_data=None) -> cuwid.CompiledUnitWithID | Generator[cuwid.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_governance_area(self, governance_area_translated: trm.TranslatedGovernanceArea, additional_data=None) -> cms.CompiledSolidityGovernanceArea | Generator[cuwid.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_role(self, role_translated: crt.TranslatedSubpartTemplated, additional_data=None) -> cuwid.CompiledUnitWithID | Generator[cuwid.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_committee(self, committee_translated: trm.TranslatedCommittee, additional_data=None) -> cms.CompiledSolidityCommittee | Generator[cuwid.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_dao(self, dao_translated: trm.TranslatedDAO, additional_data=None) -> cms.CompiledSolidityDAO | Generator[cuwid.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def compile_diagram(self, diagram_translated: trm.TranslatedDiagram, additional_data=None) -> cms.CompiledSolidityDiagram | Generator[cuwid.CompiledUnitWithID, None, None]:
        """
        Override-designed
        """
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)
