class Solution:
    # Expand around center, O(n^2)
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        def decide_one(s, left_pointer, right_pointer):
            temp = ''
            while left_pointer >= 0 and right_pointer <= len(s) - 1 and s[left_pointer] == s[right_pointer]:
                temp = s[left_pointer:right_pointer + 1]
                left_pointer -= 1
                right_pointer += 1
            return temp

        for i in range(len(s)):
            temp = decide_one(s, i, i)
            if len(longest) < len(temp):
                longest = temp
            temp = decide_one(s, i, i + 1)
            if len(longest) < len(temp):
                longest = temp
        return longest

    def longestPalindrome2(self, s: str) -> str:

        # Optimization on duplicated letters
        if len(s) <= 1:
            return s
        min_left, max_len = 0, 1
        mid = 0
        while mid < len(s):
            if len(s) - mid <= max_len // 2:
                break
            left, right = mid, mid
            while right < len(s) - 1 and s[right + 1] == s[right]:
                right += 1  # Skip duplicate characters in the middle
            mid = right + 1  # For next iter
            while right < len(s) - 1 and left > 0 and s[right + 1] == s[left - 1]:
                right += 1
                left -= 1  # Expand the selection as long it is a palindrome
            new_len = right - left + 1  # record best palindrome
            if new_len > max_len:
                min_left = left
                max_len = new_len
        return s[min_left:min_left + max_len]

    # Manacher algorithm
    def longestPalindrome3(self, s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


print(Solution().longestPalindrome("a"))
