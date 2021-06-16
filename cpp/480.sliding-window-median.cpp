/*
 * @lc app=leetcode id=480 lang=cpp
 *
 * [480] Sliding Window Median
 */

#include<vector>
#include<set>
#include<iostream>
using namespace std;
// @lc code=start
class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<int> window(nums.begin(), nums.begin() + k);
        multiset<int>::iterator mid = next(window.begin(), k / 2);
        vector<double> medians;
        for (int i = k;; i++) {
            // Push the current median.
            medians.push_back((double(*mid) + *prev(mid, 1 - k % 2)) / 2);

            // If all done, return.
            if (i == nums.size()) return medians;

            // Insert nums[i].
            window.insert(nums[i]);
            if (nums[i] < *mid) mid--;

            // Erase nums[i-k].
            if (nums[i - k] <= *mid) mid++;
            window.erase(window.lower_bound(nums[i - k]));
        }
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> nums = {1,3,-1,-3,5,3,6,7};
    Solution().medianSlidingWindow(nums,3);
    return 0;
}
