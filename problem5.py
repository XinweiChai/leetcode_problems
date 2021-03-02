def decide_one(s, left_pointer, right_pointer):
    temp = ''
    while left_pointer >= 0 and right_pointer <= len(s) - 1 and s[left_pointer] == s[right_pointer]:
        temp = s[left_pointer:right_pointer + 1]
        left_pointer -= 1
        right_pointer += 1
    return temp


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        for i in range(len(s)):
            temp = decide_one(s, i, i)
            if len(longest) < len(temp):
                longest = temp
            temp = decide_one(s, i, i + 1)
            if len(longest) < len(temp):
                longest = temp
        return longest


print(Solution().longestPalindrome("a"))
