def make_parentheses(n):
    def make(s, left, right):
        if left < n:
            make(s + '(', left + 1, right)
        if left > right:
            make(s + ')', left, right + 1)
        if left == n and right == n:
            par.append(s)

    par = []
    make('', 0, 0)
    return par


print(make_parentheses(3))
