
import networkx as nx
from enum import Enum
from DAOclasses import DAO

class GraphType(Enum):
    LIST = 0
    FOREST = 1
    GRAPH = 2

class ControlGraph:
    def __init__(self, dao: DAO):
        self.dao = dao
        self.control_graph: nx.DiGraph = None
        self.graph_type: GraphType = None
        self.is_cyclic = False #hypotesis

    def add_new_default_graph(self):
        self.control_graph = nx.DiGraph()

    def recalculate_graph_properties(self):
        simple_cycles = nx.simple_cycles(self.graph_type)
        self.is_cyclic = simple_cycles != None and len(simple_cycles) > 0
        # TODO : verificare se fosse una foresta, una lista, od altro (grafo)
