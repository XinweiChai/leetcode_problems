from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = Counter(s1)
        to_reach = len(s1)
        c = Counter()
        cnt = 0
        lo = 0
        hi = 0
        while hi < len(s2):
            cur = s2[hi]
            if cur not in s1:
                lo = hi + 1
                c.clear()
                cnt = 0
            else:
                c[cur] += 1
                if c[cur] == s1[cur]:
                    cnt += 1
                    if cnt == to_reach:
                        return True
                elif c[cur] == s1[cur] + 1:
                    while s2[lo] != cur:
                        if c[s2[lo]] == s1[s2[lo]]:
                            cnt -= 1
                        c[s2[lo]] -= 1
                        lo += 1
                    c[cur] -= 1
                    lo += 1
            hi += 1
        return False

    # The use of update
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = {i: 0 for i in set(s2)}
        dict2 = {}
        dict2.update(dict1)
        dict1.update({i: s1.count(i) for i in set(s1)})
        ls1 = len(s1)
        ls2 = len(s2)

        dict2.update({i: s2[:ls1].count(i) for i in set(s2[:ls1])})

        if dict1 == dict2:
            return True
        right = ls1
        left = 0
        while right < ls2:
            dict2[s2[right]] += 1
            dict2[s2[left]] -= 1
            if dict1 == dict2:
                return True
            right += 1
            left += 1
        return False

    def checkInclusion3(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict1 = {i: 0 for i in set(s2)}
        dict2 = {}
        dict2.update(dict1)
        dict1.update({i: s1.count(i) for i in set(s1)})
        ls1 = len(s1)
        ls2 = len(s2)

        dict2.update({i: s2[:ls1].count(i) for i in set(s2[:ls1])})
        to_reach = sum(dict1[i] != dict2[i] for i in dict2)

        if to_reach == 0:
            return True
        right = ls1
        left = 0
        while right < ls2:
            dict2[s2[right]] += 1
            if dict2[s2[right]] == dict1[s2[right]]:
                to_reach -= 1
            elif dict2[s2[right]] == dict1[s2[right]] + 1:
                to_reach += 1
            dict2[s2[left]] -= 1
            if dict2[s2[left]] == dict1[s2[left]]:
                to_reach -= 1
            elif dict2[s2[left]] == dict1[s2[left]] - 1:
                to_reach += 1
            if to_reach == 0:
                return True
            right += 1
            left += 1
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion3("hello", "aooolleoooleh"))
