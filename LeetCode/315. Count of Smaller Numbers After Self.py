class Solution(object):
    def count_smaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        counts[i] is the number of smaller elements to the right of nums[i]
        """
        # build a BST from i = n - 1 to 0
        # each node stores the number of nodes in its left subtree + 1 (itself)
        # when add a node:
        # if go left, node.count += 1, return value don't add
        # if go right, node.count don't add, return value += node.count
        # when it reaches a leaf, return return value
        # new node always has node.count == 1
        counts = []
        if nums:
            nums.reverse()
            root = None
            for num in nums:
                if not root:
                    root = Node(nums[0], 1)
                    counts.append(0)
                else:
                    counts.append(self.insert(root, num))
            counts.reverse()
        return counts

    def insert(self, root, num):
        ret = 0  # ret is the number of numbers smaller than num
        if root.val < num:
            ret += root.count
            if root.right:
                ret += self.insert(root.right, num)
            else:
                root.right = Node(num, 1)
        elif root.val > num:
            root.count += 1
            if root.left:
                ret += self.insert(root.left, num)
            else:
                root.left = Node(num, 1)
        else:
            ret += root.count - 1
            if root.right:
                ret += self.insert(root.right, num)
            else:
                root.right = Node(num, 1)
        return ret


class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count
        self.left = None
        self.right = None
