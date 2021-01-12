from ..DataStructure import Graph, Edge, Vertex
from typing import List

def bridge(g: Graph) -> List[Edge]:
    disc = [None] * len(g.vertices)
    parent = [None] * len(g.vertices)
    low = [len(g.vertices)] * len(g.vertices)
    id_map = {id(v):i for i, v in enumerate(g.vertices)}
    ret_edge = []
    def helper(v: Vertex, time: int) -> None:
        nonlocal disc, low, ret_edge, id_map
        disc[id_map[id(v)]] = time
        for e in v.edges:
            end_v = e.end
            if disc[id_map[id(end_v)]] == None:
                parent[id_map[id(end_v)]] = v
                helper(end_v, time + 1)
                low[id_map[id(v)]] = min(low[id_map[id(v)]], low[id_map[id(end_v)]])
                if low[id_map[id(end_v)]] > disc[id_map[id(v)]]:
                    ret_edge += [e]
            elif end_v != parent[id_map[id(v)]]:
                low[id_map[id(v)]] = min(low[id_map[id(v)]], disc[id_map[id(end_v)]])
    helper(g.vertices[0],0)
    return ret_edge
