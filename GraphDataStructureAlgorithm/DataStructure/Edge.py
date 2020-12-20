from . import Vertex
class Edge(object):
    def __init__(self,start: Vertex, end: Vertex, weight: float = 1) -> None:
        self.start = start
        self.end = end
        self.weight = weight