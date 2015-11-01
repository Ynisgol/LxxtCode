class Solution(object):
    def find_strobogrammatic(self, n):
        """
        :type n: int, n > 0
        :rtype: List[str]
        """
        if n <= 0:
            return []
        # 1, 8, 0; 6, 9
        all_bits = [1, 8, 0, 6, 9]
        mid_bits = [1, 8, 0]

        # use helper and permutation template
        sol = []
        res = []
        self.find_strb_helper(n, sol, all_bits, mid_bits, res)
        return res

    def find_strb_helper(self, n, sol, all_bits, mid_bits, res):
        if len(sol) == (n + 1) / 2:  # done constructing
            res += [self.to_string(sol, n % 2 == 1)]
        else:
            bits = mid_bits if len(sol) == n / 2 else all_bits
            for e in bits:
                if sol or e or n == 1:
                    sol += [e]
                    self.find_strb_helper(n, sol, all_bits, mid_bits, res)
                    sol.pop()

    @staticmethod
    def to_string(sol, is_odd):
        new_sol = list(sol)
        ret = ""
        for e in new_sol:
            ret += str(e)
        if is_odd:
            new_sol.pop()
        while new_sol:
            tmp = new_sol.pop()
            if tmp == 6:
                tmp = 9
            elif tmp == 9:
                tmp = 6
            ret += str(tmp)
        return ret

