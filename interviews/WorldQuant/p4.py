def minimumOperations(numbers):
    # Write your code here
    # n = len(numbers)
    # total_moves = 0
    # for i in range(len(numbers)):
    #     cnt_left = 0
    #     cnt_right = 0
    #     for j in range(i):
    #         if numbers[i] > numbers[j]:
    #             cnt_left += 1
    #         elif numbers[i] < numbers[j]:
    #             cnt_right += 1
    #     total_moves += min(cnt_left, cnt_right)
    # return n + 2 * total_moves
    def getCount(arr, num):
        if len(arr) == 0 or len(arr) == 1 or max(arr) == num:
            return 1
        else:
            left = 0
            right = 0
            for i in range(len(arr)):
                if num < arr[i]:
                    left = left + 1
                elif num > arr[i]:
                    right = right + 1
            return right * 2 + 1 if right <= left else left * 2 + 1

    arr = []
    tot = 0
    for i in range(len(numbers)):
        tot = tot + getCount(arr, numbers[i])
        arr.append(numbers[i])
    return tot

if __name__ == '__main__':
    print(minimumOperations([10, 6, 2, 3, 7, 1, 2]))
