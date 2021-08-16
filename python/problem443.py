from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_cnt = 1
        cur_char = chars[0]
        right = 1
        left = 1
        while right < len(chars):
            if chars[right] == cur_char:
                cur_cnt += 1
                right += 1
            else:
                cur_char = chars[right]
                if cur_cnt == 1:
                    left += 1
                else:
                    chars[left:right] = list(str(cur_cnt))
                    left += len(str(cur_cnt)) + 1
                    cur_cnt = 1
                right = left
        if cur_cnt != 1:
            chars[left:right] = list(str(cur_cnt))
        return len(chars)


if __name__ == '__main__':
    print(Solution().compress(["a", "b", "b", "c", "c", "c", "a"]))
