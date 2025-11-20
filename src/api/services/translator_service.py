"""
Service for translating DAO-ML to Solidity smart contracts.
Uses the PipelineManager architecture for proper processing flow.
"""
import sys
from pathlib import Path
from typing import Tuple, List, Optional, Union

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Pipeline infrastructure
import src.pipeline.pipeline_manager as pmp
import src.pipeline.pipeline_item as pi
import src.pipeline.utilities.pi_str as pstr
import src.pipeline.utilities.pi_any_value as pval

# Input handling
import src.input.xml_file_input as xfi
import src.validators.xml.xml_dao_validator as xvi
import src.validators.validation_result_to_errors as vete
import src.pipeline.utilities.pi_exception_raiser as perrr

# Model generation
import src.model_generators.xml_string_model_generator as xsmg
from src.model.diagram_manager import DiagramManager

# Postprocessing - translation
import src.postprocessing.model_translation.translation_types as ct
import src.postprocessing.model_translation.model_translator_configurable as mcc
import src.postprocessing.model_translation.solidity.voting_protocols_list_loader as pi_vpll
import src.postprocessing.model_translation.solidity.translation_types_solidity as transl_types_sol
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as jinja_opt_versions
import src.postprocessing.model_translation.solidity.tests.jinja.solidity_tests_translator_jinja_hardhat as sol_test_t

# Postprocessing - compilation
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.tpbn_txt_file as template_by_name_txt
import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.c_sol_t_j_1_0_0 as c_sol_t_j_1_0_0
import src.postprocessing.output_preparation.compilers.solidity.tests.templates.jinja.c_sol_tests_t_j as c_sol_tests_t_j

# Output
import src.output.jinja_text_file_output as jtfo
import src.postprocessing.output_preparation.json.model_to_json as m_json

# Constants
import src.postprocessing.consts_template as consts_t
import src.utilities.utils as u


class ServicePrinterDebug(u.PrinterDebug):
    """Simple printer debug for the service."""
    def __init__(self):
        self.messages = []
        self.errors = []

    def print_msg(self, msg):
        self.messages.append(str(msg))

    def print_error(self, msg):
        self.errors.append(str(msg))

    def print_debug(self, _msg):
        pass  # Silent debug


