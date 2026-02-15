class GovernanceAreaSplitConfiguration:
    """
        Allows to set the Governance Area split configuration, which is used to split the Governance Area into multiple contracts if it exceeds a certain number of elements. This is useful to avoid hitting the maximum contract byte size limit of Solidity.
    """

    def __init__(self,
                 force_governance_area_split: bool = False,
                 min_total_permissions_for_split: int = None
                 ):
        self.min_total_permissions_for_split = min_total_permissions_for_split
        self.force_governance_area_split = force_governance_area_split
        # TODO SOMETHING ELSE?
