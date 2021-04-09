from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []

        def rec(s, cur, cnt):
            if not s:
                if not cnt:
                    res.append('.'.join(cur))
            else:
                if s[0] == '0':
                    rec(s[1:], cur + ['0'], cnt - 1)
                else:
                    rec(s[1:], cur + [s[:1]], cnt - 1)
                    if len(s) >= 2:
                        rec(s[2:], cur + [s[:2]], cnt - 1)
                    if len(s) >= 3 and int(s[:3]) <= 255:
                        rec(s[3:], cur + [s[:3]], cnt - 1)

        rec(s, [], 4)
        return res


print(Solution().restoreIpAddresses("1111"))
