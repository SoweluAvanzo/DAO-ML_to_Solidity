import argparse

import src.configurations as configs

import src.postprocessing.model_translation.solidity.translation_types_solidity as trans_type_sol

import src.phases_builders.shared as pb_shared
import src.phases_builders.input_fetch as pb_i_f
import src.phases_builders.model_generation as pb_m_g
import src.phases_builders.postprocessing as pb_pp
import src.phases_builders.output as pb_o

import src.postprocessing.model_translation.solidity.translation_types_solidity as transl_types_sol
import src.postprocessing.model_translation.solidity.optimized.jinja.jinja_optimized_versions as jinja_opt_versions
import src.postprocessing.model_translation.asm.translator_asm_versions as t_asm_versions
import src.postprocessing.model_translation.asm.t_j_asm_1_0_0 as t_j_asm_1_0_0
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.template_provider_by_name as t_prov_by_name
import src.postprocessing.output_preparation.compilers.shared.templates.template_providers.tpbn_txt_file as template_by_name_txt


import src.utilities.extended_enum as ex_enum
import src.utilities.utils as u
import src.utilities.errors as e_c


def __tbf_combos():
    # leads to 16 combinations
    t_f_b = ["base", "template", "folder"]
    t_f_b_extended = [*t_f_b, "templates"]  # the plural
    seps = ["_", "-"]
    # the result was pre-computed, so the lenght is known in advance
    tbfc = [None] * (8 * len(seps))
    combination = [None] * len(t_f_b)
    i = 0
    for a in t_f_b_extended:
        combination[0] = a
        for b in t_f_b:
            if (a != b) and (not a.startswith(b)):
                combination[1] = b
                for c in t_f_b:
                    if (a != c) and (b != c) \
                            and (not a.startswith(c)):
                        combination[2] = c
                        for sep in seps:
                            tbfc[i] = f"--{sep.join(combination)}"
                            i += 1
    tbfc.sort()
    return tbfc


global templates_base_folder_combinations
templates_base_folder_combinations = __tbf_combos()


def __enum_case_insensitive_list(e: type[ex_enum.ExtendedEnum]):
    s = set(e.list())
    for k in list(map(lambda c: c.name, e)):
        s.add(k)
    return list(s)


def __cj(l: list):
    ", ".join(l)


def __enum_comma_list(e: type[ex_enum.ExtendedEnum]):
    return __cj(__enum_case_insensitive_list(e))

#


