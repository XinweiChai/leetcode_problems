from typing import List


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
    def reversePairs(self, nums: List[int]) -> int:
        tree = BST_Node(nums[0])
        cnt = 0
        for i in range(1, len(nums)):
            cnt += tree.find(nums[i] * 2)
            tree.insert(nums[i])
        return cnt

    # Merge sort
    def reversePairs2(self, nums: List[int]) -> int:
        def sort(arr):
            half = len(arr) // 2
            cnt = cnt1 = cnt2 = 0
            if half:
                left, cnt1 = sort(arr[:half])
                right, cnt2 = sort(arr[half:])
                for i in range(len(arr) - 1, -1, -1):
                    if not right or (left and left[-1][1] > right[-1][1]):
                        if right and left[-1][1] > 2 * right[-1][1]:
                            cnt += len(right)
                        arr[i] = left.pop()
                    else:
                        arr[i] = right.pop()
            return arr, cnt + cnt1 + cnt2

        _, cnt = sort(list(enumerate(nums)))
        return cnt

if __name__ == '__main__':
    print(Solution().reversePairs2(nums=[1, 3, 2, 3, 1]))
    print(Solution().reversePairs2(nums=[2, 4, 3, 5, 1]))
