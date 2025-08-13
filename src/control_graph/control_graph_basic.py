import networkx as nx

import src.model.dao as d
import src.model.enums.graph_type as gt
import src.control_graph.control_graph_generic as cgg

class ControlGraphBasic(cgg.ControlGraphGeneric):
    """
    This implementation make use of the "networkx" package.
    """
    def __init__(self, dao:d.DAO, \
                keep_original_on_transitive_closure=False
            ):
        super().__init__(dao)
        self.control_graph: nx.DiGraph = None
        self.original_control_graph: nx.DiGraph = None
        self.graph_type: gt.GraphType = None #is calculated before the transitive closure is applied in case of hierarchical inheritance
        self.is_cyclic = False #hypotesis
        self.keep_original_on_transitive_closure = keep_original_on_transitive_closure
        self.is_already_transitive_closed = False # no transitive closure performed yet
        self.create_control_graph()


    def has_node(self, node_id):
        if self.control_graph is None:
            return None
        return self.control_graph.has_node(node_id)
    

    def has_edge(self, source_node_id, destination_node_id):
        if self.control_graph is None:
            return None
        if (not self.has_node(source_node_id)) or (not self.has_node(destination_node_id)):
            return None
        return self.control_graph.has_edge(source_node_id, destination_node_id)


    def create_control_graph(self):
        self.add_new_default_graph()
        for role in self.dao.roles.values():
            #self.control_graph.add_node(role.role_id, color="blue", size=10)
            for controller in role.controllers:
                self.control_graph.add_edge(role.get_id(),controller)
        for committee in self.dao.committees.values():
            for controller in committee.controllers:
                self.control_graph.add_edge(committee.get_id(),controller)
            #print(f'Control graph generated for DAO {self.dao.dao_id} \nPrinting edges and nodes \n')
            #assignment of control graph to DAO object
            # print edges
            # for node in self.control_graph.nodes:
            #     print(f'Node: {node} \n')
            # for edge in self.control_graph.edges:
            #     print(f'Edge: {edge} \n')
            # print("now simple cycles!")
            #print paths
        #     for loop in nx.simple_cycles(self.control_graph):
        #         print(f'Loop: {loop} \n') 
        # print("now recalculate properties")
        self.recalculate_graph_properties()
        # print(f'Control graph updated and calculated properties. The graph type is {self.graph_type}, and it is {self.is_cyclic} that the graph is cyclic \nPrinting edges and nodes \n')


    def add_new_default_graph(self):
        self.is_already_transitive_closed = False
        self.control_graph = nx.DiGraph()
        self.original_control_graph = self.control_graph


    def should_explicit_transitive_edges(self) -> bool:
        return self.dao.hierarchical_inheritance == 1


    def manage_transitive_closure(self):
        if self.should_explicit_transitive_edges() and not self.is_already_transitive_closed:
            transitive_closed = nx.transitive_closure(self.control_graph)
            self.original_control_graph = self.control_graph if self.keep_original_on_transitive_closure else transitive_closed
            self.control_graph = transitive_closed
            self.is_already_transitive_closed = True


    def recalculate_graph_properties(self):
        self.graph_type = self.get_graph_type()
        self.manage_transitive_closure()


    def get_graph_type(self):
        if self.control_graph is None:
            return None
        if self.graph_type is not None:
            return self.graph_type
        if nx.is_directed_acyclic_graph(self.control_graph):
            if self.is_list():
                self.graph_type = gt.GraphType.LIST #the graph is a list and doesn't contain cycles
            else:
                self.graph_type = gt.GraphType.DAG #the graph is a DAG, but not a list
        else:
            self.is_cyclic = True
            self.graph_type = gt.GraphType.GRAPH #the graph contains cycles
        return self.graph_type


    def is_list(self):
        if self.control_graph is None:
            return False
        return all(self.control_graph.out_degree(n) <= 1 for n in self.control_graph.nodes)


    def for_each_node(self, action=None, metadata_node_data_view:dict=None):
        if action is None or self.control_graph is None:
            return
        for node in list(self.control_graph.nodes(data= \
                        metadata_node_data_view['data'] if metadata_node_data_view is not None and 'data' in metadata_node_data_view else False) \
            ):
            if node is not None:
                action(node)


    def get_all_descendants_of(self, node_id) -> list:
        if self.control_graph is None:
            return None
        return nx.descendants(self.control_graph, node_id)
