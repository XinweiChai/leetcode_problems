from ListNode import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # if not headA or not headB:
        #     return None
        # countA = 0
        # save_headA = headA
        # save_headB = headB
        # while headA.next:
        #     countA +=1
        #     headA = headA.next
        # while headB.next:
        #     countA -=1
        #     headB = headB.next
        # headA = save_headA
        # headB = save_headB
        # if countA > 0:
        #     for _ in range(countA):
        #         headA = headA.next
        # else:
        #     for _ in range(-countA):
        #         headB = headB.next
        # if headA and headA == headB:
        #     return headA
        # while headA.next:
        #     headA = headA.next
        #     headB = headB.next
        #     if headA == headB:
        #         return headA
        # return None

        # Clever version
        if not headA or not headB:
            return None
        save_headA = headA
        save_headB = headB
        while (headA!=headB):
            headA = headA.next if headA else save_headB
            headB = headB.next if headB else save_headA
        return headA

a = ListNode(1)
print(Solution().getIntersectionNode(a,a))