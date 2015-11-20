import heapq


class Solution:
    def __init__(self):
        return

    # @param buildings: A list of lists of integers
    # @return: A list of lists of integers
    def building_outline(self, buildings):
        heights = []
        for building in buildings:
            # need to negate building[2] since heapq only supports min heap
            heights += [(building[0], - building[2],  1), (building[1], - building[2], -1)]
        heights = sorted(heights, cmp=lambda x, y: x[0] - y[0] if x[0] != y[0] else y[2] - x[2])
        outlines = []
        h = []
        prev = 0
        for height in heights:
            if height[2] == 1:
                if not h:
                    prev = height[0]
                elif h and h[0] > height[1]:
                    if prev != height[0]:
                        outlines += [[prev, height[0], - h[0]]]
                    prev = height[0]
                heapq.heappush(h, height[1])
            else:  # height[2] == -1
                old_top = h[0]
                i = self.find(h, height[1], 0)
                h[i] = h[-1]
                h.pop()
                heapq.heapify(h)
                if not h or h[0] != old_top:
                    if prev != height[0]:
                        outlines += [[prev, height[0], - old_top]]
                    prev = height[0]
        return outlines

    def find(self, h, value, i):
        if i >= len(h):
            return -1
        if h[i] == value:
            return i
        elif h[i] > value:
            return -1
        else:
            left = self.find(h, value, 2 * i + 1)
            if left != -1:
                return left
            right = self.find(h, value, 2 * i + 2)
            return right


print Solution().building_outline([
    [1, 5, 1],
    [2, 7, 2],
    [4, 5, 1],
    [4, 6, 3]
])
