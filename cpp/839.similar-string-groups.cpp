/*
 * @lc app=leetcode id=839 lang=cpp
 *
 * [839] Similar String Groups
 */

#include <vector>
#include <string>
#include <numeric>
#include <iostream>
using namespace std;

// @lc code=start
class disjoint_set {
    vector<int> v;
    int sz;
public:
    disjoint_set(int n) {
        v.resize(n);
        iota(v.begin(), v.end(), 0);
        sz = n;
    }

    int find(int i) {
        if (i != v[i])
            v[i] = find(v[i]);
        return v[i];
    }

    // Using constant memory instead of a stack
    int find2(int i){
        int root = i;
        while (root!=v[root]){
            root = v[root];
        }
        while (v[i] != root){
            int parent = v[i];
            v[i] = root;
            i = parent;
        }
        return root;
    }

    // One-pass algorithm
    int find3(int i){
        while (v[i]!=i){
            // Path splitting
            // v[i] = v[v[i]];
            // i = v[i];

            // Path halving
            int temp = v[i];
            v[i] = v[v[i]];
            i = temp;
        }
        return i;
    }
    
    void join(int i, int j) {
        int ri = find3(i), rj = find3(j);
        if (ri != rj) {
            v[rj] = ri;
            sz--;
        }
    }
    
    int size() {
        return sz;
    }
};

class Solution {
public:
    bool similar(string &a, string &b) {
        int n = 0;
        for (int i = 0; i < a.size(); i++)
            if (a[i] != b[i] && ++n > 2)
                return false;
        return true;
    }

    int numSimilarGroups(vector<string>& A) {
        disjoint_set ds(A.size());
        for (int i = 0; i < A.size(); i++)
            for (int j = i + 1; j < A.size(); j++)
                if (similar(A[i], A[j]))
                    ds.join(i, j);
        return ds.size();
    }
};


// @lc code=end

int main(int argc, char const *argv[])
{
    vector<string> a = {"abcd", "dbca", "acbd", "efgh"};
    cout << Solution().numSimilarGroups(a);
    return 0;
}
