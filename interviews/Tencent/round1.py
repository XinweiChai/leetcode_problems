def find_mode(lst):
    first = None
    second = None
    freq_first = 0
    freq_second = 0
    n = len(lst)
    for i in lst:
        if i == first:
            freq_first += 1
        elif i == second:
            freq_second += 1
        elif freq_first == 0:
            first = i
            freq_first = 1
        elif freq_second == 0:
            second = i
            freq_second = 1
        else:
            freq_first -= 1
            freq_second -= 1
    res = []
    if lst.count(first) > n // 3:
        res.append(first)
    if lst.count(second) > n // 3:
        res.append(second)
    return res


def biggest_square(dp):
    r = len(dp)
    c = len(dp[0])
    for i in range(r):
        for j in range(c):
            dp[i][j] = int(dp[i][j])
    max_area = 0

    for i in range(1, r):
        for j in range(1, c):
            if dp[i][j] == 1:
                dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
            max_area = max(dp[i][j], max_area)
    return max_area ** 2


if __name__ == '__main__':
    # print(find_mode([1, 1, 1, 3, 3, 2, 2, 2]))
    # print(find_mode([3,2,3]))
    print(biggest_square([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                          ["1", "0", "0", "1", "0"]]))
