import sys


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def __init__(self):
        return

    @staticmethod
    # @param A: Given an integer array with no duplicates.
    # @return: The root of max tree.
    def max_tree(a):
        # write your code here
        # when A is empty, return a empty node; that is, return None.
        if not a:
            return None
        else:
            # always have the reference of current max node
            # if the next integer is greater than current max
            # then everything before the next integer
            # should've been constructed
            # if smaller (no duplicates, can't be equal), compare to the next
            # one in the storage (comparison goes backward)
            # when "greater" is found, shrink everything after the one
            # (including itself), add to the left of the next integer
            # put the next integer into the storage
            # an array as storage is enough, as stack
            # worst case: descending sequence?
            # need dummy node: root can change
            # O(n) proof: each peek comes with an insert or shrink,
            # but total times of insert and shrink are linear.
            nodes = []  # stack to store top nodes
            for i in a + [sys.maxint]:
                tmp = None
                new_node = TreeNode(i)
                while nodes:
                    if i < nodes[-1].val:
                        break
                    else:
                        tmp2 = nodes.pop()
                        tmp2.right = tmp
                        tmp = tmp2
                new_node.left = tmp
                nodes += [new_node]
            return nodes[0].left
