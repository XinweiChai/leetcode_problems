/*
 * @lc app=leetcode id=264 lang=cpp
 *
 * [264] Ugly Number II
 */
#include <iostream>
#include <vector>
using namespace std;
// @lc code=start
class Solution {
public:
    int nthUglyNumber(int n) {
        int t2 = 0, t3 = 0, t5 = 0;  // pointers for 2, 3, 5
        vector<int> k(n);
        k[0] = 1;
        for (int i = 1; i < n; i++) {
            k[i] = min(k[t2] * 2, min(k[t3] * 3, k[t5] * 5));
            if (k[i] == k[t2] * 2) t2++;
            if (k[i] == k[t3] * 3) t3++;
            if (k[i] == k[t5] * 5) t5++;
        }
        return k[n - 1];
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    cout << Solution().nthUglyNumber(100);
    return 0;
}
