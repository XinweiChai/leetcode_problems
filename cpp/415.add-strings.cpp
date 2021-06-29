/*
 * @lc app=leetcode id=415 lang=cpp
 *
 * [415] Add Strings
 */

#include <iostream>
using namespace std;
// @lc code=start
class Solution {
   public:
    string addStrings(string num1, string num2) {
        int n1 = num1.length();
        int n2 = num2.length();
        if (n1 > n2) {
            swap(num1, num2);
            swap(n1, n2);
        }
        num1 = string(n2 - n1, '0') + num1;
        int carry = 0;
        int cur = 0;
        string res = "";
        for (int i = n2 - 1; i >= 0; --i) {
            cur = (num1[i] - '0') + (num2[i] - '0') + carry;
            carry = 0;
            if (cur >= 10) {
                ++carry;
                cur -= 10;
            }
            res = to_string(cur) + res;
        }
        if (carry == 1) {
            res = "1" + res;
        }
        return res;
    }
};
// @lc code=end
int main(int argc, char const *argv[]) {
    cout << Solution().addStrings("456", "77") << endl;
    return 0;
}
