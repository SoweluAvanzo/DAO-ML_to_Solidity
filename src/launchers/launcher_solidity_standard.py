import src.translator_process as translator_process

import src.phases_builders.shared as pb_shared

import src.utilities.utils as u
# import src.utilities.logger_debug as logger_debug

logger = u.PrinterDebug()  # logger_debug.LoggerDebug(class_name=__name__)
external_unique_key_producer: pb_shared.KeyUniqueProducer = pb_shared.KeyUniqueProducerSimpleSequential()

# TODO setup the ...

# translator_process.InputConfiguration
# translator_process.ModelConfiguration
# [translator_process.PostprocessingOutput] : list of ...
# ... translator_process.PostprocessingConfiguration
# ... translator_process.OutputConfiguration

tp = translator_process.TranslatorProcess(
    None,  # TODO: input_configuration
    None,  # TODO: model_configuration
    None,  # TODO: postprocessing_output_configurations
    # TODO
    printer_debug=logger,
    external_unique_key_producer=external_unique_key_producer
)

logger.print_msg("START\n\n")
tp.translate()
logger.print_msg("\n\nEND")
