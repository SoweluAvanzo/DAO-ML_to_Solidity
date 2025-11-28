
import src.pipeline.pipeline_item as pi
import src.pipeline.utilities.pi_str as pstr
import src.pipeline.utilities.pi_any_value as pval

import src.phases_builders.shared as pb_shared
import src.phases_builders.phase_step_variants as psv
import src.phases_builders.phase_builder as pb

import src.postprocessing.model_translation.model_translator_configurable as mcc
import src.postprocessing.model_translation.translation_types as tt
import src.postprocessing.model_translation.solidity.voting_protocols_list_loader as pi_vpll
import src.postprocessing.model_translation.solidity.translation_types_solidity as transl_types_sol
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as jinja_opt_versions
import src.postprocessing.model_translation.solidity.tests.jinja.solidity_tests_translator_jinja_hardhat as sol_test_t
import src.postprocessing.model_translation.asm.t_j_asm_1_0_0 as t_j_asm_1_0_0
import src.postprocessing.model_translation.asm.translator_asm_versions as t_asm_versions

import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as t_prov_by_name
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.tpbn_txt_file as template_by_name_txt
import src.postprocessing.output_preparation.compilers.solidity.templates.jinja.c_sol_t_j_1_0_0 as c_sol_t_j_1_0_0
import src.postprocessing.output_preparation.compilers.solidity.tests.templates.jinja.c_sol_tests_t_j as c_sol_tests_t_j
import src.postprocessing.output_preparation.compilers.asm.templates.jinja.c_j_asm as c_asm_t_j
import src.postprocessing.output_preparation.json.model_to_json as pp_o_json


import src.postprocessing.consts_template as consts_t
import src.utilities.utils as u
import src.utilities.extended_enum as ee
import src.utilities.errors as e_c


class PostProcessingTransformation(psv.PhaseSubstepVariants):
    SOLIDITY = "sol"
    SOLIDITY_HARDHAT_TESTS = "sol_hardhat_tests"
    ASM = "asm"
    JSON = "json"
    # PETRI_NETS = "petri"

#


class AdditionalDataPostProcessing(pb.AdditionalDataSubPhase):
    def __init__(self, phase_step_variant: PostProcessingTransformation,
                 k_model_generator: str
                 ):
        super().__init__(phase_step_variant)
        self.k_model_generator = k_model_generator


class AdditionalDataPostProcessingTemplated(AdditionalDataPostProcessing):
    def __init__(self, phase_step_variant: PostProcessingTransformation,
                 k_model_generator: str,
                 templates_provider: t_prov_by_name.TemplateProviderByName = None,
                 version_translator: str = None,
                 version_translation_target: str = None
                 ):
        super().__init__(phase_step_variant, k_model_generator)
        self.templates_provider = templates_provider
        self.version_translator = version_translator
        self.version_translation_target = version_translation_target


class AdditionalDataSolidity(AdditionalDataPostProcessingTemplated):
    def __init__(self, k_model_generator: str,
                 folder_voting_protocols: str,
                 templates_provider: t_prov_by_name.TemplateProviderByName = None,
                 folder_templates: str = None,
                 version_translator: str = jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value,
                 translator_solidity_subtype: str = transl_types_sol.TranslationTypesSolidity.OPTIMIZED.value,
                 version_translation_target: str = "1.0.0",
                 ):
        super().__init__(PostProcessingTransformation.SOLIDITY, k_model_generator,
                         templates_provider=templates_provider,
                         version_translator=version_translator,
                         version_translation_target=version_translation_target
                         )
        self.translator_solidity_subtype = translator_solidity_subtype
        self.folder_voting_protocols = folder_voting_protocols
        self.folder_templates = folder_templates


