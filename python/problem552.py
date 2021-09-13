num = 1000000007


class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 1:
            return 3
        end_l = [0] * n
        end_p = [0] * n
        end_l[0], end_l[1] = 1, 2
        end_p[0], end_p[1] = 1, 2
        for i in range(2, n):
            end_l[i] = (end_p[i - 1] + end_p[i - 2]) % num
            end_p[i] = (end_p[i - 1] + end_l[i - 1]) % num
        tot = end_l[-1] + end_p[-1] + 2 * (end_l[-2] + end_p[-2])
        for i in range(n - 2):
            tot += ((end_l[i] + end_p[i]) * (end_l[n - 3 - i] + end_p[n - 3 - i])) % num
        return tot % num

    def checkRecord2(self, n: int) -> int:
        if n == 1:
            return 3
        nums = [1, 1, 2]
        for i in range(2, n):
            nums.append((nums[i] + nums[i - 1] + nums[i - 2]) % num)
        result = (nums[n] + nums[n - 1] + nums[n - 2]) % num
        for i in range(n):
            result += nums[i + 1] * nums[n - i] % num
            result %= num
        return result


if __name__ == '__main__':
    print(Solution().checkRecord2(2))
