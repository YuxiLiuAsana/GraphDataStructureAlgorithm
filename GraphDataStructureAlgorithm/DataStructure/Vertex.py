from . import Edge
from . import Vertex


class Vertex(object):
    def __init__(self, value) -> None:
        self.value = value
        self.edges = []

    def add_edge(self, edge: Edge) -> None:
        self.edges += [edge]

    def add_edge(self, end: Vertex) -> None:
        self.edges += [Edge(self, end)]