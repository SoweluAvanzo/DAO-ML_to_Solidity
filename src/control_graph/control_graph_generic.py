import src.model.dao as daoModule

class ControlGraphGeneric:
    # TODO
    def __init__(self, dao):
        self.dao: daoModule.DAO = dao

    def has_node(self, node_id):
        return False
    
    def has_edge(self, source_node_id, destination_node_id):
        return False

    def get_graph_type(self):
        raise Exception("Not implemented yet.")
    
    def is_list(self):
        raise Exception("Not implemented yet.")

    def should_explicit_transitive_edges(self) -> bool:
        return False

    def manage_transitive_closure(self):
        pass

    def for_each_node(self, action=None, metadata_node_data_view:dict=None):
        pass

    def get_all_descendants_of(self, node_id) -> list:
        return None

    # TODO: 2025-08-28 collection of all usages

    """


    # FROM DAOclasses


    def add_new_default_graph(self):
        self.control_graph = nx.DiGraph()

    def recalculate_graph_properties(self):
        self.graph_type = self.get_graph_type()
        if self.dao.hierarchical_inheritance == 1:
            self.control_graph =  nx.transitive_closure(self.control_graph)
            ......

    def get_graph_type(self):
        if nx.is_directed_acyclic_graph(self.control_graph):
        ....




    # ParseXML


    def visitDao(self, ctx):
    ... al fondo di ....
        for loop in nx.simple_cycles(self.daos[dao_id].dao_control_graph):




    # SimpleSolidityTranslator

    def generate_roles(self) -> list[str]:
        ...
                    topological_order = list(nx.topological_sort(G.control_graph))





    # ControlGraphBasic
    
    def recalculate_graph_properties(self):
        ...
            self.control_graph =  nx.transitive_closure(self.control_graph)


    def get_graph_type(self):
        if nx.is_directed_acyclic_graph(self.control_graph):
        ...



        


    # OptimizedSolidityTranslator

        
    def get_control_bitflags(self, role_or_committee, r_o_c_ID, group_size, functionalities_ids):
        ...
        all_controllers = list( nx.descendants(self.context.dao.dao_control_graph.control_graph, r_o_c_ID) ) \
        ...



    """


    # nx.descendants(self.context.dao.dao_control_graph.control_graph, r_o_c_ID)

