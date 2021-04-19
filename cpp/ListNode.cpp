#include <iostream>
#include <vector>
#include "ListNode.h"
using namespace std;

ListNode *createList(vector<int> args){
    ListNode sentinel(0);
    ListNode *head = &sentinel;
    for (int i:args){
        head->next = new ListNode(i);
        head = head->next;
    }
    return sentinel.next;
}

void printAll(ListNode *x){
    if (x){
        cout<< x->val << " ";
        printAll(x->next);
    }
}