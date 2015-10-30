__author__ = 'Logsiny'


class Solution(object):
    @staticmethod
    def word_break(s, word_dict):
        """
        :type s: str
        :type word_dict: Set[str]
        :rtype: bool
        """
        # Use DP. dp[i] means if s[:i] can be successfully segmented (0 <= i <= len(s)).
        # dp[0] = True
        # dp[len(s)] is what we want.
        # a straightforward DP would be: (use maximum length of word in wordDict to optimize)
        # If for any 0<= k < i, we have dp[k] == True and s[k:i] is in dict, then dp[i] = True.
        length = len(s)
        if length == 0:
            return True
        else:
            max_len = 0
            for word in word_dict:
                max_len = len(word) if len(word) > max_len else max_len
            dp = [False] * (length + 1)
            dp[0] = True
            for i in range(1, length + 1):
                for j in range(1, max_len + 1):
                    if i - j >= 0:
                        if dp[i - j] and s[i - j:i] in word_dict:
                            dp[i] = True
                            break
            return dp[length]
