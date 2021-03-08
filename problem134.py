class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Stupid traversal
        # l = len(gas)
        # for i in range(l):
        #     cur = 0
        #     flag = True
        #     for j in range(l):
        #         pos = i + j if i + j < l else i + j - l
        #         cur += gas[pos] - cost[pos]
        #         if cur < 0:
        #             flag = False
        #             break
        #     if flag:
        #         return i
        # return -1
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return -1 if sum(gas)-sum(cost) < 0 else start


print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
