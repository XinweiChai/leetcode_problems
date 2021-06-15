from typing import List


def minGroup(ls: List[str]) -> int:
    def similar(s1, s2):
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        pair = None
        flag = True
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if not pair:
                    pair = (s1[i], s2[i])
                elif flag:
                    flag = False
                    if (s2[i], s1[i]) != pair:
                        return False
                else:
                    return False
        return True

    d = {}
    cnt = 0
    for i in range(len(ls)):
        if i not in d:
            cnt += 1
            d[i] = cnt
        for j in range(i + 1, len(ls)):
            if similar(ls[i], ls[j]):
                d[j] = cnt
    return cnt


if __name__ == '__main__':
    print(minGroup(ls=['abcd', 'aaaa', 'dcba', 'qwer']))
