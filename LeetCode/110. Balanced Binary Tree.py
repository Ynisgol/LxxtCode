# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def is_balanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_balanced_helper(root) != -1

    def is_balanced_helper(self, root):
        """
        :type root: tree root node
        :rtype: returns -1 is the tree is not balanced or returns the height of the tree if it is balanced
        define: single node is considered of height 1, None is considered of height 0 (special handling)
        """
        if not root:
            return 0
        left = self.is_balanced_helper(root.left)
        right = self.is_balanced_helper(root.right)
        if left == -1 or right == -1 or not -1 <= left - right <= 1:
            return -1
        return max(left, right) + 1
