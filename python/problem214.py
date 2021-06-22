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

    def shortestPalindrome2(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

    # Using the table building part of KMP algorithm, with complexity O(n)
    def shortestPalindrome3(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = len(s_new)
        f = [0] * n_new
        for i in range(1, n_new):
            t = f[i - 1]
            while t > 0 and s_new[i] != s_new[t]:
                t = f[t - 1]
            if s_new[i] == s_new[t]:
                t += 1
            f[i] = t
        return rev[0:n - f[n_new - 1]] + s


if __name__ == '__main__':
    print(Solution().shortestPalindrome3("aacecaaa"))
