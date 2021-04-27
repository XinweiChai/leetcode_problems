#include <iostream>

#include "ListNode.h"
using namespace std;

class Solution {
   public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode *sentinel = new ListNode(INT32_MIN, head), *cur=head, *prev=sentinel, *next = nullptr;
        while (cur) {
            next = cur->next;
            if (cur->val < prev->val) {
                prev->next = next;
                ListNode *temp = sentinel;
                while (temp->next){
                    if (temp->val<=cur->val && temp->next->val>=cur->val){
                        cur->next = temp->next;
                        temp->next = cur;
                        break;
                    }
                    temp = temp->next;
                }
            }
            else{
                prev = cur;
            }
            cur = next;
        }
        return sentinel->next;
    }
};

int main(int argc, char const* argv[]) {
    vector<int> a = {4, 2, 1, 3};
    printAll(Solution().insertionSortList(createList(a)));
    return 0;
}