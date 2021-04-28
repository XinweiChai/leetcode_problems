#include <iostream>
#include <string>
#include <unordered_map>
using std::cout;
using std::endl;
using std::max;
using std::string;
using std::unordered_map;

class Solution {
   public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> used;
        int max_len = 0, start = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (used.find(s[i]) != used.end() && start <= used[s[i]]) {
                start = used[s[i]] + 1;
            } else {
                max_len = max(max_len, i - start + 1);
            }
            used[s[i]] = i;
        }
        return max_len;
    }
};

int main(int argc, char const* argv[]) {
    cout << Solution().lengthOfLongestSubstring("tmmzuxt") << endl;
    return 0;
}
