from ..DataStructure import Graph, Edge, Vertex
from typing import List
def bellman_ford(g: Graph, source_index: int) -> List[float]:
    ret = [float("inf")] * len(g.vertices)
    id_map = {id(v): i for i, v in enumerate(g.vertices)}
    ret[source_index] = 0
    for _ in range(len(ret)-1):
        for v in g.vertices:
            for e in v.edges:
                start_index =id_map[id(e.begin)]
                end_index = id_map[id(e.end)]
                ret[end_index] = min(ret[end_index], ret[start_index] + e.weight)
    for v in g.vertices:
        for e in v.edges:
            start_index = id_map[id(e.begin)]
            end_index = id_map[id(e.end)]
            if ret[end_index] > ret[start_index] + e.weight:
                return []
    return ret