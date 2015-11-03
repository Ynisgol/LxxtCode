from collections import deque


class Solution:
    def __init__(self):
        return

    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    @staticmethod
    def max_sliding_window(nums, k):
        # write your code here
        # we can try a max deque that stores index
        # and a deque that stores the window (no need to store window)
        # 1. when the window deque is not full
        #   put one into the window deque
        #   do
        #   (peek tail of max deque, if greater than the tail, pop then add)
        #   until smaller than tail or deque empty
        #   <deque head always stores current max>
        # 2. when the window deque is full
        #   do all the above, also the following
        #   remove head, add tail
        #   if the head index == the head of max deque (can't be >),
        #       remove head of max deque
        #   if <,
        #       do nothing to max deque
        # in each iteration, return the head of max deque
        # until no more num to add to window deque
        # Time Complexity:
        # each num: add to window deque once, add to max deque once, pop once
        #           peek once, remove once = O(n)
        # max size of both deque = k
        # ---------------------------------------------------------------------
        if not nums or k == 0:
            return []
        else:  # nums contains at least 1 number and k > 0
            swm = []
            max_dq = deque()
            for i in range(len(nums)):
                while max_dq and nums[i] > nums[max_dq[-1]]:
                    max_dq.pop()
                max_dq.append(i)
                if i >= k:
                    if i - k == max_dq[0]:
                        max_dq.popleft()
                if i >= k - 1:
                    swm += [nums[max_dq[0]]]
            return swm

print Solution().max_sliding_window([1, 2, 7, 7, 2, 10, 3, 4, 5], 2)
# So, this is super hard difficulty?
