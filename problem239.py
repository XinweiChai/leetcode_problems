import collections


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        r = []
        q = collections.deque()
        for i in range(n):
            while q and q[0] < i - k + 1:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                r.append(nums[q[0]])
        return r


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
# print(Solution().maxSlidingWindow([1, -1], 1))
