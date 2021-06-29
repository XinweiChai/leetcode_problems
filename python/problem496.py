from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        st = []
        ans = []

        for x in nums2:
            while len(st) and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(d.get(x, -1))
        return ans


if __name__ == '__main__':
    print(Solution().nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
