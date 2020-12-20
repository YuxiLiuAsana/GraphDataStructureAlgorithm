from . import TreeNode


class TreeNode(object):
    def __init__(self, val) -> None:
        self.val = val
        self.children = []

    def add_child(self, child: TreeNode) -> None:
        self.children += [child]