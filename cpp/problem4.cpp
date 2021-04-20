#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    float findMedianSortedArrays(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size();
        if (m > n) {
            // A.swap(B);
            swap(A, B);
            swap(m, n);
        }
        if (n == 0) {
            throw "Value Error";
        }
        int imin = 0, imax = m, half_len = (m + n + 1) / 2;
        float maxOfLeft, minOfRight;
        while (imin <= imax) {
            int i = (imin + imax) / 2;
            int j = half_len - i;
            if (i < m && B[j - 1] > A[i]) {
                imin = i + 1;
            } else if (i > 0 && A[i - 1] > B[j]) {
                imax = i - 1;
            } else {
                if (i == 0) {
                    maxOfLeft = B[j - 1];
                } else if (j == 0) {
                    maxOfLeft = A[i - 1];
                } else {
                    maxOfLeft = max(A[i - 1], B[j - 1]);
                }
                if ((m + n) % 2 == 1) {
                    return maxOfLeft;
                }
                if (i == m) {
                    minOfRight = B[j];
                } else if (j == n) {
                    minOfRight = A[i];
                } else {
                    minOfRight = min(A[i], B[j]);
                }
                return (maxOfLeft + minOfRight) / 2.0;
            }
        }
        return 0.0;
    }
};

int main(int argc, char const* argv[]) {
    vector<int> a = {1, 2, 3, 4, 5};
    vector<int> b = {4, 6, 7};
    cout << Solution().findMedianSortedArrays(a, b) << endl;
    return 0;
}