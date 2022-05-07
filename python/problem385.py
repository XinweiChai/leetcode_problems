# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype Sequence[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        elem = s.split(',')
        stack = [NestedInteger()]
        for i in elem:
            start = 0
            end = len(i) - 1
            while i[end] == ']':
                end -= 1
            while i[start] == '[':
                start += 1
                new = NestedInteger()
                stack[-1].add(new)
                stack.append(new)
            if start != end + 1:
                stack[-1].add(NestedInteger(int(i[start:end + 1])))
            for i in range(end + 1, len(i)):
                stack.pop()
        return stack[-1].getList()[-1]