class AdditionalDataSolidityHardhatTests(AdditionalDataPostProcessingTemplated):
    def __init__(self, k_model_generator: str,
                 templates_provider: t_prov_by_name.TemplateProviderByName = None,
                 folder_templates: str = None,
                 version_translator: str = "1.0.0",
                 version_translation_target: str = "1.0.0",
                 ):
        super().__init__(PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS, k_model_generator,
                         templates_provider=templates_provider,
                         version_translator=version_translator,
                         version_translation_target=version_translation_target
                         )
        self.folder_templates = folder_templates


class AdditionalDataASM(AdditionalDataPostProcessingTemplated):
    def __init__(self, k_model_generator: str,
                 templates_provider: t_prov_by_name.TemplateProviderByName = None,
                 folder_templates: str = None,
                 version_translator: str = t_asm_versions.ASMTranslatorVersions.ASM_1_0_0.value,
                 version_translation_target: str = t_j_asm_1_0_0.TARGET_VERSION,
                 ):
        super().__init__(PostProcessingTransformation.ASM, k_model_generator,
                         templates_provider=templates_provider,
                         version_translator=version_translator,
                         version_translation_target=version_translation_target
                         )
        self.folder_templates = folder_templates


class AdditionalDataJSON(AdditionalDataPostProcessing):
    def __init__(self, k_model_generator: str,
                 indent=None
                 ):
        super().__init__(PostProcessingTransformation.JSON, k_model_generator,)
        self.indent = indent


# class AdditionalDataPetriNets(AdditionalDataPostProcessingTemplated):
#    def __init__(self, k_model_generator: str,
#                 version_translator=None,
#                 version_translation_target=None,
#                 altro=None
#                 ):
#        super().__init__(PostProcessingTransformation.PETRI_NETS, k_model_generator,
#                         templates_provider=None,
#                         version_translator=None,
#                         version_translation_target=None)
#        self.altro = altro


#
#
#


