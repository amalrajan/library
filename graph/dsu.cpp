#include <bits/stdc++.h>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


void initialize(int arr[], int szarr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = i;
        szarr[i] = 1;
    }
}

int dsu_root(int arr[], int i) {
    while (arr[i] != i) i = arr[i];
    return i;
}

int dsu_find(int arr[], int a, int b) {
    return dsu_root(a) == dsu_root(b);
}

int dsu_union(int arr[], int a, int b) {
    arr[dsu_root(a)] = dsu_root(b);
}

int dsu_weighted_union(int arr[], int szarr[], int a, int b) {
    int root_a = dsu_root(a);
    int root_b = dsu_root(b);

    if (szarr[root_a] < szarr[root_b]) {
        arr[root_a] = arr[root_b];
        szarr[root_b] += szarr[root_a];
    } else {
        arr[root_b] = arr[root_a];
        szarr[root_a] += szarr[root_b];
    }
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif


    // initialization
    const int n = 10;
    int arr[n];
    int szarr[n];
    initialize(arr, szarr, n);


    return 0;
}