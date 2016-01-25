# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    @staticmethod
    def inorder_successor(root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        else:
            stack = deque()
            stack.append(root)
            prev = None
            next_flag = False
            while stack:
                curr = stack[-1]
                if prev is None or prev.left == curr or prev.right == curr:
                    if curr.left:
                        stack.append(curr.left)
                else:
                    stack.pop()
                    if next_flag:
                        return curr
                    if curr == p:
                        next_flag = True
                    if curr.right:
                        stack.append(curr.right)
                prev = curr
            return None
