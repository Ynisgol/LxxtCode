import heapq


class Solution(object):
    def get_skyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        heights = []
        for building in buildings:
            # need to negate building[2] since heapq only supports min heap
            # (height, direction, x, counter-x)
            heights += [(- building[2], 1, building[0], building[1]), (- building[2], -1, building[1], building[0])]
        heights = sorted(heights, cmp=lambda x, y: x[2] - y[2] if x[2] != y[2] else y[1] - x[1])
        outlines = []
        h = []
        prev = -1
        for height in heights:
            if height[1] == 1:
                if not h:
                    if prev != -1:
                        outlines += [[prev, 0]]
                    prev = height[2]
                elif h and h[0][0] > height[0]:
                    if prev != height[2]:
                        outlines += [[prev, - h[0][0]]]
                    prev = height[2]
                elif h[0][3] >= height[3]:  # also h[0][0] <= height[0]
                    continue
                heapq.heappush(h, height)
            else:  # height[2] == -1
                i = self.find(h, height, 0)
                if i != -1:
                    old_top = h[0][0]
                    h[i] = h[-1]
                    h.pop()
                    heapq.heapify(h)
                    if not h or h[0][0] != old_top:
                        if prev != height[2]:
                            outlines += [[prev, - old_top]]
                        prev = height[2]
        if prev != -1:
            outlines += [[prev, 0]]
        return outlines

    def find(self, h, value, i):
        if i >= len(h):
            return -1
        if self.is_counter(h[i], value):
            return i
        elif h[i][0] > value[0]:
            return -1
        else:
            left = self.find(h, value, 2 * i + 1)
            if left != -1:
                return left
            right = self.find(h, value, 2 * i + 2)
            return right

    @staticmethod
    def is_counter(up, down):
        return up[0] == down[0] and up[1] + down[1] == 0 and up[2] == down[3] and up[3] == down[2]
