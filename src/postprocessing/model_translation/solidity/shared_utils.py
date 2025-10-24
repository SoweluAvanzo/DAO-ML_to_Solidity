
import src.model.enums.user_functionalities_group_size as user_functionalities_group_size_module
import src.model.enums.entity_type_controllable as etc
import src.model.dao as d
import src.model.aggregable_entity as aggregable_e

import src.files.file_utils as fu

"""
Just a bunch of functionalities that are shared among many translators
"""


def get_DAO_functionalities_ids(dao: d.DAO):
    i = 0
    functionalities_ids: dict[str, int] = {}
    for role in dao.roles.values():
        functionalities_ids[role.get_id()] = i
        i += 1
    for committee in dao.committees.values():
        functionalities_ids[committee.get_id()] = i
        i += 1
    return functionalities_ids


def newEntityData(final_id=0, name="", index=-1, original_id="", address="", entity_type: etc.EntityTypeControllable = None, mask: int = -1):
    if entity_type == None:
        entity_type = etc.EntityTypeControllable.ROLE.value  # default
    return {
        "final_id": final_id,
        "name": name,
        "index": index,
        "original_id": original_id,
        "address": address,
        "entity_type": entity_type,
        "mask": mask
    }


def get_control_bitflags(
    dao: d.DAO,
    role_or_committee: aggregable_e.AggregableEntity,
    group_size: user_functionalities_group_size_module.UserFunctionalitiesGroupSize,
    functionalities_ids: dict[str, int]
):
    r_o_c_ID = role_or_committee.get_id()
    bits_for_id = group_size.value[1]
    mask = 0
    is_transitive = dao.hierarchical_inheritance == 1 or dao.hierarchical_inheritance == "1"
    if not dao.dao_control_graph.has_node(r_o_c_ID):
        return 0, 0
    all_controllers = dao.dao_control_graph.get_all_descendants_of(r_o_c_ID) \
        if is_transitive else \
        role_or_committee.controllers
    if is_transitive and dao.dao_control_graph.has_edge(r_o_c_ID, r_o_c_ID):
        all_controllers.append(r_o_c_ID)
    for controller in all_controllers:
        index = functionalities_ids[controller]
        mask |= (1 << index)
    return mask << bits_for_id, mask


def get_roles_committee_computed_data(dao: d.DAO, functionalities_ids: dict[str, int], group_size: int):
    # entities_amount = len(dao.roles) + len(dao.committees)
    index_entity = 0
    entity_to_data = {}
    roles_computed_data = {}
    committees_computed_data = {}
    i = 0
    for role in dao.roles.values():
        mask_shifted_for_id_bits, original_mask = get_control_bitflags(
            dao, role,   group_size, functionalities_ids)
        final_id = functionalities_ids[role.get_id(
        )] | mask_shifted_for_id_bits
        name_sanitized = fu.sanitize_filename(role.role_name)
        ed = newEntityData(
            final_id=final_id,
            name=name_sanitized,
            index=index_entity,
            original_id=role.get_id(),
            # shouldn't I use "i" rather than "index_identity"???
            address=f"addr{index_entity}",
            entity_type=etc.EntityTypeControllable.ROLE.value,
            mask=original_mask
        )
        entity_to_data[role.get_id()] = ed
        roles_computed_data[role.get_id()] = ed
        index_entity += 1
        i += 1
    i = 0
    for committee in dao.committees.values():
        mask_shifted_for_id_bits, original_mask = get_control_bitflags(
            dao, committee,   group_size, functionalities_ids)
        final_id = functionalities_ids[committee.get_id(
        )] | mask_shifted_for_id_bits
        name_sanitized = fu.sanitize_filename(committee.committee_description)
        ed = newEntityData(
            final_id=final_id,
            name=name_sanitized,
            index=index_entity,
            original_id=committee.get_id(),
            # shouldn't I use "i" rather than "index_identity"???
            address=f"addr{index_entity}",
            entity_type=etc.EntityTypeControllable.COMMITTEE.value,
            mask=original_mask
        )
        entity_to_data[committee.get_id()] = ed
        committees_computed_data[committee.get_id()] = ed
        index_entity += 1
        i += 1
    return {
        "entity_to_data": entity_to_data,
        "roles_computed_data": roles_computed_data,
        "committees_computed_data": committees_computed_data
    }


# see "optimized_translator.newEntityData(...)"
def addresses_by_entities_data(dao: d.DAO, entity_to_data: dict[str, dict]) -> dict[int, dict[str, any]]:
    addr_E_By_E_ID = {}  # "address entity by entity ID"
    owner_role = dao.owner_role
    address_role = "owner"

    entity_data_by_original_id = {
        e['original_id']: e for e in entity_to_data.values()}

    # reminder: the "final_id" is the justapposition of "bitmasn" + "id"
    i = 0
    owner_id = owner_role.get_id()
    for entity_id in dao.roles.keys():  # note: type "entity_id" == str
        if owner_id != entity_id:
            entity_data = entity_data_by_original_id[entity_id]
            entity_data['address'] = f"addr{i}"
            addr_E_By_E_ID[entity_data['final_id']] = entity_data['address']
            i += 1
    entity_data = entity_data_by_original_id[owner_id]
    addr_E_By_E_ID[entity_data['final_id']] = address_role
    i += 1
    for entity_id in dao.committees.keys():
        entity_data = entity_data_by_original_id[entity_id]
        entity_data['address'] = f"addr{i}"
        addr_E_By_E_ID[entity_data['final_id']] = entity_data['address']
        i += 1
    return addr_E_By_E_ID
