/*
 * @lc app=leetcode id=135 lang=cpp
 *
 * [135] Candy
 */
 #include <vector>
 #include <iostream>
 using namespace std;

// @lc code=start
class Solution {
public:
    int count(int n) {
        return (n * (n + 1)) / 2;
    }
    int candy(vector<int>& ratings) {
        if (ratings.size() <= 1) {
            return ratings.size();
        }
        int candies = 0;
        int up = 0;
        int down = 0;
        int oldSlope = 0;
        for (int i = 1; i < ratings.size(); i++) {
            int newSlope = (ratings[i] > ratings[i - 1]) ? 1 
                : (ratings[i] < ratings[i - 1] ? -1 
                : 0);

            if ((oldSlope > 0 && newSlope == 0) || (oldSlope < 0 && newSlope >= 0)) {
                candies += count(up) + count(down) + max(up, down);
                up = 0;
                down = 0;
            }
            if (newSlope > 0) {
                up++;
            } else if (newSlope < 0) {
                down++;
            } else {
                candies++;
            }
            oldSlope = newSlope;
        }
        candies += count(up) + count(down) + max(up, down) + 1;
        return candies;
    }
};
// @lc code=end

int main(int argc, char const *argv[])
{
    vector<int> a = {1,3,2,2,1};
    cout << Solution().candy(a);
    return 0;
}
