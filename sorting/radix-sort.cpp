#include <bits/stdc++.h>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


int output[10005];

void radix_sort(int*, int);
void counting_sort(int*, int, int);

void radix_sort(int arr[], int n) {
    int mul = 1;
    int maxi = *max_element(arr, arr + n);

    while (maxi / mul) {
        counting_sort(arr, n, mul);
        mul *= 10;
    }
}

void counting_sort(int arr[], int n, int place) {
    int count[10];
    fill(count, count + 10, 0);

    for (int i = 0; i < n; i++) count[(arr[i] / place) % 10] += 1;
    for (int i = 1; i < 10; i++) count[i] += count[i - 1];

    for (int i = n - 1; i >= 0; i--) {
        output[(count[(arr[i] / place) % 10]) - 1] = arr[i];
        count[(arr[i] / place) % 10] -= 1;
    }

    for (int i = 0; i < n; i++) arr[i] = output[i];
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

    radix_sort(arr, n);
    for (int i = 0; i < n; i++) cout << arr[i] << ' ';

    return 0;
}