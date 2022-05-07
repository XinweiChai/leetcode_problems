from typing import Sequence
from collections import Counter


class Solution:
    def leastInterval(self, tasks: Sequence[str], n: int) -> int:
        tasks_count = list(Counter(tasks).values())
        max_count = max(tasks_count)
        max_count_tasks = tasks_count.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
