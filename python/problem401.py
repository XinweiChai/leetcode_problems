from typing import Sequence
import itertools


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> Sequence[str]:
        res = []

        def has_ones(num):
            res = 0
            while num:
                res += num & 1
                num >>= 1
            return res

        for i in range(turnedOn + 1):
            minutes = []
            hours = []
            for hour in range(12):
                if has_ones(hour) == i:
                    hours.append(hour)
            for minute in range(60):
                if has_ones(minute) == turnedOn - i:
                    minutes.append(minute)
            for hour, minutes in itertools.product(hours, minutes):
                res.append(f"{hour}:{str(minutes).zfill(2)}")
        return res

    # Short version
    def readBinaryWatch2(self, turnedOn: int) -> Sequence[str]:
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == turnedOn]


if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))