/*
 * @lc app=leetcode id=363 lang=cpp
 *
 * [363] Max Sum of Rectangle No Larger Than K
 */

#include <limits.h>
#include <string.h>

#include <set>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        if (matrix.empty()) return 0;
        int row = matrix.size(), col = matrix[0].size(), res = INT_MIN;
        for (int l = 0; l < col; ++l) {
            vector<int> sums(row, 0);
            for (int r = l; r < col; ++r) {
                for (int i = 0; i < row; ++i) {
                    sums[i] += matrix[i][r];
                }

                // Find the max subarray no more than K
                set<int> accuSet;
                accuSet.insert(0);
                int curSum = 0, curMax = INT_MIN;
                for (int sum : sums) {
                    curSum += sum;
                    set<int>::iterator it = accuSet.lower_bound(curSum - k);
                    if (it != accuSet.end()) curMax = max(curMax, curSum - *it);
                    accuSet.insert(curSum);
                }
                res = max(res, curMax);
            }
        }
        return res;
    }
    int maxSumSubmatrix2(vector<vector<int>>& matrix, int k) {
        int m = matrix.size();
        int n = matrix[0].size();

        // colSum[i]: sum of col i while upper and lower rows are bounded
        int colSum[n];
        int res = INT_MIN;

        for (int i{0}; i < m; i++) {
            // for(int t{0}; t<n; t++)colSum[t] = 0;
            memset(colSum, 0, sizeof colSum);

            for (int j{i}; j < m; j++) {
                // Add current row
                for (int t{0}; t < n; t++) colSum[t] += matrix[j][t];

                // Kadane Optimization
                // For current fixed rows, Max SubArray Sum sor far
                int curMax = INT_MIN;
                // Max SubArray Ends at previous index
                int preMax = 0;

                for (int t{0}; t < n; t++) {
                    // Ends at current position/Column
                    // 1. Start fresh, 2. subArray following preIndex
                    preMax = max(colSum[t], colSum[t] + preMax);
                    curMax = max(curMax, preMax);
                }

                if (curMax <= k) {
                    res = max(res, curMax);
                    continue;  // Proceed to next row
                }

                // Selecting columns
                for (int l{0}; l < n; l++) {
                    int curSum = 0;
                    for (int r{l}; r < n; r++) {
                        // Including current columns
                        curSum += colSum[r];

                        if (curSum <= k) {
                            res = max(res, curSum);
                        }
                    }
                }
            }
        }
        return res;
    }
};
// @lc code=end
