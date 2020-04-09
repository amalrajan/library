#include <bits/stdc++.h>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;

int freq[100005];


void count_sort(int arr[], int n) {
    fill(freq, freq + 100005, 0);
    for (int i = 0; i < n; i++) freq[arr[i]] += 1;

    int i = 0, j = 0;
    while (i < n) {
        while (freq[j] > 0) {
            arr[i++] = j;
            freq[j] -= 1;
        }
        j += 1;
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

    count_sort(arr, n);
    for (int i = 0; i < n; i++) cout << arr[i] << ' ';

    return 0;
}