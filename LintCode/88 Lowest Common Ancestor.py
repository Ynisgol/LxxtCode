import copy
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def __init__(self):
        return

    """
    @param root: The root of the binary search tree.
    @param A and B: two nodes in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    @staticmethod
    def lowest_common_ancestor(root, a, b):
        # write your code here
        # use a stack to search for the two nodes
        # take a snapshot when found
        # compare the two stacks
        # assume root is not None and A, B exist in the tree
        stack = deque()
        stack.append(root)
        # pre-order traversal
        # for stack,
        # if coming from the parent, check self first, then go to the left
        # if coming from the left, add right to stack
        # if coming from the right, pop and do nothing
        prev = None
        snapshot_a, snapshot_b = None, None
        while stack:
            curr = stack[-1]
            if prev is None or prev.left == curr or prev.right == curr:
                if curr == a:
                    snapshot_a = copy.copy(stack)
                if curr == b:
                    snapshot_b = copy.copy(stack)
                if snapshot_a and snapshot_b:
                    break
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
                else:
                    stack.pop()
            elif prev == curr.left:
                if curr.right:
                    stack.append(curr.right)
                else:
                    stack.pop()
            else:
                stack.pop()
            prev = curr

        # process the snapshots
        common = None
        for i, j in zip(snapshot_a, snapshot_b):
            if i == j:
                common = i
            else:
                break
        return common


na = TreeNode('a')
nb = TreeNode('b')
nc = TreeNode('c')
nd = TreeNode('d')
ne = TreeNode('e')
nc.left = ne
na.left = nb
na.right = nc
nc.right = nd
print Solution.lowest_common_ancestor(na, ne, nd).val
