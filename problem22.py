def make_parentheses(n):
    # def make(s, left, right):
    #     if left < n:
    #         make(s + '(', left + 1, right)
    #     if left > right:
    #         make(s + ')', left, right + 1)
    #     if left == n and right == n:
    #         par.append(s)
    #
    # par = []
    # make('', 0, 0)
    # return par

    # DP solution
    dp = [[] for i in range(n + 1)]
    dp[0].append('')
    for i in range(n + 1):
        for j in range(i):
            dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
    return dp[n]


print(make_parentheses(3))
