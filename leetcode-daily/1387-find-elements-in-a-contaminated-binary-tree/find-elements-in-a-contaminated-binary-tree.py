# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.head = root

    def find(self, target: int) -> bool:
        root = self.head
        path = []
        while target:
            # check if odd
            if target & 1:
                path.append(0)
                target = (target - 1) // 2
            else:
                path.append(1)
                target = (target - 2) // 2
        # traverse path in reverse, as it is formed from the bottom
        # and now we are traversing from the top
        for dir in range(len(path) -1, -1, -1):
            if path[dir] == 0 and root.left:
                root = root.left
            elif path[dir] == 1 and root.right:
                root = root.right
            else:
                return False
        return True