def get_args(logger: u.PrinterDebug = None):
    parser = argparse.ArgumentParser(
        description="CLI Parser for DAO-ML Translator"
    )

    # input

    parser.add_argument(
        "-f", "--file",
        "--file-name", "--file_name",
        "--file-path", "--file_path",
        "-i", "--input", "--input_uri", "--input-uri",
        type=str,
        help="file name/path of the (XML?) DAO (Diagram, actually) You need to process",
        required=False
    )
    parser.add_argument(
        "-if", "--input_base_folder", "--input-base-folder", "--input-folder", "--input_folder",
        type=str,
        help="folder path acting as the starting point for all inputs",
        required=False
    )
    l_if = __enum_case_insensitive_list(pb_shared.ModelPersistanceFormat)
    parser.add_argument(
        "-i_f", "--input_format",
        "--input-format",
        type=str,
        help=f"Format of the input in which the model has been encoded; currently the accepted values are the following ones: {__cj(l_if)}",
        choices=l_if,
        required=False
    )
    parser.add_argument(
        "-fie", "--file_input_extension", "--file-input-extension",
        type=str,
        help="Extension of the input file",
        required=False
    )
    l_pt = __enum_case_insensitive_list(pb_shared.PersistanceType)
    parser.add_argument(
        "-pt", "--persistance_type", "--persistance-type",
        type=str,
        help=f"Types of persistance units to read the model from or to save the produced output; currently it accepts: {__cj(l_pt)}",
        choices=l_pt,
        required=False
    )
    # ... xml
    parser.add_argument(
        "-xml_v", "--xml_version", "--xml-version",
        type=str,
        help="Version of the XML standard (as input)",
        required=False
    )
    # TODO: add Databse URI / API endpoint parameters

    # model generation
    # ... xml, currently (2025-12-12) no other formats have some configurations
    parser.add_argument(
        "--xml_schema_folder", "--xml-schema-folder",
        type=str,
        help="Folder path holding the XML schema file",
        required=False
    )
    parser.add_argument(
        "--xml_schema_filename", "--xml-schema-filename",
        type=str,
        help="Folder path holding the XML schema file",
        required=False
    )
    parser.add_argument(
        "--xml_schema_extension", "--xml-schema-extension",
        type=str,
        help="Extension of the XML schema file",
        required=False
    )

    # postprocessing
    ppt_options = __enum_case_insensitive_list(
        pb_pp.PostProcessingTransformation)
    parser.add_argument(
        "-pp", "-ppt",
        "--post_processing_transformation", "--post-processing-transformation",
        "--post_processing", "--post-processing",
        type=str,
        help=f"Post-processing phase, one(+) of the following: [{__cj(ppt_options)}]",
        required=True,
        choices=ppt_options,
        action="append"
    )
    parser.add_argument(
        "-vt", "-vtr", "--version_translator", "--version-translator",
        type=str,
        help="Version of the translator. Defaults to '1.0.0'",
        default=[],
        required=False,
        action="append"
    )
    parser.add_argument(
        "--version_translation_target",  "--version-translation-target",
        "--version_translation",  "--version-translation",
        "--version_target",  "--version-target",
        type=str,
        help="Version of what is being produced as output; multiple evolutions might co-exists (in futrher developments). Defaults to '1.0.0'",
        default=[],
        required=False,
        action="append"
    )
    folder_templates_options = list(set([
        "-tfb", "-btf", "-ftb",
        *templates_base_folder_combinations,
        "-tf", "--templates-folder", "--templates_folder", "--template-folder", "--template_folder",
        "-ft", "--folder_templates", "--folder-templates", "--folder_template", "--folder-template"
    ]))
    print(f"folder_templates_options: {folder_templates_options}")
    parser.add_argument(
        "--base_template_folder",
        *folder_templates_options,
        type=str,
        help="folder (base) path for all template files; could be an absolute path or a relative path.",
        required=False,
        action="append"
    )
    # ... solidity
    # tt_sol = trans_type_sol.TranslationTypesSolidity.list()
    # parser.add_argument(
    #     "-tss", "--translator_solidity_subtype", "--translator-solidity-subtype",
    #     help=f"Types of Solidity-specific translations; available values: [{', '.join(tt_sol)}]",
    #     default=trans_type_sol.TranslationTypesSolidity.OPTIMIZED.value,
    #     choices=tt_sol,
    #     required=False
    # )
    parser.add_argument(
        "-fvps", "--folder_voting_protocols_solidity", "--folder-voting-protocols-solidity",
        "-sfvp", "--solidity_folder_voting_protocols", "--solidity-folder-voting-protocols",
        "-fps", "--folder_voting_solidity", "--folder-voting-solidity",
        "-sfp", "--solidity_folder_voting", "--solidity-folder-voting",
        type=str,
        help="folder (base) path for all voting protocol template files; could be an absolute path or a relative path.",
        required=False,
        action="append"
    )
    # json
    parser.add_argument(
        "-ij", "--indent_json", "--indent-json",
        help="Indentation for JSON dumping",
        default=None,
        required=False,
        action="append"
    )

    # output

    ot_options = pb_o.OutputType.list()
    parser.add_argument(
        "-ot", "--output_type", "--output-type",
        type=str,
        help=f"Output type, which depends upon the related Post Processing Translation: either a plain text (used for JSON) or a Jinja-based template (currently used for Solidity, Solidity Hardhat Test or ASM); current available options: [{__cj(ot_options)}]",
        required=True,
        choices=ot_options,
        action="append"
    )

    l_pt = __enum_case_insensitive_list(pb_shared.PersistanceType)
    parser.add_argument(
        "-op", "-opt",
        "--output_persistance", "--output-persistance",
        "--output_persistance_type", "--output-persistance-type",
        type=str,
        help=f"Types of persistance ends to output the result of the related Post Processing Translation; currently it accepts: {__cj(l_pt)}",
        choices=l_pt,
        required=True,
        action="append"
    )

    parser.add_argument(
        "-ouri", "--output", "--output-uri", "--output_uri",
        type=str,
        help="URI for the output (a folder path for the File-based ones, a onnection string for); if it's specified once, then it's applied to all outpts. If multiple postprocessing are defined and some (but not all) of them requires a file-based output, then You can shortcut the outputs entries: at first, define the first postprocessing with the file output and the folder path as this flag value, then define all non-file-outputting postprocessing, then define the last postprocessing omitting the output-uri, so that they will inherit the value.",
        required=False,
        action="append"
    )

    # ---------

    args = parser.parse_args()

    cmd_configs = configs.TranslatorConfigs()

    # input

    is_input_file = False
    if args.persistance_type:
        match(args.persistance_type):
            case pb_shared.PersistanceType.DATABASE.value:
                raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED + ": Database")
            case pb_shared.PersistanceType.FILE.value:
                is_input_file = True  # see below the "file" part to recycle that part
            case _:
                raise Exception(
                    f"{e_c.ERROR_TEXT__NOT_IMPLEMENTED} : {args.persistance_type}")

    if is_input_file or args.file:
        cmd_configs.input_config.source_uri = args.file
        cmd_configs.input_config.persistance_type = pb_shared.PersistanceType.FILE
        if args.input_base_folder:
            cmd_configs.input_config.file_base_folder = args.input_base_folder
    if args.input_format:
        match(args.input_format):
            case pb_shared.ModelPersistanceFormat.JSON.value:
                cmd_configs.model_format = pb_shared.ModelPersistanceFormat.JSON
                cmd_configs.input_config.file_extension = pb_shared.ModelPersistanceFormat.JSON.value \
                    if args.file_input_extension is None else args.file_input_extension
            case pb_shared.ModelPersistanceFormat.XML.value:
                cmd_configs.model_format = pb_shared.ModelPersistanceFormat.XML
                cmd_configs.input_config.file_extension = pb_shared.ModelPersistanceFormat.XML.value \
                    if args.file_input_extension is None else args.file_input_extension
                if args.xml_version:
                    cmd_configs.input_config.xml_version = args.xml_version
            case _:
                raise Exception(
                    f"{e_c.ERROR_TEXT__NOT_IMPLEMENTED} : {args.input_format}")
    # model
    if cmd_configs.model_format == pb_shared.ModelPersistanceFormat.XML:
        if args.xml_schema_folder or args.input_base_folder:
            cmd_configs.model_gen_config.xml_schema_folder = args.input_base_folder \
                if args.xml_schema_folder is None else args.xml_schema_folder
        else:
            raise Exception(
                f"XML has been choosen as the input / model generation format, but no xml_schema_folder has been set")
        if args.xml_schema_filename:
            cmd_configs.model_gen_config.xml_schema_filename = args.xml_schema_filename
        else:
            raise Exception(
                f"XML has been choosen as the input / model generation format, but no xml_schema_filename has been set")
        if args.xml_schema_extension:
            cmd_configs.model_gen_config.xml_schema_extension = args.xml_schema_extension
        else:
            raise Exception(
                f"XML has been choosen as the input / model generation format, but no xml_schema_extension has been set")

    # postprocessing & output

    # ... first, checks the mandatory fields
    if (not args.post_processing_transformation) or (len(args.post_processing_transformation) <= 0):
        raise Exception(
            f"post_processing_transformation (multi)flag is required")
    if (not args.output_type) or (len(args.output_type) <= 0):
        raise Exception(
            f"output_type (multi)flag is required")
    if (not args.output_persistance) or (len(args.output_persistance) <= 0):
        raise Exception(
            f"output_persistance (multi)flag is required")
    if (not args.output) or (len(args.output) <= 0):
        raise Exception(
            f"output (or output_uri) (multi)flag is required")

    if len(args.output_type) != len(args.output_persistance):
        raise Exception(
            f"output_type amount of entries ({len(args.output_type)}) is different than the output_persistance ones ({len(args.output_persistance)})")

    # (see the "help" section for output_uri)
    output_folder_default: str = None
    index_ppt_version_translator = 0  # solidity
    index_ppt_translation_target = 0  # solidity
    index_ppt_indent_json = 0  # json
    index_output_uri = 0
    index_output_persistance_types = 0  # both output_type and output_persistance
    index_folder_voting_protocols_solidity = 0
    index_base_template_folder = 0
    pairs_ppt_o: list[configs.PostprocessingOutputPairConfigs] = []

    # ... if this is the first entry, then store it if it's FILE (see the "help" section for output_uri)
    if args.output_persistance[0] == pb_shared.PersistanceType.FILE.value:
        output_folder_default = args.output[0]
    elif len(args.output_type) != len(args.post_processing_transformation):
        raise Exception(
            f"post_processing_transformation amount of entries ({args.post_processing_transformation}) must be equal to the output ones (both output_type and persistance_type: {len(args.persistance_type)}) because there is no default configuration for non-defined output entries")

    logger.print_msg(f"output_folder_default -> {output_folder_default}")
    logger.print_msg(
        f"args.post_processing_transformation -> {args.post_processing_transformation}")
    logger.print_msg(
        f"args.base_template_folder -> {args.base_template_folder}")
    logger.print_msg(
        f"args.version_translator -> {args.version_translator}")
    logger.print_msg(
        f"args.version_translation_target -> {args.version_translation_target}")
    logger.print_msg(
        f"args.output_persistance -> {args.output_persistance}")
    logger.print_msg(
        f"args.output_type -> {args.output_type}")
    logger.print_msg(
        f"args.output -> {args.output}")
    logger.print_msg(
        f"args.folder_voting_protocols_solidity -> {args.folder_voting_protocols_solidity}")

    ppts: list[str] = args.post_processing_transformation
    for index_post_processing_transformation in range(len(ppts)):
        ppt_c = configs.PostprocessingConfigs()
        o_c = configs.OutputConfigs()
        # get the most important fields
        ppt = pb_pp.REVERSE_MAPPING_PostProcessingTransformation[
            ppts[index_post_processing_transformation]
        ]
        version_translator_str: str = args.version_translator[index_ppt_version_translator] \
            if index_ppt_version_translator < len(args.version_translator) \
            else None
        translation_target_str: str = args.version_translation_target[index_ppt_translation_target] \
            if index_ppt_translation_target < len(args.version_translation_target) \
            else None
        output_persistance_type_str: str = args.output_persistance[index_output_persistance_types] \
            if index_output_persistance_types < len(args.output_persistance) \
            else None
        output_type_str: str = args.output_type[index_output_persistance_types] \
            if index_output_persistance_types < len(args.output_type) \
            else None
        output_uri_str: str = args.output[index_output_uri] \
            if index_output_uri < len(args.output) \
            else None
        base_template_folder_str: str = args.base_template_folder[index_base_template_folder] \
            if index_base_template_folder < len(args.base_template_folder) \
            else None
        # set the most important and mandatory fields
        # ... post processing transformation
        ppt_c.post_processing_transformation = ppt
        if version_translator_str is not None:
            ppt_c.version_translator = version_translator_str
            index_ppt_version_translator += 1
        print(
            f"\n\n DEBUG: translation_target_str : {translation_target_str}, type: {type(translation_target_str)} \n\n")
        if translation_target_str is not None:
            ppt_c.version_translation_target = translation_target_str
            index_ppt_translation_target += 1

        print(
            f"\n\n DEBUG: ppt_c.version_translation_target : {ppt_c.version_translation_target}, type: {type(ppt_c.version_translation_target)} \n\n")
        # ... output
        if output_type_str is not None:
            o_c.output_type = pb_o.REVERSE_MAPPING_OutputType[output_type_str]
            index_output_persistance_types += 1
        if output_persistance_type_str is not None:
            o_c.persistance_type = pb_shared.REVERSE_MAPPING_PersistanceType[
                output_persistance_type_str]
        o_c.output_uri = output_folder_default if output_uri_str is None else output_uri_str

        # now, the complex part
        index_output_uri += 1
        match(ppt.value):
            case pb_pp.PostProcessingTransformation.SOLIDITY.value \
                | pb_pp.PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS.value \
                    | pb_pp.PostProcessingTransformation.ASM.value:
                # | pb_pp.PostProcessingTransformation.PETRI_NETS.value \
                base_template_folder = output_folder_default if \
                    base_template_folder_str is None else base_template_folder_str
                print(
                    f"AJAJJAJAJJA DEBUUUUUUUU        base_template_folder: {base_template_folder} ,,, output_uri_str: {output_uri_str}")
                ppt_c.base_template_folder = base_template_folder
                if ppt == pb_pp.PostProcessingTransformation.SOLIDITY \
                        or ppt == pb_pp.PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS:
                    ppt_c.folder_voting_protocols_solidity = \
                        args.folder_voting_protocols_solidity[index_folder_voting_protocols_solidity] \
                        if index_folder_voting_protocols_solidity < len(args.folder_voting_protocols_solidity) \
                        else base_template_folder
                    print(
                        f"folder_voting_protocols_solidity .... len: {len(args.folder_voting_protocols_solidity)}, args.folder_voting_protocols_solidity: {args.folder_voting_protocols_solidity}")
                    print(
                        f"... ... index_folder_voting_protocols_solidity: {index_folder_voting_protocols_solidity} ,,, base_template_folder: {base_template_folder}")
                    index_folder_voting_protocols_solidity += 1
                    ppt_c.translator_solidity_subtype = trans_type_sol.TranslationTypesSolidity.OPTIMIZED.value  # by default
                match(ppt.value):
                    case pb_pp.PostProcessingTransformation.SOLIDITY.value:
                        if (ppt_c.version_translator is None) or (ppt_c.version_translator not in jinja_opt_versions.JinjaOptimizedVersions):
                            ppt_c.version_translator = jinja_opt_versions.JinjaOptimizedVersions.JO_1_0_0.value
                    case pb_pp.PostProcessingTransformation.SOLIDITY_HARDHAT_TESTS.value:
                        if (ppt_c.version_translator is None):
                            # currently (2025-12-18) it's not generalized (and there's just one version)
                            ppt_c.version_translator = "1.0.0"
                    case pb_pp.PostProcessingTransformation.ASM.value:
                        if (ppt_c.version_translator is None) or (ppt_c.version_translator not in t_asm_versions.ASMTranslatorVersions):
                            ppt_c.version_translator = t_asm_versions.ASMTranslatorVersions.ASM_1_0_0.value

            case pb_pp.PostProcessingTransformation.JSON.value:
                ppt_c.indent_json = args.indent_json[index_ppt_indent_json] \
                    if index_ppt_indent_json < len(args.indent_json) \
                    else None
                if ppt_c.indent_json is not None:
                    if str.isdigit(ppt_c.indent_json):
                        ppt_c.indent_json = int(ppt_c.indent_json)
                index_ppt_indent_json += 1
            case _:
                raise Exception(
                    f"On postprocessing #{index_post_processing_transformation}, unrecognized / unmanageable PostProcessingTransformation: {ppt}")
        #
        """
        # TODO: fill with future (2025-12-17) developments
        match(output_type_str):
            case pb_o.OutputType.JINJA_COMPILATION.value:
                match(output_persistance_type_str):
                    case(pb_shared.PersistanceType.FILE.value):
                    case _:
                        raise Exception(
                            f"On postprocessing #{index_post_processing_transformation}, unrecognized / unmanageable output_persistance_type_str: {output_persistance_type_str}")
            case pb_o.OutputType.PLAIN_STRING.value:
                match(output_persistance_type_str):
                    case(pb_shared.PersistanceType.FILE.value):
                    case _:
                        raise Exception(
                            f"On postprocessing #{index_post_processing_transformation}, unrecognized / unmanageable output_persistance_type_str: {output_persistance_type_str}")
            case _:
                raise Exception(
                    f"On output #{index_post_processing_transformation}, unrecognized / unmanageable output_type: {output_type_str}")
        """
        # ... then ...
        pairs_ppt_o.append(
            configs.PostprocessingOutputPairConfigs(
                postprocessingConfigs=ppt_c,
                outputConfigs=o_c
            )
        )
    cmd_configs.all_postprocessingOutputPairConfigs = pairs_ppt_o

    if logger:
        logger.print_msg(cmd_configs.to_string(indent="\t\t"))

    return cmd_configs
