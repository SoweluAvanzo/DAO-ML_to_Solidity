import src.pipeline.pipeline_item as pi
import src.validators.base_validator as bv


class JSONValidator(bv.BaseValidator):

    # TODO: deve ricevere un oggetto (JSON/dict) e verificare che rispetti il modello denro il model

    # 1) All Roles/Committees 's "associated_to" (which are IDs) must be among the Permissions' IDs
    # 2) All Roles' "aggregates" (which are IDs) must be existing Roles' IDs
    # 3) All Committees' "aggregates" (which are IDs) must be existing Committees' IDs
    # 4) All Roles/Committees 's "is_controlled_by" (which are IDs) must be among the Roles/Committees ' IDs
    """
    Also: (see "xml_dao_validator.py")
        check_relation_graphs(d, "aggregation_level", "aggregates"))
        check_relation_graphs(d, "federation_level", "federates_into"))
        check_cyclic_dependencies(d, "aggregates"))
        check_cyclic_dependencies(d, "federates_into"))
        check_relations_in_same_DAO(d, early_return=False))
    """

    """
    NOTE:
    "check_relations_in_same_DAO" checks if any object (Role/Committee/Relation/Permission/etc) is referring to
    something that is NOT present in the same DAO they belong.
    The possible references are: ["federates_into","aggregates","associated_to","is_controlled_by"].
    Implementation notes:
    a) for each DAO, collect all of those object IDs (including the DAO's one) into a set, which is the value of a map whose keys are the DAOs' IDs (one set for each individual DAO)
    b) for each DAO, collect all of those references (again, in a set for each DAO)
    c.1) perform the "subtraction" "b-a" (i.e., all references in "b" not present in "a")
    c.2) partition the "leftover after the subtraction" into "present in any other DAO | totally missing link" for a better debugging/printing
    c.3) IF c is empty -> ok ELSE error
    """

    def validate(self, input_to_validate: dict) -> bool:
        raise Exception("TODO : NOT IMPLEMENTED YET (31-12-2025)")
