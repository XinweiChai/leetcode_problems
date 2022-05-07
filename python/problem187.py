from typing import Sequence


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> Sequence[str]:
        seen = set()
        dup = set()
        for i in range(len(s) - 9):
            if s[i:i + 10] in seen:
                dup.add(s[i:i + 10])
            else:
                seen.add(s[i:i + 10])
        return list(dup)


if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences(s="AAAAAAAAAAA"))
