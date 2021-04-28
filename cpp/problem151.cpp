#include <iostream>
#include <regex>
#include <string>
#include <vector>
using std::cout;
using std::endl;
using std::regex;
using std::sregex_token_iterator;
using std::string;
using std::vector;

string &trim(string &s) {
    if (s.empty()) {
        return s;
    }
    s.erase(0, s.find_first_not_of(" "));
    s.erase(s.find_last_not_of(" ") + 1);
    return s;
}

class Solution {
   public:
    string reverseWords(string s) {
        s = trim(s);
        regex reg("[ ]+");
        vector<string> v(sregex_token_iterator(s.begin(), s.end(), reg, -1),
                         sregex_token_iterator());
        s = v[v.size() - 1];
        for (int i = v.size() - 2; i >= 0; --i) {
            s += ' ' + v[i];
        }
        return s;
    }
};

int main(int argc, char const *argv[]) {
    cout << Solution().reverseWords("  Bob    Loves  Alice   ") << endl;
    return 0;
}