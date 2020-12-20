from ..DataStructure import Graph, Vertex
from typing import List
import heapq
def dijkstras(g: Graph, start_index: int) -> List[float]:
    vertices = g.vertices
    v_id = {id(v): i for i, v in enumerate(vertices)}
    dist = [float('inf')] * len(vertices)
    visited = [False] * len(vertices)
    heap = []
    heapq.heappush([0,start_index])
    while len(heap):
        d, i = heapq.heappop(heap)
        if visited[i]:
            continue
        visited[i] = True
        dist[i] = min(dist[i], d)
        v = vertices[i]
        for e in v.edges:
            end_id = v_id[id(e.end)]
            if not visited[end_id]:
                heapq.heappush(heap, [d + e.weight,end_id])
    return dist


