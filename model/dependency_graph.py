
import networkx as nx

class DependencyGraph:
    
    def __init__(self) -> None:
        self.dao_control_graph = nx.DiGraph()
        self.roots = {}
