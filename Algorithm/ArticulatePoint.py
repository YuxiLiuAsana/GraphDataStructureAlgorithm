from ..DataStructure import Graph, Vertex
from .DFS import dfs_tree
from typing import List


def articulate_point(g: Graph) -> List[Vertex]:
    tree = dfs_tree(g)
    if tree is None:
        return []
