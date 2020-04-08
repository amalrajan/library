#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


int kadane(int arr[], int n) {
    int curr_max = arr[0];
    int max_so_far = arr[0];

    for (int i = 1; i < n; i++) {
        curr_max = max(arr[i], curr_max + arr[i]);
        max_so_far = max(max_so_far, curr_max);
    }

    return max_so_far;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    string x = "ABCBDAB";
    string y = "BDCABA";
    cout << lcs(x, y);

    return 0;
}