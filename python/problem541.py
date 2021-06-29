class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return ''.join(s[i * 2 * k + k - 1:None if i == 0 else i * 2 * k - 1:-1] +
                       s[i * 2 * k + k:(i + 1) * 2 * k]
                       for i in range(len(s) // (2 * k) + 1))


if __name__ == '__main__':
    print(Solution().reverseStr(s="abcdefg", k=2))
