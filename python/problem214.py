class Solution:
    # O(n^2) time out
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def is_palindrome(begin, end):
            while begin < end:
                if s[begin] != s[end]:
                    return False
                begin += 1
                end -= 1
            return True

        for i in range(len(s) - 1, -1, -1):
            if is_palindrome(0, i):
                return s[:i:-1] + s


if __name__ == '__main__':
    print(Solution().shortestPalindrome('a'))
