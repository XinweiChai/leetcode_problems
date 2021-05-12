#include <iostream>
#include <vector>
using namespace std;

// Time complexity O(nlogn) by using fenwick tree.
int BIT[100005], a[100005], n;
void update(int x, int delta) {
    // x & -x gets the maximum 2^k factor of x
    for (; x <= n; x += x & -x) {
        BIT[x] += delta;
    }
}

int query(int x) {
    int sum = 0;
    for (; x > 0; x -= x & -x) sum += BIT[x];
    return sum;
}

long getCount(long number, int i) {
    int left = query(number - 1);
    int right = i - query(number);
    return left < right ? 2 * left + 1 : 2 * right + 1;
}

long minimumOperations(vector<int> numbers) {
    long ans = 0;
    n = 0;
    for (int i = 0; i < numbers.size(); i++) {
        n = max(n, numbers[i]);
    }
    for (int i = 0; i < numbers.size(); i++) {
        ans += getCount(numbers[i], i);
        update(numbers[i], 1);
    }
    return ans;
}

int main(int argc, char const *argv[]) {
    cout << minimumOperations({10, 6, 2, 3, 7, 1, 2});
    return 0;
}
