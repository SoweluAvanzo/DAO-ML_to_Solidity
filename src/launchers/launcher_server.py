import src.launchers.launcher_configurable as launcher_config
import src.launchers.cmd_args as cmd_args
import src.translator_process as translator_process

# TODO create a Flask server, with an API that build a "TranslatorProcess"

"""
# SOMEWHERE ELSE ..
    tp: translator_process.TranslatorProcess = None 

IN THE API :
    config = 
    tc: launcher_config.TranslatorAndConfigurations = launcher_config.new_translator_process(
        config,
        instantiate_new_translator_process= tp is not None,
        logger=logger
    )
    if tp is None:
        tp = tc.translator_process
    
"""
