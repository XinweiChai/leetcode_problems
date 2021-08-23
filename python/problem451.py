class Solution:
    def frequencySort(self, s: str) -> str:
        chars = set(s)
        chars = [(c, s.count(c)) for c in chars]
        chars.sort(key=lambda t: -t[1])
        return ''.join(char * count for char, count in chars)


if __name__ == '__main__':
    print(Solution().frequencySort(s="tree"))
