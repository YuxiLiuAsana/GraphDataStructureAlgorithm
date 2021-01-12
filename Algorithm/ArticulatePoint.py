from ..DataStructure import Graph, Vertex
from typing import List


def articulate_point(g: Graph) -> List[Vertex]:
    low = [len(g.vertices)] * len(g.vertices)
    discover = [None] * len(g.vertices)
    ap = [False] * len(g.vertices)
    id_map = {id(v):i for i,v in enumerate(g.vertices)}
    def helper(v: Vertex, time: int) -> None:
        discover[id_map[id(v)]] = time
        children = 0
        for e in v.edges:
            if discover[id_map[id(e.end)]] == None:
                children += 1
                helper(e.end, time + 1)
                low[id_map[id(v)]] = min(low[id_map[id(v)]],low[id_map[id(e.end)]])
                if time == 0 and children > 1:
                    ap[id_map[id(v)]] = True
                if time != 0 and low[id_map[id(e.end)]] >= discover[id_map[id(v)]]:
                    ap[id_map[id(v)]] = True
            else:
                low[id_map[id(v)]] = min(low[id_map[id(v)]], discover[id_map[id(e.end)]])
    helper(g.vertices[0], 0)
    return ap
