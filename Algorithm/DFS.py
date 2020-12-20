from ..DataStructure import Graph, Vertex, TreeNode
from typing import List, Optional


def dfs_visited(g: Graph) -> List[bool]:
    vertices = g.vertices
    if len(vertices) == 0:
        return []
    visited = [False] * len(vertices)
    v_id = {id(v): i for i, v in enumerate(vertices)}
    start = vertices[0]

    def helper(v: Vertex) -> None:
        nonlocal visited, v_id
        visited[v_id[id(v)]] = True
        for e in v.edges:
            next_v = e.end
            if not visited[v_id[id(next_v)]]:
                helper(next_v)
    helper(start)
    return visited


def dfs_tree(g: Graph) -> Optional[TreeNode]:
    vertices = g.vertices
    if len(vertices) == 0:
        return None
    visited = [False] * len(vertices)
    v_id = {id(v): i for i, v in enumerate(vertices)}
    start = vertices[0]

    def helper(v: Vertex) -> TreeNode:
        nonlocal visited, v_id
        visited[v_id[id(v)]] = True
        node = TreeNode(v.value)
        for e in v.edges:
            next_v = e.end
            if not visited[v_id[id(next_v)]]:
                next_node = helper(next_v)
                node.add_child(next_node)
        return node
    return helper(start)

