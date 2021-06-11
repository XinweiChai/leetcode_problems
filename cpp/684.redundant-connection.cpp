/*
 * @lc app=leetcode id=684 lang=cpp
 *
 * [684] Redundant Connection
 */

#include <numeric>
#include <vector>
using namespace std;

// @lc code=start
class DisjointSet {
    vector<int> v, rank;

   public:
    DisjointSet(int n) {
        v.resize(n + 1);
        rank.resize(n + 1);
        iota(v.begin(), v.end(), 0);
        fill(rank.begin(), rank.end(), 0);
    }

    int find(int i) {
        if (i != v[i]) v[i] = find(v[i]);
        return v[i];
    }

    bool join(int i, int j) {
        i = find(i);
        j = find(j);
        if (i == j) return false;
        if (rank[i] < rank[j]) swap(i, j);
        v[j] = v[i];
        if (rank[i] == rank[j]) rank[i]++;
        return true;
    }
};

class Solution {
   public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        DisjointSet ds(edges.size());
        for (auto i : edges) {
            if (!ds.join(i[0], i[1])) return i;
        }
        return {0, 0};
    }
};

// @lc code=end


int main(int argc, char const *argv[])
{
    vector<vector<int>> edges = {{1,2},{2,3},{3,4},{1,4},{1,5}};
    Solution().findRedundantConnection(edges);
    return 0;
}