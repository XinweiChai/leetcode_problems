#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<vector<int>> jobs;
        int n = startTime.size();
        for (int i = 0; i < n; ++i) {
            jobs.push_back({endTime[i], startTime[i], profit[i]});
        }
        sort(jobs.begin(), jobs.end());
        map<int, int> dp = {{0, 0}};
        for (auto& job : jobs) {
            int cur = prev(dp.upper_bound(job[1]))->second + job[2];
            if (cur > dp.rbegin()->second){
                dp[job[0]] = cur;
            }
        }
        return dp.rbegin()->second;
    }
};

int main(int argc, char const* argv[]) {
    /* code */
    vector<int> startTime = {1, 2, 3, 4, 6}, endTime = {3, 5, 10, 6, 9},
                profit = {20, 20, 100, 70, 60};
    cout << Solution().jobScheduling(startTime, endTime, profit);
    return 0;
}
