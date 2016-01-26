class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        # calculate prefix sum array: p[i] = sum(nums[0 to i - 1]), i = 1, 2, ..., n; p[0] = 0
        # range sum s(i, j) = p[j + 1] - p[i], 0 <= i <= j < n
        # find all i, j pair so that lower <= p[j +1] - p[i] <= upper
        # p[i] + lower <= p[j + 1] <= p[i] + upper
        # for any i, 0 <= i < n, find all j, i < j < n, so that p[i] + lower <= p[j] <= p[i] + upper
        # put p[i] into BST backwards, before putting a new one, search the tree for qualified i, j pairs
        if not nums or lower > upper:
            return 0

        ps = prefixSum(nums)
        bst = BST(Node(ps[-1]))
        ret = 0
        for i in reversed(ps[:-1]):
            ret += bst.searchRange(i + lower, i + upper)
            bst.insert(Node(i))
        return ret


def prefixSum(nums):
    ret = [0]
    s = 0
    for i in nums:
        s += i
        ret.append(s)
    return ret


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        curr = self.root
        while True:
            if node.val < curr.val:
                curr.numleft += 1
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = node
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = node
                    break

    def searchRange(self, lower, upper):
        return self.searchUpper(upper) - self.searchLower(lower)

    def searchLower(self, val):
        ret = 0
        curr = self.root
        while curr:
            if val <= curr.val:
                curr = curr.left
            else:
                ret += curr.numleft
                curr = curr.right
        return ret

    def searchUpper(self, val):
        ret = 0
        curr = self.root
        while curr:
            if val < curr.val:
                curr = curr.left
            else:
                ret += curr.numleft
                curr = curr.right
        return ret


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.numleft = 1


print Solution().countRangeSum([1, 2, -1, -2], -2, 2)
