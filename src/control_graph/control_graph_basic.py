import networkx as nx

import src.model.dao as d
import src.model.enums.graph_type as gt
import src.control_graph.control_graph_generic as cgg

class ControlGraphBasic(cgg.ControlGraphGeneric):
    def __init__(self, dao:d.DAO):
        super().__init__(dao)
        self.control_graph: nx.DiGraph = None
        self.graph_type: gt.GraphType = None #is calculated before the transitive closure is applied in case of hierarchical inheritance
        self.is_cyclic = False #hypotesis
        self.create_control_graph()
    

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
        self.control_graph = nx.DiGraph()

    def recalculate_graph_properties(self):
        self.graph_type = self.get_graph_type()
        if self.dao.hierarchical_inheritance == 1:
            self.control_graph =  nx.transitive_closure(self.control_graph)
        

    def get_graph_type(self):
        if nx.is_directed_acyclic_graph(self.control_graph):
            if self.is_list():
                print("the control graph is a list and doesn't contain cycles")
                return gt.GraphType.LIST #the graph is a list and doesn't contain cycles
            else:
                return gt.GraphType.DAG #the graph is a DAG, but not a list
        else:
            self.is_cyclic = True
            return gt.GraphType.GRAPH #the graph contains cycles
        
    def is_list(self):
        return all(self.control_graph.out_degree(n) <= 1 for n in self.control_graph.nodes)
    