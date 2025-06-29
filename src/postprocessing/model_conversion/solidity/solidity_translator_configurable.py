import src.pipeline.pipeline_item as pi
import src.postprocessing.model_conversion.solidity.solidity_translator_general as sol_transl_general


class TranslatorConfigurable(sol_transl_general.TranslatorGeneral):
    
    def __init__(self, pipeline_item_data: pi.PIData):
        super().__init__(pipeline_item_data)

    def translate(self, additional_data=None):
        return None

    """
    TODO:
    take inspiration from the old version:


    
    class SolidityTranslator(Translator):
        def __init__(self, dao, translation_type, additional_metadata = None, diamond=False):
            self.dao = dao
            self.translation_type = translation_type
            self.additional_metadata = additional_metadata
            self.diamond = diamond
            # set the translator that these parameters are enforcing
            self.translator_proxy:Translator = None
            # voting_protocol_translator = VotingProtocolTranslator() #TODO: instanziare il traduttore del protocollo di voto
            group_size = self.dao.metadata.user_functionalities_group_size
            if self.translation_type == "simple" or group_size == None:
                self.translator_proxy = SimpleSolidityTranslator(self.dao) # , voting_protocol_translator)
            elif self.translation_type == "optimized":
                if self.diamond == True:
                    self.translator_proxy = OptimizedDiamondTranslator(self.dao)
                else:
                    self.translator_proxy = OptimizedSolidityTranslator(self.dao) # , voting_protocol_translator)
            else:
                raise ValueError("Invalid translation type")
            # continue to mimic the proxy by overriding all this instances' values with the proxy ones
            self.context = self.translator_proxy.context

        def translate(self) -> list[TranslatedSmartContract]:
            # call the pre-calculated proxy
            return self.translator_proxy.translate()

    """