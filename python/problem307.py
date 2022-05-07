from typing import Sequence


# Using Segment Tree
class NumArray:

    def __init__(self, nums: Sequence[int]):
        self.n = len(nums)
        self.tree = [0] * (self.n << 1)
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[(i << 1) + 1]

    def update(self, index: int, val: int) -> None:
        cur = index + self.n
        diff = val - self.tree[cur]
        while cur:
            self.tree[cur] += diff
            cur >>= 1

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        tot = 0
        while left <= right:
            if left & 1:
                tot += self.tree[left]
                left += 1
            if not right & 1:
                tot += self.tree[right]
                right -= 1
            left >>= 1
            right >>= 1
        return tot

    def sumRange2(self, left: int, right: int) -> int:
        def helper(l, r):
            if l > r:
                return 0
            if l == r:
                return self.tree[l]
            return (l & 1) * self.tree[l] + helper((l + 1) >> 1, (r - 1) >> 1) + (r & 1 == 0) * self.tree[r]

        return helper(left + self.n, right + self.n)


# Using Fenwick Tree (Binary Indexed Tree)
class NumArray2:
    def __init__(self, nums: Sequence[int]):
        self.nums = nums
        self.N = len(self.nums)
        self.tree = [0] * (self.N + 1)
        # optimize initiate BIT in O(n)
        for j in range(1, self.N + 1):
            self.tree[j] += self.nums[j - 1]
            if (j + (j & (-j))) <= self.N:
                self.tree[j + (j & (-j))] += self.tree[j]

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index <= self.N:
            self.tree[index] += diff
            index += (index & (-index))

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right) - self.getSum(left - 1)

    def getSum(self, i):
        sm = 0
        i += 1
        while i > 0:
            sm += self.tree[i]
            i -= (i & (-i))
        return sm


if __name__ == '__main__':
    # Your NumArray object will be instantiated and called as such:
    # obj = NumArray(nums)
    # obj.update(index,val)
    # param_2 = obj.sumRange(left,right)
    obj = NumArray2(list(range(1, 16)))
    obj.update(0, 5)
    print(obj.sumRange(0, 3))
