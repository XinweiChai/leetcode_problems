#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
   public:
    int threeSumClosest(vector<int>& nums, int target) {
        int diff = INT32_MAX;
        unsigned sz = nums.size();
        sort(begin(nums), end(nums));
        for (int i = 0; i < sz && diff != 0; ++i) {
            unsigned lo = i + 1, hi = sz - 1;
            while (lo < hi) {
                int sum = nums[i] + nums[lo] + nums[hi];
                if (abs(target - sum) < abs(diff)) diff = target - sum;
                if (sum < target)
                    ++lo;
                else
                    --hi;
            }
        }
        return target - diff;
    }
};

int main() {
    vector<int> v = {-1, 2, 1, -4};
    cout << Solution().threeSumClosest(v, 1) << endl;
    return 0;
}
