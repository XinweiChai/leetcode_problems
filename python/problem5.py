class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Expand around center, O(n^2)
        # longest = ''
        #
        # def decide_one(s, left_pointer, right_pointer):
        #     temp = ''
        #     while left_pointer >= 0 and right_pointer <= len(s) - 1 and s[left_pointer] == s[right_pointer]:
        #         temp = s[left_pointer:right_pointer + 1]
        #         left_pointer -= 1
        #         right_pointer += 1
        #     return temp
        #
        # for i in range(len(s)):
        #     temp = decide_one(s, i, i)
        #     if len(longest) < len(temp):
        #         longest = temp
        #     temp = decide_one(s, i, i + 1)
        #     if len(longest) < len(temp):
        #         longest = temp
        # return longest

        # Manacher's Algorithm O(n)

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


print(Solution().longestPalindrome("a"))
