class GovernanceAreaSplitConfiguration:
    def __init__(self, min_total_permissions_for_split: int = None):
        # TODO SOMETHING ELSE?
        self.min_total_permissions_for_split = min_total_permissions_for_split


class SolidityTranslatorConfiguration:
    """
    Holds the (key of the PipelineItems providing the) configurations a Solidity Translator Configurable depends on. This is used to avoid hardcoding the keys of the PipelineItems in the Solidity Translator Configurable, and to have a single place where to change them if needed.
    It also allows to set the Governance Area split configuration, which is used to split the Governance Area into multiple contracts if it exceeds a certain number of elements. This is useful to avoid hitting the maximum contract byte size limit of Solidity.
    """

    def __init__(self,
                 key_translator_type: str = None,
                 key_translator_version: str = None,
                 key_translator_target: str = None,
                 key_translator_solidity_subtype: str = None,
                 key_force_governance_area_split: str = None,
                 # used for GovernanceAreaSplitConfiguration
                 key_governance_area_split_configuration: str = None
                 ):
        self.key_translator_type = key_translator_type
        self.key_translator_version = key_translator_version
        self.key_translator_target = key_translator_target
        self.key_translator_solidity_subtype = key_translator_solidity_subtype
        self.key_force_governance_area_split = key_force_governance_area_split
        self.key_governance_area_split_configuration = key_governance_area_split_configuration
