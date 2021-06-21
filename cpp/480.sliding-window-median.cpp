/*
 * @lc app=leetcode id=480 lang=cpp
 *
 * [480] Sliding Window Median
 */

#include <algorithm>
#include <functional>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
using namespace std;
// @lc code=start
class Solution {
   public:
    vector<double> medianSlidingWindow1(vector<int>& nums, int k) {
        multiset<int> window(nums.begin(), nums.begin() + k);
        multiset<int>::iterator mid = next(window.begin(), k / 2);
        vector<double> medians;
        for (int i = k;; i++) {
            // Push the current median.
            medians.push_back((double(*mid) + *prev(mid, 1 - k % 2)) / 2);

            // If all done, return.
            if (i == nums.size()) return medians;

            // Insert nums[i].
            window.insert(nums[i]);
            if (nums[i] < *mid) mid--;

            // Erase nums[i-k].
            if (nums[i - k] <= *mid) mid++;
            window.erase(window.lower_bound(nums[i - k]));
        }
    }
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        vector<double> a;
        vector<pair<int, int>> smallHeap;
        vector<pair<int, int>> largeHeap;
        for (int i = 0; i < k; ++i) {
            push(smallHeap, make_pair(nums[i], i));
        }
        for (int i = 0; i < k - (k >> 1); ++i) {
            move(smallHeap, largeHeap);
        }
        a.push_back(getMid(smallHeap, largeHeap, k));
        for (int i = k; i < nums.size(); ++i) {
            if (nums[i] >= ~largeHeap.front().first) {
                push(largeHeap, make_pair(~nums[i], i));
                if (nums[i - k] <= ~largeHeap.front().first) {   
                    move(largeHeap, smallHeap);
                }
            } else {
                push(smallHeap, make_pair(nums[i], i));
                if (nums[i - k] >= ~largeHeap.front().first) {
                    move(smallHeap, largeHeap);
                }
            }
            while (!smallHeap.empty() && i - k >= smallHeap.front().second) {
                pop(smallHeap);
            }
            while (!largeHeap.empty() && i - k >= largeHeap.front().second) {
                pop(largeHeap);
            }
            a.push_back(getMid(smallHeap, largeHeap, k));
        }
        return a;
    }
    struct comp {
        bool operator()(const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first == b.first) {
                return a.second > b.second;
            }
            return a.first < b.first;
        }
    };

    void push(vector<pair<int, int>>& a, pair<int, int> ele) {
        a.push_back(ele);
        push_heap(a.begin(), a.end(), comp());
    }

    void pop(vector<pair<int, int>>& a) {
        pop_heap(a.begin(), a.end(), comp());
        a.pop_back();
    }

    void move(vector<pair<int, int>>& a, vector<pair<int, int>>& b) {
        pair<int, int> temp = a.front();
        pop(a);
        push(b, make_pair(~int(temp.first), temp.second));
    }
    double getMid(vector<pair<int, int>>& a, vector<pair<int, int>>& b, int k) {
        if (k % 2 == 1)
            return ~b.front().first * 1.0;
        else
            return a.front().first / 2.0 + ~b.front().first / 2.0;
    }
};
// @lc code=end

int main(int argc, char const* argv[]) {
    vector<int> nums = {5, 5, 8, 1, 4, 7, 1, 3, 8, 4};
    auto a = Solution().medianSlidingWindow(nums, 8);
    for (double i : a) {
        cout << i << ' ';
    }
    return 0;
}
