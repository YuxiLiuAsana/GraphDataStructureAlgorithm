from ..DataStructure import Graph
from .DFS import dfs_visited
from functools import reduce
def strongly_connect_direct_graph(g: Graph) -> bool:
    forward_visited = dfs_visited(g)
    g.reverse_edge()
    backward_visited = dfs_visited(g)
    return reduce(lambda a, b: a and b, forward_visited + backward_visited)
