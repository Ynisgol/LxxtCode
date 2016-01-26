import bisect


class FenwickTree:
    def __init__(self, val):
        self.maxVal = val
        self.arrays = [0] * (val + 1)

    def insert(self, x):
        while x <= self.maxVal:
            self.arrays[x] += 1
            x += x & - x

    def sum(self, x):
        ret = 0
        while x > 0:
            ret += self.arrays[x]
            x -= x & - x
        return ret


class Solution:
    def __init__(self):
        return

    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums or lower > upper:
            return 0
        # prefix sum array
        sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        # sort and remove dup
        osums = sorted(set(sums))
        # calculate prefix sum array: p[i] = sum(nums[0 to i - 1]), i = 1, 2, ..., n; p[0] = 0
        # range sum s(i, j) = p[j + 1] - p[i], 0 <= i <= j < n
        # find all i, j pair so that lower <= p[j +1] - p[i] <= upper
        # p[i] + lower <= p[j + 1] <= p[i] + upper
        # for any j, 0 < j <= n, find all i, 0 <= i < j, so that p[j] - upper <= p[i] <= p[j] - lower
        # put p[i] into BST backwards, before putting a new one, search the tree for qualified i, j pairs
        ret = 0
        ft = FenwickTree(len(osums))
        ft.insert(bisect.bisect_left(osums, 0) + 1)
        for s in sums[1:]:
            left = bisect.bisect_left(osums, s - upper)
            right = bisect.bisect_right(osums, s - lower)
            ret += ft.sum(right) - ft.sum(left)
            ft.insert(bisect.bisect_left(osums, s) + 1)
        return ret


print Solution().countRangeSum([1, 2, -1, -2], -2, 2)
