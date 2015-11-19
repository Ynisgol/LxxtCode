from collections import defaultdict


class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.words_dict = defaultdict(list)
        for i in range(len(words) - 1, -1, -1):
            self.words_dict[words[i]] += [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1 = list(self.words_dict[word1])
        index2 = list(self.words_dict[word2])
        shortest_dist = abs(index1[-1] - index2[-1])
        while index1 and index2:
            if index1[-1] < index2[-1]:
                dist = index2[-1] - index1[-1]
                index1.pop()
            else:
                dist = index1[-1] - index2[-1]
                index2.pop()
            shortest_dist = shortest_dist if shortest_dist < dist else dist
        return shortest_dist


# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
