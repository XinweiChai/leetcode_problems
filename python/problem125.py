class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_valid(c):
            return 'a' <= c <= 'z' or 'A' <= c <= 'Z' or '0' <= c <= '9'

        def down_case(c):
            if 'A' <= c <= 'Z':
                return chr(ord(c) - ord('A') + ord('a'))
            else:
                return c

        left = 0
        right = len(s) - 1
        while left < right:
            while left <= len(s) - 1 and not is_valid(s[left]):
                left += 1
            if left == len(s):
                return True
            while right >= 0 and not is_valid(s[right]):
                right -= 1
            if down_case(s[left]) != down_case(s[right]):
                return False
            else:
                left += 1
                right -= 1
        return True


print(Solution().isPalindrome(".,"))
