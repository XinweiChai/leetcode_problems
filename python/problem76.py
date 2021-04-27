from collections import Counter


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype -> str
        """

        # if not t or not s:
        #     return ""
        #
        # # Dictionary which keeps a count of all the unique characters in t.
        # dict_t = Counter(t)
        #
        # # Number of unique characters in t, which need to be present in the desired window.
        # required = len(dict_t)
        #
        # # left and right pointer
        # l, r = 0, 0
        #
        # # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        # formed = 0
        #
        # # Dictionary which keeps a count of all the unique characters in the current window.
        # window_counts = {}
        #
        # # ans tuple of the form (window length, left, right)
        # ans = float("inf"), None, None
        #
        # while r < len(s):
        #
        #     # Add one character from the right to the window
        #     character = s[r]
        #     window_counts[character] = window_counts.get(character, 0) + 1
        #
        #     # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        #     if character in dict_t and window_counts[character] == dict_t[character]:
        #         formed += 1
        #
        #     # Try and contract the window till the point where it ceases to be 'desirable'.
        #     while l <= r and formed == required:
        #         character = s[l]
        #
        #         # Save the smallest window until now.
        #         if r - l + 1 < ans[0]:
        #             ans = (r - l + 1, l, r)
        #
        #         # The character at the position pointed by the `left` pointer is no longer a part of the window.
        #         window_counts[character] -= 1
        #         if character in dict_t and window_counts[character] < dict_t[character]:
        #             formed -= 1
        #
        #         # Move the left pointer ahead, this would help to look for a new window.
        #         l += 1
        #
        #         # Keep expanding the window once we are done contracting.
        #     r += 1
        # return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

        if not s or not t:
            return ""
        c_s = Counter()
        c_t = Counter(t)
        left = 0
        right = 0
        res = ""
        min_len = float('inf')
        formed = 0
        required = len(c_t)
        while right < len(s):
            c_s[s[right]] += 1
            if c_s[s[right]] == c_t[s[right]]:
                formed += 1
            while formed == required:
                if c_s[s[left]] == c_t[s[left]]:
                    if right - left < min_len:
                        min_len = right - left
                        res = s[left:right + 1]
                    formed -= 1
                c_s[s[left]] -= 1
                left += 1
            right += 1
        return res


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