class PostProcessingFactory(pb.PipelineItemFactory):
    def __init__(self, key_unique_producer: pb_shared.KeyUniqueProducer,
                 printer_debug: u.PrinterDebug = None):
        super().__init__(key_unique_producer, printer_debug=printer_debug)

    def get_PhaseSubstepVariants_enum(self) -> psv.PhaseSubstepVariants:
        return PostProcessingTransformation

    def new_folder_based_templates_provider(self, subphase: PostProcessingTransformation,  folder_templates: str = None) -> tuple[t_prov_by_name.TemplateProviderByName, pi.PipelineItem]:
        templates_provider = template_by_name_txt.TemplateProviderFromTxtFile(
            base_template_folder=consts_t.DEFAULT_BASE_FOLDER_TEMPLATES if folder_templates is None else folder_templates
        )
        k_pi_templates_provider = self.new_unique_key(
            f"k_pi_templates_provider_{subphase.value}")
        # the template provider must be added to the chain so that the template compiler could retrieve it and use it
        return (
            templates_provider,
            pval.PIAnyValue(
                pi.PIData(k_pi_templates_provider, None),
                templates_provider
            )
        )

    def new_pipeline_item_from_variant(self, pi_data: pi.PIData,
                                       phase_step_variant_and_data: pb.AdditionalDataSubPhase
                                       ) -> list[pi.PipelineItem]:
        if phase_step_variant_and_data.phase_step_variant == PostProcessingTransformation.SOLIDITY:
            if not isinstance(phase_step_variant_and_data, AdditionalDataSolidity):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected AdditionalDataSolidity, got: {type(phase_step_variant_and_data)}")
            k_model_generator = phase_step_variant_and_data.k_model_generator
            templates_provider = phase_step_variant_and_data.templates_provider
            folder_voting_protocols = phase_step_variant_and_data.folder_voting_protocols
            version_translator = phase_step_variant_and_data.version_translator
            translator_solidity_subtype = phase_step_variant_and_data.translator_solidity_subtype
            version_translation_target = phase_step_variant_and_data.version_translation_target
            # prepare PipelineItems
            k_translator_type_sol = self.new_unique_key(
                "k_translator_type_sol")
            pi_translator_type_sol = pstr.PIStr(
                pi.PIData(k_translator_type_sol, None),
                tt.TranslationTypes.SOLIDITY.value
            )
            k_version_translator_sol = self.new_unique_key(
                "k_version_translator_sol")
            pi_version_translator_sol = pstr.PIStr(
                pi.PIData(k_version_translator_sol, None),
                jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value if version_translator is None else version_translator
            )
            k_translator_target_sol = self.new_unique_key(
                "k_translator_target_sol")
            pi_translator_target_sol = pstr.PIStr(
                pi.PIData(k_translator_target_sol, None),
                "1.0.0" if version_translation_target is None else version_translation_target
            )
            k_translator_solidity_subtype_sol = self.new_unique_key(
                "k_translator_solidity_subtype_sol")
            pi_translator_solidity_subtype_sol = pstr.PIStr(
                pi.PIData(k_translator_solidity_subtype_sol, None),
                translator_solidity_subtype
            )
            k_all_voting_protocols_submitter = consts_t.KEY__ALL_VOTING_PROTOCOLS__ON_ADDITIONAL_DATA
            p_voting_protocol_list_loader = pi_vpll.VotingProtocolListLoader(
                pi.PIData(k_all_voting_protocols_submitter, None),
                printer_debug=self.printer_debug,
                folder_voting_protocols=folder_voting_protocols
            )

            # ... prepare the list of dependencies for the translator
            k_translator_sol = self.new_unique_key("k_translator_sol")
            translator_deps = [
                k_model_generator, k_translator_type_sol, k_version_translator_sol, k_translator_target_sol, k_translator_solidity_subtype_sol, k_all_voting_protocols_submitter
            ]
            encountered_transl_deps = set(translator_deps)
            for d in pi_data.dependencies:
                if d not in encountered_transl_deps:
                    translator_deps.append(d)
                    encountered_transl_deps.add(d)
            del encountered_transl_deps  # free the memory
            translator_sol = mcc.ModelTranslatorConfigurable(
                pi.PIData(k_translator_sol, translator_deps),
                key_model=k_model_generator,
                key_translator_type=k_translator_type_sol,
                key_translator_version=k_version_translator_sol,
                key_translator_target=k_translator_target_sol,
                printer_debug=self.printer_debug
            )

            # ... templates_provider management
            pi_templates_provider: pi.PipelineItem = None
            k_pi_templates_provider: str = None
            if templates_provider is None:  # build a new one
                folder_templates = phase_step_variant_and_data.folder_templates
                # the template provider must be added to the chain so that the template compiler could retrieve it and use it
                t_p, pi_t_p = self.new_folder_based_templates_provider(
                    subphase=phase_step_variant_and_data.phase_step_variant,
                    folder_templates=folder_templates
                )
                pi_templates_provider = pi_t_p
                phase_step_variant_and_data.templates_provider = t_p
                k_pi_templates_provider = pi_templates_provider.get_key()

            # ... compiler
            k_template_compiler_sol = self.new_unique_key(
                "k_template_compiler_sol")
            template_compiler_sol = c_sol_t_j_1_0_0.CompilerSolidityTemplateJinja_1_0_0(pi.PIData(k_template_compiler_sol, [
                k_translator_sol,
                k_model_generator,
                k_pi_templates_provider
            ]),
                key_diagram_instance_data=k_translator_sol,
                key_diagram_model=k_model_generator,
                key_template_skeleton_provider_by_name=k_pi_templates_provider,
                printer_debug=self.printer_debug
            )
            # generate the complete list
            all_pi = [
                translator_sol,  # this must be the first
                p_voting_protocol_list_loader,
                pi_translator_type_sol,
                pi_version_translator_sol,
                pi_translator_target_sol,
                pi_translator_solidity_subtype_sol
            ]
            if pi_templates_provider is not None:
                all_pi.append(pi_templates_provider)

            # now, the end
            all_pi.append(
                template_compiler_sol  # this must be the last
            )
            return all_pi

        elif phase_step_variant_and_data.phase_step_variant == PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS:
            if not isinstance(phase_step_variant_and_data, AdditionalDataSolidityHardhatTests):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected AdditionalDataSolidityHardhatTests, got: {type(phase_step_variant_and_data)}")
            # TODO: fare un "chained" di traduzione e compilazione usando :
            # - "pp_mt_sol_c" configurable
            # (2025-11-17) E PRENDERE SPUNTO DA "t_file_1.py" DA RIGA 250 IN POI
            k_model_generator = phase_step_variant_and_data.k_model_generator
            templates_provider = phase_step_variant_and_data.templates_provider

            # ... templates_provider management
            pi_templates_provider: pi.PipelineItem = None
            k_pi_templates_provider: str = None
            if templates_provider is None:  # build a new one
                folder_templates = phase_step_variant_and_data.folder_templates
                # the template provider must be added to the chain so that the template compiler could retrieve it and use it
                t_p, pi_t_p = self.new_folder_based_templates_provider(
                    subphase=phase_step_variant_and_data.phase_step_variant,
                    folder_templates=folder_templates
                )
                pi_templates_provider = pi_t_p
                phase_step_variant_and_data.templates_provider = t_p
                k_pi_templates_provider = pi_templates_provider.get_key()

            k_translator_sol_test = self.new_unique_key(
                "k_translator_sol_test")
            # TODO Hardhat Tests - currently (2025-11-28), there's no "configurable", just the "1.0.0"
            translator_sol_test = sol_test_t.SolidityTestsTranslatorJinjaHardhat_1_0_0(
                pi.PIData(k_translator_sol_test, [k_model_generator]),
                optional_external_data=None,
                key_model=k_model_generator,
                is_optimized=True
            )
            k_is_result_as_list = self.new_unique_key("k_is_result_as_list")
            pi_is_result_as_list = pval.PIAnyValue(
                pi.PIData(k_is_result_as_list, None), True)
            k_compiler_sol_test = self.new_unique_key(
                "k_compiler_sol_test")
            compiler_sol_test = c_sol_tests_t_j.CompilerSolidityTestsTemplateJinja(
                pi.PIData(k_compiler_sol_test,
                          [k_translator_sol_test, k_pi_templates_provider,
                           k_model_generator, k_is_result_as_list]
                          ),
                optional_external_data=None,
                key_diagram_instance_data=k_translator_sol_test,
                key_template_skeleton_provider_by_name=k_pi_templates_provider,
                key_diagram_model=k_model_generator,
                key_is_result_as_list=k_is_result_as_list
            )
            return [
                translator_sol_test,
                k_compiler_sol_test,
                compiler_sol_test
            ]

        elif phase_step_variant_and_data.phase_step_variant == PostProcessingTransformation.ASM:
            if not isinstance(phase_step_variant_and_data, AdditionalDataASM):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected AdditionalDataASM, got: {type(phase_step_variant_and_data)}")
            # extract info from the provided configuration data
            k_model_generator = phase_step_variant_and_data.k_model_generator
            templates_provider = phase_step_variant_and_data.templates_provider
            version_translator = phase_step_variant_and_data.version_translator
            version_translation_target = phase_step_variant_and_data.version_translation_target
            # prepare PipelineItems
            k_translator_type_asm = self.new_unique_key(
                "k_translator_type_asm")
            pi_translator_type_asm = pstr.PIStr(
                pi.PIData(k_translator_type_asm, None),
                tt.TranslationTypes.ASM.value
            )
            k_version_translator_asm = self.new_unique_key(
                "k_version_translator_asm")
            pi_version_translator_asm = pstr.PIStr(
                pi.PIData(k_version_translator_asm, None),
                t_asm_versions.ASMTranslatorVersions.ASM_1_0_0.value if version_translator is None else version_translator
            )
            k_translator_target_asm = self.new_unique_key(
                "k_translator_target_asm")
            pi_translator_target_asm = pstr.PIStr(
                pi.PIData(k_translator_target_asm, None),
                t_j_asm_1_0_0.TARGET_VERSION if version_translation_target is None else version_translation_target
            )

            k_translator_asm = self.new_unique_key("k_translator_asm")
            translator_deps = [
                k_model_generator, k_translator_type_asm, k_version_translator_asm, k_translator_target_asm,
            ]
            encountered_transl_deps = set(translator_deps)
            for d in pi_data.dependencies:
                if d not in encountered_transl_deps:
                    translator_deps.append(d)
                    encountered_transl_deps.add(d)
            del encountered_transl_deps  # free the memory
            translator_asm = mcc.ModelTranslatorConfigurable(
                pi.PIData(k_translator_asm, translator_deps),
                key_model=k_model_generator,
                key_translator_type=k_translator_type_asm,
                key_translator_version=k_version_translator_asm,
                key_translator_target=k_translator_target_asm,
                printer_debug=self.printer_debug
            )

            # ... templates_provider management
            pi_templates_provider: pi.PipelineItem = None
            k_pi_templates_provider: str = None
            if templates_provider is None:  # build a new one
                folder_templates = phase_step_variant_and_data.folder_templates
                # the template provider must be added to the chain so that the template compiler could retrieve it and use it
                t_p, pi_t_p = self.new_folder_based_templates_provider(
                    subphase=phase_step_variant_and_data.phase_step_variant,
                    folder_templates=folder_templates
                )
                pi_templates_provider = pi_t_p
                phase_step_variant_and_data.templates_provider = t_p
                k_pi_templates_provider = pi_templates_provider.get_key()

            k_is_result_as_list = self.new_unique_key("k_is_result_as_list")
            pi_is_result_as_list = pval.PIAnyValue(
                pi.PIData(k_is_result_as_list, None), True)
            k_compiler_asm = self.new_unique_key("k_compiler_asm")
            compiler_asm = c_asm_t_j.CompilerASMTemplateJinja(
                pi.PIData(k_compiler_asm, [
                    k_translator_asm, k_pi_templates_provider, k_model_generator, k_is_result_as_list
                ]),
                optional_external_data=None,
                key_diagram_instance_data=k_translator_asm,
                key_template_skeleton_provider_by_name=k_pi_templates_provider,
                key_diagram_model=k_model_generator,
                key_is_result_as_list=k_is_result_as_list
            )
            return [
                p
                for p in [
                    translator_asm,  # this must be the first
                    pi_translator_type_asm,
                    pi_version_translator_asm,
                    pi_translator_target_asm,
                    pi_is_result_as_list,
                    pi_templates_provider,
                    compiler_asm  # this must be the last
                ]
                if p is not None
            ]
        elif phase_step_variant_and_data.phase_step_variant == PostProcessingTransformation.JSON:
            if not isinstance(phase_step_variant_and_data, AdditionalDataJSON):
                raise Exception(
                    f"Wrong class for given phase_step_variant_and_data: expected AdditionalDataJSON, got: {type(phase_step_variant_and_data)}")
            return [
                pp_o_json.JsonStringModelGenerator(pi_data,
                                                   string_output_required=False,
                                                   indent=phase_step_variant_and_data.indent if "indent" in phase_step_variant_and_data else None
                                                   )
            ]
        # elif phase_step_variant_and_data.phase_step_variant == PostProcessingTransformation.PETRI_NETS:
        #    if not isinstance(phase_step_variant_and_data, AdditionalDatapetriNets):
        #        raise Exception(
        #            f"Wrong class for given phase_step_variant_and_data: expected AdditionalDatapetriNets, got: {type(phase_step_variant_and_data)}")
        #   TODO
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED +
                        " : " + phase_step_variant_and_data.phase_step_variant.value)
