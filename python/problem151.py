import re


class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.split(r'\s+', s.strip())
        s.reverse()
        return ' '.join(s)
