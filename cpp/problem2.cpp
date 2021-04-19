#include <iostream>

#include "ListNode.h"
using namespace std;

class Solution {
   public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        bool addOne = false;
        ListNode saveHead = ListNode();
        ListNode* sumNode = &saveHead;
        while (l1 || l2 || addOne) {
            sumNode->next = new ListNode();
            sumNode = sumNode->next;
            if (l1) {
                sumNode->val += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                sumNode->val += l2->val;
                l2 = l2->next;
            }
            if (addOne) {
                sumNode->val += 1;
                addOne = false;
            }
            if (sumNode->val >= 10) {
                sumNode->val -= 10;
                addOne = true;
            }
        }
        return saveHead.next;
    }
};

int main(int argc, char const* argv[]) {
    printAll(Solution().addTwoNumbers(createList({2, 4, 3, 5}),
                                      createList({5, 6, 4})));
    cout << endl;
    return 0;
}
