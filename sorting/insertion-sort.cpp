#include <bits/stdc++.h>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;

int arr[100005];


void insertion_sort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int temp = arr[i];
        int j = i;

        while (j > 0 && temp < arr[j - 1]) {
            arr[j] = arr[j - 1];
            j -= 1;
        }

        arr[j] = temp;
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

    insertion_sort(arr, n);
    for (int i = 0; i < n; i++) cout << arr[i] << ' ';

    return 0;
}