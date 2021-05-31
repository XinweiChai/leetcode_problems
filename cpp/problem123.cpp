#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    int maxProfit(vector<int>& prices) {
        if (!prices.size()) return 0;
        int buy1 = INT32_MAX;
        int sell1 = INT32_MIN;
        int buy2 = INT32_MAX;
        int sell2 = INT32_MIN;
        for (int i = 0; i < prices.size(); i++) {
            buy1 = min(buy1, prices[i]);
            sell1 = max(sell1, prices[i] - buy1);
            buy2 = min(buy2, prices[i] - sell1);
            sell2 = max(sell2, prices[i] - buy2);
        }
        return sell2;
    }
};

int main(int argc, char const* argv[]) {
    // vector<int> a = {3, 3, 5, 0, 0, 3, 1, 4};
    vector<int> a = {1, 2, 3, 4, 5};
    cout << Solution().maxProfit(a);
    return 0;
}
