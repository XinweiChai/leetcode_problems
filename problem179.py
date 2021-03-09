from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        key = cmp_to_key(lambda x, y: int(y + x) - int(x + y))
        res = ''.join(sorted(map(str, nums), key=key)).lstrip('0')
        return res or '0'


print(Solution().largestNumber([3, 30, 34, 5, 9]))
