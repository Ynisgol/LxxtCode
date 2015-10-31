class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_len = 0

    def longest_consecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # use helper function:
        #   recursively traverse the tree
        #   carry current local max length over
        #   update global max length
        # use global variable to max length
        self.longest_consc_helper(root, 1)
        return self.max_len

    def longest_consc_helper(self, node, loc_max_len):
        if node:
            self.max_len = loc_max_len if loc_max_len > self.max_len else self.max_len
            for child in [node.left, node.right]:
                if child:
                    if child.val == node.val + 1:
                        self.longest_consc_helper(child, loc_max_len + 1)
                    else:
                        self.longest_consc_helper(child, 1)

    # It is better not to use class field max_len. If so, we will need to pass it around.
    # Do we have an even better solution?
