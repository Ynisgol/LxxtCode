class Solution(object):
    def word_break(self, s, word_dict):
        """
        :type s: str
        :type word_dict: Set[str]
        :rtype: List[str]
        """
        # use a helper function: return all the solutions for s[index:] (0 <= index < len(s)).
        # when index == 0 is what we want.
        # when index == len(s) should return []
        # use a hashtable to store those return values: (index, return value)
        # helper function calls itself when a match is found
        # use max length of word in dict to optimize
        if not word_dict:  # empty word_dict
            return []
        else:
            max_word_len = max(len(word) for word in word_dict)
            if not max_word_len:
                return []
            else:  # max_word_len > 0
                return self.word_break_helper(s, word_dict, 0, max_word_len, {})

    def word_break_helper(self, s, word_dict, index, max_word_len, solutions):
        if index == len(s):  # because if len(s) == 0, we want it to return []
            return []
        elif index not in solutions:
            total_solution = []
            for i in range(index + 1, 1 + min(index + max_word_len, len(s))):
                if s[index:i] in word_dict:
                    tmp = self.word_break_helper(s, word_dict, i, max_word_len, solutions)
                    if not tmp:
                        if i == len(s):
                            solution = [s[index:i]]
                        else:
                            solution = []
                    else:
                        solution = [s[index:i] + ' ' + sentence for sentence in tmp]
                    total_solution += solution
            solutions[index] = total_solution
        return solutions[index]


print Solution().word_break("abc", ['a', 'b', 'c'])
