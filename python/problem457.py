from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                nums[i] %= n
            else:
                nums[i] %= -n

        def move(cur):
            cur += nums[cur]
            cur %= n
            return cur

        def sign(i):
            return 1 if i > 0 else -1

        for idx, i in enumerate(nums):
            if i == 0 or i >= n or i <= -n:
                continue
            sgn = sign(i)
            slow = idx
            # ignore self-loop
            if slow == move(slow):
                continue
            fast = idx
            while 1:
                slow = move(slow)
                last = move(fast)
                fast = move(last)
                if sign(nums[last]) != sgn or sign(nums[fast]) != sgn or nums[last] % n == 0:
                    break
                nums[last] += n * sgn
                nums[fast] += n * sgn
                if slow == fast:
                    return True
        return False

    # A more tricky way of marking
    def circularArrayLoop2(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            mark = str(i)
            while type(nums[i]) == int and (num * nums[i]) > 0 and nums[i] % len(nums) != 0:
                jump = nums[i]
                nums[i] = mark
                i = (i + jump) % len(nums)
            if nums[i] == mark:
                return True
        return False


if __name__ == '__main__':
    print(Solution().circularArrayLoop([2, -1, 1, 2, 2]))
