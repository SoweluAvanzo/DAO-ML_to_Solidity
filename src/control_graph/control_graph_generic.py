import src.model.dao as daoModule

import src.utilities.errors as e_c


class ControlGraphGeneric:
    # TODO
    def __init__(self, dao):
        self.dao: daoModule.DAO = dao

    def has_node(self, node_id):
        return False

    def has_edge(self, source_node_id, destination_node_id):
        return False

    def get_graph_type(self):
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def is_list(self):
        raise Exception(e_c.ERROR_TEXT__NOT_IMPLEMENTED)

    def should_explicit_transitive_edges(self) -> bool:
        return False

    def manage_transitive_closure(self):
        pass

    def for_each_node(self, action=None, metadata_node_data_view: dict = None):
        pass

    def get_all_descendants_of(self, node_id) -> list:
        return None
