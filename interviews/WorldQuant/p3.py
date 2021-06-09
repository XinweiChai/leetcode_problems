import bisect


def taxiDriver(pickup, drop, tip):
    # Write your code here
    n = len(pickup)
    profit = [drop[i] - pickup[i] + tip[i] for i in range(n)]
    travels = sorted(zip(pickup, drop, profit), key=lambda x: x[1])
    dp = [[0, 0]]
    for s, e, p in travels:
        i = bisect.bisect(dp, [s + 1]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    return dp[-1][1]


if __name__ == '__main__':
    print(taxiDriver([0, 2, 9, 10, 11, 12], [5, 9, 11, 11, 14, 17], [1, 2, 3, 2, 2, 1]))
