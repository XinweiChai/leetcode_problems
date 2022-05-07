from typing import Sequence


class Solution:
    def findMaximumXOR(self, nums: Sequence[int]) -> int:
        # length of max number in a binary representation
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L, -1, -1):
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            curr_xor = max_xor | 1
            # compute all existing prefixes
            # of length (L - i) in binary representation
            prefixes = {num >> i for num in nums}
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            max_xor |= any(curr_xor ^ p in prefixes for p in prefixes)

        return max_xor


if __name__ == '__main__':
    print(Solution().findMaximumXOR(nums=[3, 10, 5, 25, 2, 8]))
