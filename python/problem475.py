from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        if houses[-1] <= heaters[0]:
            return heaters[0] - houses[0]
        if houses[0] >= heaters[-1]:
            return houses[-1] - heaters[-1]
        radius = 0
        ptr = 0
        for i in houses:
            while i > heaters[ptr]:
                ptr += 1
                if ptr == len(heaters):
                    return max(radius, houses[-1] - heaters[-1])
            radius = max(radius, min(abs(i - heaters[ptr - 1]), heaters[ptr] - i))
        return radius


if __name__ == '__main__':
    print(Solution().findRadius([1, 2, 3, 5, 15], [2, 30]))
