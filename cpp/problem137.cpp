#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
   public:
    int singleNumber(vector<int>& nums) {
        // unordered_set<int> s;
        // long sum = 0;
        // for (int i : nums) {
        //     s.insert(i);
        //     sum += i;
        // }
        // for (long i : s) {
        //     sum -= 3 * i;
        // }
        // return -sum / 2;

        int ones = 0, twos = 0;
        for (int i : nums){
            ones = (ones ^ i) & ~twos;
            twos = (twos ^ i) & ~ones;
        }
        return ones;
    }
};