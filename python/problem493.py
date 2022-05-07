from typing import Sequence
from bisect import bisect


# Similar to problem315

# Need to be self-balancing
class BST_Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.cnt = 1

    def insert(self, val):
        cur = self
        while 1:
            cur.cnt += 1
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = BST_Node(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = BST_Node(val)
                    return

    def find(self, val):
        cur = self
        cnt = 0
        while 1:
            if val < cur.val:
                cnt += 1
                if cur.right:
                    cnt += cur.right.cnt
                if cur.left:
                    cur = cur.left
                else:
                    return cnt
            elif val >= cur.val:
                if cur.right:
                    cur = cur.right
                else:
                    return cnt


class Solution:
    def reversePairs(self, nums: Sequence[int]) -> int:
        tree = BST_Node(nums[0])
        cnt = 0
        for i in range(1, len(nums)):
            cnt += tree.find(nums[i] * 2)
            tree.insert(nums[i])
        return cnt

    # Merge sort
    def reversePairs2(self, nums: Sequence[int]) -> int:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums, 0
            m = len(nums) // 2
            left, countl = mergeSort(nums[:m])
            right, countr = mergeSort(nums[m:])
            count = countl + countr
            for r in right:
                diff = len(left) - bisect(left, r * 2)
                if diff <= 0:
                    break
                count += diff
            return sorted(left + right), count

        return mergeSort(nums)[1]

    # Using insert trick
    def reversePairs3(self, nums: Sequence[int]) -> int:
        left = []
        ans = 0
        for i, n in enumerate(nums):
            j = bisect(left, 2 * n)
            ans += i - j
            k = bisect(left, n)
            # insert trick
            # left[k:k] = [n]
            left.insert(k, n)
        return ans


if __name__ == '__main__':
    print(Solution().reversePairs3(nums=[1, 3, 2, 3, 1]))
    print(Solution().reversePairs3(nums=[2, 4, 3, 5, 1]))
