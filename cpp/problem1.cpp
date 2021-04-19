#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> h;
        for (int i = 0; i < nums.size(); ++i) {
            int n = target - nums[i];
            if (h.find(n) != h.end()) {
                return {h[n], i};
            } else {
                h[nums[i]] = i;
            }
        }
        throw "No two sum solution";
    }
};

int main() {
    vector<int> a = {2, 7, 11, 15};
    vector<int> ivec = Solution().twoSum(a, 9);
    for (int c : ivec) cout << c << " ";
    cout << "\n";
    return 0;
}
