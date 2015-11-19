import sys


class Solution(object):
    @staticmethod
    def shortest_distance(words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = -1
        index2 = -1
        shortest_dist = sys.maxint
        for i in range(len(words)):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
            else:
                continue
            if index1 != -1 and index2 != -1:
                dist = abs(index2 - index1)
                shortest_dist = shortest_dist if shortest_dist < dist else dist
        return shortest_dist
