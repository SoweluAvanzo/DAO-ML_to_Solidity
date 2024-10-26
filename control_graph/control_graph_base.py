import networkx as nx

# from ..model.control_graph_generic import ControlGraphGeneric
# from ..model.enums.graph_type import GraphType
import model.control_graph_generic as control_graph_generic #ControlGraphGeneric
import model.enums.graph_type as graph_type #GraphType

class ControlGraphBase(control_graph_generic.ControlGraphGeneric):
    '''
    First, simple implementation of the control graph (controlling Role, Committee
    and the ability to perform operations onto one another).
    '''
    def __init__(self, dao):
        super().__init__(dao)
        self.control_graph: nx.DiGraph = None
        self.graph_type: graph_type.GraphType = None #is calculated before the transitive closure is applied in case of hierarchical inheritance
        self.is_cyclic = False #hypotesis
        self.create_control_graph()

    def create_control_graph(self):
        self.add_new_default_graph()
        for role in self.dao.roles.values():
            #self.control_graph.add_node(role.id, color="blue", size=10)
            for controller in role.controllers:
                self.control_graph.add_edge(role.id,controller)
        for committee in self.dao.committees.values():
            #self.control_graph.add_node(committee.id, color="red", size=25)
            for controller in committee.controllers:
                self.control_graph.add_edge(committee.id,controller)
            print(f'Control graph generated for DAO {self.dao.id} \nPrinting edges and nodes \n')
            #assignment of control graph to DAO object
            # print edges
            for node in self.control_graph.nodes:
                print(f'Node: {node} \n')
            for edge in self.control_graph.edges:
                print(f'Edge: {edge} \n')
            print("now simple cycles!")
            #print paths
            for loop in nx.simple_cycles(self.control_graph):
                print(f'Loop: {loop} \n') 
        print("now recalculate properties")
        self.recalculate_graph_properties()
        print(f'Control graph updated and calculated properties. The graph type is {self.graph_type}, and it is {self.is_cyclic} that the graph is cyclic \nPrinting edges and nodes \n')

    def add_new_default_graph(self):
        self.control_graph = nx.DiGraph()

    def recalculate_graph_properties(self):
        self.graph_type = self.get_graph_type()
        if self.dao.hierarchical_inheritance == 1:
            self.control_graph =  nx.transitive_closure(self.control_graph)

    def get_graph_type(self):
        if nx.is_directed_acyclic_graph(self.control_graph):
            if self.is_list():
                print("the graph is a list and doesn't contain cycles")
                return graph_type.GraphType.LIST #the graph is a list and doesn't contain cycles
            else:
                return graph_type.GraphType.DAG #the graph is a DAG, but not a list
        else:
            self.is_cyclic = True
            return graph_type.GraphType.GRAPH #the graph contains cycles

    def is_list(self):
        return all(self.control_graph.out_degree(n) <= 1 for n in self.control_graph.nodes)
