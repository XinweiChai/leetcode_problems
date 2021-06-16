from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # rank = [i[0] for i in sorted(enumerate(score), key=lambda x: -x[1])]
        # special = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        # for i in range(min(3, len(rank))):
        #     score[rank[i]] = special[i]
        # for i in range(3, len(rank)):
        #     score[rank[i]] = str(i + 1)
        # return score

        # A better solution
        dunums = sorted(score, reverse=True)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]
        dt = dict(zip(dunums, medal))
        return [dt[i] for i in score]

if __name__ == '__main__':
    print(Solution().findRelativeRanks(score=[10, 3, 8, 9, 4]))
