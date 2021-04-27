#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node){
            return nullptr;
        }
        if (copies.find(node)==copies.end()){
            copies[node] = new Node(node->val);
            for (Node* i : node->neighbors){
                copies[node]->neighbors.push_back(cloneGraph(i));
            }
        }
        return copies[node];
    }
private:
    unordered_map<Node*, Node*> copies;
};

