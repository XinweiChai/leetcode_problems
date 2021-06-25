/*
 * @lc app=leetcode id=241 lang=cpp
 *
 * [241] Different Ways to Add Parentheses
 */
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> diffWaysToCompute(string expression) {
        unordered_map<string, vector<int>> map;
        return dp(map, expression);
    }

    vector<int> dp(unordered_map<string, vector<int>> &map, string expr) {
        if (map.find(expr) == map.end()) {
            vector<int> res;
            for (int i = 0; i < expr.size(); ++i) {
                if (expr[i] == '+' || expr[i] == '-' || expr[i] == '*') {
                    vector<int> left = dp(map, expr.substr(0, i));
                    vector<int> right = dp(map, expr.substr(i + 1));
                    for (int j : left) {
                        for (int k : right) {
                            switch (expr[i]) {
                                case '+':
                                    res.push_back(j + k);
                                    break;
                                case '-':
                                    res.push_back(j - k);
                                    break;
                                case '*':
                                    res.push_back(j * k);
                                    break;
                                default:
                                    break;
                            }
                        }
                    }
                }
            }
            if (res.empty()) {
                map[expr] = {atoi(expr.c_str())};
            } else {
                map[expr] = res;
            }
        }
        return map[expr];
    }
};
// @lc code=end

int main(int argc, char const *argv[]) {
    for (int i : Solution().diffWaysToCompute("2-1-1")) {
        cout << i;
    }
    return 0;
}
