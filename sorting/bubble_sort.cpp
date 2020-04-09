#include <bits/stdc++.h>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;

int arr[100005];


void bubble_sort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) swap(arr[j], arr[j + 1]);
        }
    }
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    // #ifndef ONLINE_JUDGE
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    // #endif

    const int n = 5;
    int arr[n] = {7, 2, 0, 2, 5};

    bubble_sort(arr, n);
    for (int i = 0; i < n; i++) cout << arr[i] << ' ';

    return 0;
}