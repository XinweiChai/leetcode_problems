class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for i in preorder.split(','):
            if stack and stack[-1] == '#':
                if len(stack) < 2:
                    return False
                stack.pop()
                stack.pop()
            stack.append(i)
        return stack == ['#']

    def isValidSerialization2(self, preorder: str) -> bool:
        stack = []
        p = preorder.split(',')
        if p.pop() != '#':
            return False
        for i in p:
            if i == '#':
                if stack:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack

    def isValidSerialization3(self, preorder: str) -> bool:
        p = preorder.split(',')
        slot = 1
        for node in p:
            if slot == 0:
                return False
            if node == '#':
                slot -= 1
            else:
                slot += 1
        return slot == 0


if __name__ == '__main__':
    print(Solution().isValidSerialization2("9,3,4,#,#,1,#,#,2,#,6,#,#"))
