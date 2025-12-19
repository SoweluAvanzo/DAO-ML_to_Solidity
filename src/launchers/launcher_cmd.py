# TUTTO configurabile da argomenti di linea di comando

import src.launchers.cmd_args as cmd_args
import src.translator_process as translator_process
import src.launchers.launcher_configurable as launcher_config
import src.configurations as configs

import src.utilities.utils as u

# import src.utilities.logger_debug as logger_debug

logger = u.PrinterDebug()  # logger_debug.LoggerDebug(class_name=__name__)


def main(args: configs.TranslatorConfigs = None):
    if args is None:
        args = cmd_args.get_args(logger=logger)
    tp: translator_process.TranslatorProcess = None
    logger.print_msg("START\n\n")
    tc: launcher_config.TranslatorAndConfigurations = launcher_config.new_translator_process(
        args,
        instantiate_new_translator_process=True,
        logger=logger,
    )
    tp = tc.translator_process
    tp.translate(
        tc.translation_configuration
    )
    logger.print_msg("\n\nEND")

#
#
#

# python -m src.launchers.launcher_cmd --file "asd.xml" --.... > lss.txt


if __name__ == "__main__":
    main(None)
