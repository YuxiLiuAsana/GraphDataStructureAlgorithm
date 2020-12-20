from ..DataStructure import Graph, Vertex
from typing import List
def dijkstras(g: Graph, start_index: int) -> List[float]:
    dist = [float('inf')] * len()
