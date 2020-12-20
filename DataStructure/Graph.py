from typing import List
from . import Vertex, Edge


class Graph(object):
    def __init__(self, type = "undirected") -> None:
        self.type = type
        self.vertices = []

    def add_vertices(self, vertices: List) -> None:
        self.vertices += vertices

    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices += [vertex]

    def add_edge(self, edge: Edge) -> None:
        edge.start.add_edge(edge)
        if type == "undirected":
            edge.end.add_edge(edge.start)

    def reverse_edge(self):
        if self.type == "undirected":
            return self
        for x in self.vertices:
            for e in x.edges:
                if e.start == x:
                    e.end.add_edge(e)
        for x in self.vertices:
            x.edges = [Edge(et.end, et.start) for et in filter(lambda e: e.start != x, x.edges)]
