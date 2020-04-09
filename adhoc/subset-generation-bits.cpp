#include <bits/stdc++.h>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


void generate_subsets(int arr[], int n) {
    for (int i = 0; i < (1 << n); ++i) {
        for (int j = 0; j < n; ++j) {
            if (i & (1 << j)) cout << arr[j] << ' ';
        }
        cout << '\n';
    }
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int n = 5;
    int arr[n] = {1, 2, 3, 4, 5};

    generate_subsets(arr, n);

    return 0;
}