/*
 * @lc app=leetcode id=123 lang=cpp
 *
 * [123] Best Time to Buy and Sell Stock III
 */
#include <vector>
using namespace std;
// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<vector<int>> dp(3);
        for (vector<vector<int>>::iterator i = dp.begin(); i!=dp.end(); ++i){
            *i = vector<int>(prices.size());
        }
        for (int k=1;k<=2;++k){
            for (int i=0;i<prices.size();++i){
                for (int j=0;j<i;++j){
                    dp[k][i] = max(dp[k][i-1],prices[i]-prices[j]+dp[k-1][j-1]);
                }
            }
        }
        return dp[2][prices.size()-1];
    }
};
// @lc code=end

