def countPairs(numbers, k):
    # Write your code here
    if k == 0:
        num_set = set()
        dup_set = set()
        for i in numbers:
            if i in num_set:
                dup_set.add(i)
            num_set.add(i)
        return len(dup_set)
    else:
        cnt = 0
        numbers = set(numbers)
        for i in numbers:
            if i - k in numbers:
                cnt += 1
        return cnt


if __name__ == '__main__':
    print(countPairs([1, 1, 1, 2], 1))
