class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        return '-'.join(s[i:i + k] for i in range(0, len(s), k))[::-1]


if __name__ == '__main__':
    print(Solution().licenseKeyFormatting(s="2-5g-3-J", k=2))
