/*
 * @lc app=leetcode id=405 lang=cpp
 *
 * [405] Convert a Number to Hexadecimal
 */
#include <iostream>
#include <unordered_map>
using namespace std;
// @lc code=start
class Solution {
   public:
    const string HEX = "0123456789abcdef";
    string toHex(int num) {
        if (num == 0) return "0";
        string result;
        int count = 0;
        while (num && count++ < 8) {
            result = HEX[(num & 0xf)] + result;
            num >>= 4;
        }
        return result;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    cout << Solution().toHex(-1) << endl;
    return 0;
}
