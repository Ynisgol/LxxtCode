class Solution(object):
    @staticmethod
    def count_smaller(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        counts[i] is the number of smaller elements to the right of nums[i]
        """
        # Use Fenwick tree
        # sort nums into sequence
        # implement Fenwick tree: insert, cum_count
        if not nums:
            return []
        counts = [0] * len(nums)
        indices = {}
        for k, v in enumerate(sorted(set(nums))):
            indices[v] = k + 1
        ft = Fenwick(len(indices))
        for i in range(len(nums) - 1, - 1, - 1):
            counts[i] = ft.cum_count(indices[nums[i]] - 1)
            ft.insert(indices[nums[i]])
        return counts


class Fenwick:
    def __init__(self, max_val):
        self.maxVal = max_val
        self.array = [0] * (max_val + 1)

    def insert(self, val):
        # val must be smaller than or equal to maxVal
        # val must be great than 0
        while val <= self.maxVal:
            self.array[val] += 1
            val += val & - val

    def cum_count(self, val):
        ret = 0
        while val > 0:
            ret += self.array[val]
            val -= val & - val
        return ret