class TranslatorService:
    """Service for translating DAO-ML to Solidity contracts using pipeline architecture."""

    def __init__(self, templates_dir: Path, output_base_dir: Path):
        """
        Initialize translator service.

        Args:
            templates_dir: Path to templates directory
            output_base_dir: Base directory for output
        """
        self.templates_dir = templates_dir
        self.output_base_dir = output_base_dir
        # Schema file path for XML validation
        self.schema_path = str(PROJECT_ROOT / 'data' / 'XSD_DAO_ML.xsd')

    def _create_pipeline_manager(self, printer: ServicePrinterDebug = None) -> pmp.PipelineManager:
        """Create a new pipeline manager with optional printer."""
        if printer is None:
            printer = ServicePrinterDebug()
        return pmp.PipelineManager(printer_debug=printer)

    def _build_input_pipeline(
        self,
        pm: pmp.PipelineManager,
        input_data: Union[str, DiagramManager],
        input_type: str = "xml_string"
    ) -> Tuple[str, str]:
        """
        Build the input portion of the pipeline.

        Args:
            pm: PipelineManager to add items to
            input_data: The input data (XML string, file path, or DiagramManager)
            input_type: Type of input ("xml_string", "xml_file", "model")

        Returns:
            Tuple of (key_for_validator_input, key_for_model) - keys to use for dependencies
        """
        if input_type == "model":
            # Direct model input - no validation needed
            k_model = "k_direct_model_input"
            model_provider = pval.PIAnyValue(pi.PIData(k_model, None), input_data)
            pm.addItem(model_provider)
            return None, k_model

        elif input_type == "xml_string":
            # XML string input
            k_xml_string = "k_xml_string_input"
            xml_string_provider = pstr.PIStr(pi.PIData(k_xml_string, None), input_data)
            pm.addItem(xml_string_provider)
            return k_xml_string, None

        elif input_type == "xml_file":
            # XML file input
            k_xml_filepath = "k_xml_filepath_provider"
            xml_filepath_provider = pstr.PIStr(pi.PIData(k_xml_filepath, None), input_data)
            pm.addItem(xml_filepath_provider)

            k_xml_file_input = "k_xml_file_input"
            xml_file_input = xfi.TextFileInputXML(
                pi.PIData(k_xml_file_input, [k_xml_filepath]), xml_version="1.0"
            )
            pm.addItem(xml_file_input)
            return k_xml_file_input, None

        else:
            raise ValueError(f"Unknown input_type: {input_type}")

    def _build_validation_pipeline(
        self,
        pm: pmp.PipelineManager,
        k_input: str,
        printer: ServicePrinterDebug
    ) -> str:
        """
        Build the validation portion of the pipeline.

        Args:
            pm: PipelineManager to add items to
            k_input: Key of the input pipeline item
            printer: Printer for debug output

        Returns:
            Key of the validator output
        """
        k_xml_validator = "k_xml_validator"
        xml_validator = xvi.XMLDaoValidator(
            pi.PIData(k_xml_validator, [k_input]),
            self.schema_path,
            printer_debug=printer
        )
        pm.addItem(xml_validator)

        # Error extraction
        k_validator_errors = "k_validator_errors_extractor"
        validator_errors = vete.ValidationResultToErrorsExtractor(
            pi.PIData(k_validator_errors, [k_xml_validator]),
            key_validation_result=k_xml_validator,
            printer_debug=printer
        )
        pm.addItem(validator_errors)

        # Exception raiser for validation errors
        k_exc_raiser = "k_validation_exc_raiser"
        exc_raiser = perrr.PIExceptionRaiser(
            pi.PIData(k_exc_raiser, [k_validator_errors]),
            key_error_input=k_validator_errors,
            printer_debug=printer
        )
        pm.addItem(exc_raiser)

        return k_xml_validator

    def _build_model_generation_pipeline(
        self,
        pm: pmp.PipelineManager,
        k_validator: str,
        printer: ServicePrinterDebug
    ) -> str:
        """
        Build the model generation portion of the pipeline.

        Args:
            pm: PipelineManager to add items to
            k_validator: Key of the validator output
            printer: Printer for debug output

        Returns:
            Key of the model generator output
        """
        k_model_generator = "k_model_generator"
        model_generator = xsmg.XmlStringModelGenerator(
            pi.PIData(k_model_generator, [k_validator]),
            printer_debug=printer
        )
        pm.addItem(model_generator)
        return k_model_generator

    def _build_translation_pipeline(
        self,
        pm: pmp.PipelineManager,
        k_model: str,
        printer: ServicePrinterDebug,
        generate_tests: bool = True
    ) -> Tuple[str, str]:
        """
        Build the translation portion of the pipeline.

        Args:
            pm: PipelineManager to add items to
            k_model: Key of the model generator output
            printer: Printer for debug output
            generate_tests: Whether to generate tests

        Returns:
            Tuple of (key_translator, key_test_translator)
        """
        # Translation type
        translator_type = ct.TranslationTypes.SOLIDITY.value
        k_translator_type = "k_translator_type"
        pi_translator_type = pstr.PIStr(pi.PIData(k_translator_type, None), translator_type)
        pm.addItem(pi_translator_type)

        # Translator version
        jinja_translator_version = jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value
        k_version_translator = "k_version_translator"
        pi_version_translator = pstr.PIStr(pi.PIData(k_version_translator, None), jinja_translator_version)
        pm.addItem(pi_version_translator)

        # Target version
        k_translator_target = "k_translator_target"
        pi_translator_target = pstr.PIStr(pi.PIData(k_translator_target, None), "1.0.0")
        pm.addItem(pi_translator_target)

        # Solidity subtype
        translator_solidity_subtype = transl_types_sol.TranslationTypesSolidity.OPTIMIZED.value
        k_translator_solidity_subtype = "k_translator_solidity_subtype"
        pi_translator_solidity_subtype = pstr.PIStr(
            pi.PIData(k_translator_solidity_subtype, None), translator_solidity_subtype
        )
        pm.addItem(pi_translator_solidity_subtype)

        # Voting protocols loader
        k_all_voting_protocols = consts_t.KEY__ALL_VOTING_PROTOCOLS__ON_ADDITIONAL_DATA
        voting_protocol_loader = pi_vpll.VotingProtocolListLoader(
            pi.PIData(k_all_voting_protocols, None),
            printer_debug=printer,
            folder_voting_protocols=str(self.templates_dir / 'voting_protocols')
        )
        pm.addItem(voting_protocol_loader)

        # Main translator
        k_translator = "k_translator"
        translator = mcc.ModelTranslatorConfigurable(
            pi.PIData(k_translator, [
                k_model, k_translator_type, k_version_translator,
                k_translator_target, k_translator_solidity_subtype, k_all_voting_protocols
            ]),
            key_model=k_model,
            key_translator_type=k_translator_type,
            key_translator_version=k_version_translator,
            key_translator_target=k_translator_target,
            printer_debug=printer
        )
        pm.addItem(translator)

        # Test translator (if requested)
        k_test_translator = None
        if generate_tests:
            k_test_translator = "k_translator_sol_test"
            test_translator = sol_test_t.SolidityTestsTranslatorJinjaHardhat_1_0_0(
                pi.PIData(k_test_translator, [k_model]),
                optional_external_data=None,
                key_model=k_model,
                is_optimized=True
            )
            pm.addItem(test_translator)

        return k_translator, k_test_translator

    def _build_compilation_pipeline(
        self,
        pm: pmp.PipelineManager,
        k_translator: str,
        k_model: str,
        k_test_translator: str,
        printer: ServicePrinterDebug
    ) -> Tuple[str, str]:
        """
        Build the compilation portion of the pipeline.

        Args:
            pm: PipelineManager to add items to
            k_translator: Key of the translator output
            k_model: Key of the model
            k_test_translator: Key of the test translator output (or None)
            printer: Printer for debug output

        Returns:
            Tuple of (key_compiler, key_test_compiler)
        """
        # Template provider
        template_provider = template_by_name_txt.TemplateProviderFromTxtFile(
            base_template_folder=str(self.templates_dir)
        )
        k_template_provider = "k_template_provider"
        pi_template_provider = pval.PIAnyValue(pi.PIData(k_template_provider, None), template_provider)
        pm.addItem(pi_template_provider)

        # Main compiler
        k_compiler = "k_template_compiler"
        template_compiler = c_sol_t_j_1_0_0.CompilerSolidityTemplateJinja_1_0_0(
            pi.PIData(k_compiler, [k_translator, k_model, k_template_provider]),
            key_diagram_instance_data=k_translator,
            key_diagram_model=k_model,
            key_template_skeleton_provider_by_name=k_template_provider,
            printer_debug=printer
        )
        pm.addItem(template_compiler)

        # Test compiler (if test translator exists)
        k_test_compiler = None
        if k_test_translator:
            k_is_result_as_list = "k_is_result_as_list"
            pi_is_result_as_list = pval.PIAnyValue(pi.PIData(k_is_result_as_list, None), True)
            pm.addItem(pi_is_result_as_list)

            k_test_compiler = "k_compiler_sol_test"
            test_compiler = c_sol_tests_t_j.CompilerSolidityTestsTemplateJinja(
                pi.PIData(k_test_compiler, [
                    k_test_translator, k_template_provider, k_model, k_is_result_as_list
                ]),
                optional_external_data=None,
                key_diagram_instance_data=k_test_translator,
                key_template_skeleton_provider_by_name=k_template_provider,
                key_diagram_model=k_model,
                key_is_result_as_list=k_is_result_as_list
            )
            pm.addItem(test_compiler)

        return k_compiler, k_test_compiler

    def _build_output_pipeline(
        self,
        pm: pmp.PipelineManager,
        k_compiler: str,
        k_test_compiler: str,
        output_dir: Path
    ) -> Tuple[str, str]:
        """
        Build the output portion of the pipeline.

        Args:
            pm: PipelineManager to add items to
            k_compiler: Key of the compiler output
            k_test_compiler: Key of the test compiler output (or None)
            output_dir: Output directory

        Returns:
            Tuple of (key_output, key_test_output)
        """
        k_output = "k_compiled_output"
        compiled_output = jtfo.JinjaTextFileOutput(
            pi.PIData(k_output, [k_compiler]),
            key_compiled_diagram=k_compiler,
            base_destination=str(output_dir)
        )
        pm.addItem(compiled_output)

        k_test_output = None
        if k_test_compiler:
            k_test_output = "k_test_compiled_output"
            test_output = jtfo.JinjaTextFileOutput(
                pi.PIData(k_test_output, [k_test_compiler]),
                key_compiled_diagram=k_test_compiler,
                base_destination=str(output_dir)
            )
            pm.addItem(test_output)

        return k_output, k_test_output

    def validate_input(
        self,
        input_data: Union[str, Path],
        input_type: str = "xml_string"
    ) -> Tuple[bool, List[str], Optional[object]]:
        """
        Validate input content against DAO-ML schema.

        Args:
            input_data: Input content (string or file path)
            input_type: Type of input ("xml_string" or "xml_file")

        Returns:
            Tuple of (is_valid, errors, validation_result)
        """
        try:
            printer = ServicePrinterDebug()
            pm = self._create_pipeline_manager(printer)

            # Build input pipeline
            if input_type == "xml_file":
                input_data = str(input_data)
            k_input, _ = self._build_input_pipeline(pm, input_data, input_type)

            # Build validation pipeline
            k_validator = self._build_validation_pipeline(pm, k_input, printer)

            # Run pipeline
            try:
                outputs = pm.runPipeline()
                # Get validation result from outputs
                validation_result = outputs.get(k_validator)
                if validation_result:
                    return validation_result.validation_result, [], validation_result
                return True, [], None
            except Exception as e:
                # Validation errors are raised as exceptions
                return False, printer.errors if printer.errors else [str(e)], None

        except Exception as e:
            import traceback
            return False, [f"{str(e)}\n{traceback.format_exc()}"], None

    def generate_model(
        self,
        input_data: Union[str, Path],
        input_type: str = "xml_string"
    ) -> Tuple[bool, List[str], Optional[DiagramManager]]:
        """
        Generate internal model from input content.

        Args:
            input_data: Input content (string or file path)
            input_type: Type of input ("xml_string" or "xml_file")

        Returns:
            Tuple of (success, errors, diagram_manager)
        """
        try:
            printer = ServicePrinterDebug()
            pm = self._create_pipeline_manager(printer)

            # Build input pipeline
            if input_type == "xml_file":
                input_data = str(input_data)
            k_input, _ = self._build_input_pipeline(pm, input_data, input_type)

            # Build validation pipeline
            k_validator = self._build_validation_pipeline(pm, k_input, printer)

            # Build model generation pipeline
            k_model = self._build_model_generation_pipeline(pm, k_validator, printer)

            # Run pipeline
            try:
                outputs = pm.runPipeline()
                model = outputs.get(k_model)
                if model and isinstance(model, DiagramManager):
                    return True, [], model
                else:
                    errors = [f"Unexpected result type: {type(model)}"]
                    if printer.errors:
                        errors.extend(printer.errors)
                    return False, errors, None
            except Exception as e:
                errors = printer.errors if printer.errors else [str(e)]
                return False, errors, None

        except Exception as e:
            import traceback
            return False, [f"Model generation error: {str(e)}\n{traceback.format_exc()}"], None

    def translate_to_solidity(
        self,
        input_data: Union[str, Path, DiagramManager],
        output_dir: Path,
        input_type: str = "xml_string",
        generate_tests: bool = True
    ) -> Tuple[bool, List[str], List[str], List[str]]:
        """
        Translate input to Solidity contracts and optionally tests.

        Args:
            input_data: Input content (string, file path, or DiagramManager)
            output_dir: Directory for output files
            input_type: Type of input ("xml_string", "xml_file", or "model")
            generate_tests: Whether to generate tests

        Returns:
            Tuple of (success, errors, contract_files, test_files)
        """
        errors = []
        contract_files = []
        test_files = []

        try:
            printer = ServicePrinterDebug()
            pm = self._create_pipeline_manager(printer)

            # Build input pipeline
            if input_type == "xml_file":
                input_data = str(input_data)
            k_input, k_model = self._build_input_pipeline(pm, input_data, input_type)

            # If input is not a model, build validation and model generation
            if k_model is None:
                k_validator = self._build_validation_pipeline(pm, k_input, printer)
                k_model = self._build_model_generation_pipeline(pm, k_validator, printer)

            # Build translation pipeline
            k_translator, k_test_translator = self._build_translation_pipeline(
                pm, k_model, printer, generate_tests
            )

            # Build compilation pipeline
            k_compiler, k_test_compiler = self._build_compilation_pipeline(
                pm, k_translator, k_model, k_test_translator, printer
            )

            # Build output pipeline
            self._build_output_pipeline(pm, k_compiler, k_test_compiler, output_dir)

            # Run pipeline
            try:
                pm.runPipeline()

                # Collect output files
                # The JinjaTextFileOutput writes files directly to the output directory
                # We need to scan the output directory to find what was created
                import os
                for root, _dirs, files in os.walk(output_dir):
                    for f in files:
                        file_path = os.path.join(root, f)
                        if f.endswith('.sol'):
                            contract_files.append(file_path)
                        elif f.endswith('.js') or f.endswith('.ts'):
                            test_files.append(file_path)

                if printer.errors:
                    errors.extend(printer.errors)

                return True, errors, contract_files, test_files

            except Exception as e:
                import traceback
                errors.extend(printer.errors if printer.errors else [])
                errors.append(f"Pipeline execution error: {str(e)}")
                errors.append(traceback.format_exc())
                return False, errors, contract_files, test_files

        except Exception as e:
            import traceback
            errors.append(f"Translation error: {str(e)}")
            errors.append(traceback.format_exc())
            return False, errors, contract_files, test_files

    def generate_model_json(
        self,
        input_data: Union[str, Path, DiagramManager],
        input_type: str = "xml_string"
    ) -> Tuple[bool, List[str], Optional[str]]:
        """
        Generate JSON representation of the model.

        Args:
            input_data: Input content (string, file path, or DiagramManager)
            input_type: Type of input ("xml_string", "xml_file", or "model")

        Returns:
            Tuple of (success, errors, json_string)
        """
        try:
            printer = ServicePrinterDebug()
            pm = self._create_pipeline_manager(printer)

            # Build input pipeline
            if input_type == "xml_file":
                input_data = str(input_data)
            k_input, k_model = self._build_input_pipeline(pm, input_data, input_type)

            # If input is not a model, build validation and model generation
            if k_model is None:
                k_validator = self._build_validation_pipeline(pm, k_input, printer)
                k_model = self._build_model_generation_pipeline(pm, k_validator, printer)

            # Build JSON generation pipeline
            k_json = "k_model_to_json"
            json_generator = m_json.JsonStringModelGenerator(
                pi.PIData(k_json, [k_model]), True, indent="\t"
            )
            pm.addItem(json_generator)

            # Run pipeline
            try:
                outputs = pm.runPipeline()
                json_string = outputs.get(k_json, '{}')
                return True, [], json_string
            except Exception as e:
                errors = printer.errors if printer.errors else [str(e)]
                return False, errors, None

        except Exception as e:
            return False, [str(e)], None

    # Backwards compatibility methods
    def validate_xml(self, xml_content: str) -> Tuple[bool, List[str], Optional[object]]:
        """
        Validate XML content against DAO-ML schema.
        Backwards compatibility wrapper for validate_input.
        """
        return self.validate_input(xml_content, input_type="xml_string")
