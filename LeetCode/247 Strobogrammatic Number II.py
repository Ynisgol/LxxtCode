class Solution(object):
    def find_strobogrammatic(self, n):
        return self.find_strobogrammatic_helper(n)

    def find_strobogrammatic_helper(self, n, has_zero=False):
        """
        :type n: int, n > 0
        :type has_zero: whether to include '0' in construction
        :rtype: List[str]
        """
        if n <= 0:
            return []
        elif n == 1:
            return ['0', '1', '8']
        elif n == 2:
            if has_zero:
                return ['00', '11', '69', '88', '96']
            else:
                return ['11', '69', '88', '96']
        else:  # n >= 3
            pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
            sub = self.find_strobogrammatic_helper(n - 2, True)
            if not has_zero:
                pairs = pairs[1:]
            res = []
            for (i, j) in pairs:
                for s in sub:
                    res += [i + s + j]
            return res

print Solution().find_strobogrammatic(4)
