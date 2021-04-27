#include "TreeNode.h"
#include <iostream>
#include <vector>
using namespace std;


class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        rec(root, res);
        return res;
    }
    void rec(TreeNode* node, vector<int> &res){
        if (node){
            res.push_back(node->val);
            rec(node->left, res);
            rec(node->right,res);
        }
    }
};