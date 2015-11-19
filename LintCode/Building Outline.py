import heapq

class Solution:
    def __init__(self):
        return

    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    @staticmethod
    def building_outline(buildings):
        # write your code here
        heights = []
        for building in buildings:
            heights += [(building[0], - building[2],  1), (building[1], - building[2], -1)]
        heights = sorted(heights, cmp=lambda x, y: x[0] - y[0] if x[0] != y[0] else y[2] - x[2])
