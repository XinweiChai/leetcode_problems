#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER_ARRAY space
#
import collections


def segment(x, space):
    # Write your code here
    n = len(space)
    max_val = float("-inf")
    q = collections.deque()
    for i in range(n):
        while q and q[0] < i - x + 1:
            q.popleft()
        while q and space[q[-1]] >= space[i]:
            q.pop()
        q.append(i)
        if i >= x - 1:
            max_val = max(max_val, space[q[0]])
    return max_val


if __name__ == '__main__':
    print(segment(2, [8, 2, 4, 6]))
