from typing import Sequence


class Solution:
    def findRestaurant(self, list1: Sequence[str], list2: Sequence[str]) -> Sequence[str]:
        # O(n^2)
        # res = []
        # if len(list1) > len(list2):
        #     list1, list2 = list2, list1
        # for i in range(len(list1) + len(list2) - 1):
        #     if not res:
        #         for j in range(max(0, i - len(list2) + 1), min(i + 1, len(list1))):
        #             if list1[j] == list2[i - j]:
        #                 res.append(list1[j])
        # return res

        # Hashmap
        hm = {}
        for idx, i in enumerate(list1):
            hm[i] = idx
        res = []
        idx_sum = float('inf')
        for idx, i in enumerate(list2):
            if i in hm:
                if hm[i] + idx == idx_sum:
                    res.append(i)
                elif hm[i] + idx < idx_sum:
                    idx_sum = hm[i] + idx
                    res = [i]
        return res

if __name__ == '__main__':
    print(Solution().findRestaurant(["vacag", "KFC"], ["fvo", "xrljq", "jrl", "KFC"]))
