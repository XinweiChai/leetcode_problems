class Solution:
    # def lengthLongestPath(self, input: str) -> int:
    #     max_path = 0
    #     prefix = [0]
    #     paths = input.split('\n')
    #     cur_tabs = 0
    #     for i in paths:
    #         tabs = i.count('\t')
    #         if '.' in i:
    #             max_path = max(max_path, prefix[-1] + len(i) - tabs)
    #             continue
    #         if tabs == cur_tabs + 1:
    #             prefix.append(prefix[-1] + len(i) - tabs + 1)
    #         else:
    #             prefix = prefix[:tabs + 2]
    #         cur_tabs = tabs
    #     return max_path

    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1
        return maxlen


if __name__ == '__main__':
    print(Solution().lengthLongestPath(input="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
