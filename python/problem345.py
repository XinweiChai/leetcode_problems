import re


class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = re.findall('(?i)[aeiou]', s)
        # return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
        s = list(s)
        vowels = [i for i in s if i in 'aeiouAEIOU']
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                s[i] = vowels.pop()
        return ''.join(s)


if __name__ == '__main__':
    print(Solution().reverseVowels("hello"))
