#include <bits/stdc++.h>

#define MAX 1000005
#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;

int temp[MAX];

ll inversion_count(int*, int, int);
ll merge(int*, int, int, int);


ll inversion_count(int arr[], int left, int right) {
    ll inv_cnt = 0;

    if (left < right) {
        int mid = left + (right - left) / 2;
        inv_cnt += inversion_count(arr, left, mid);
        inv_cnt += inversion_count(arr, mid + 1, right);
        inv_cnt += merge(arr, left, mid + 1, right);
    }

    return inv_cnt;
}


ll merge(int arr[], int left, int mid, int right) {
    int i = left;
    int j = mid;
    int k = left;

    ll inv_cnt = 0;

    while (i < mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        } else {
            temp[k++] = arr[j++];
            inv_cnt += (mid - i);
        }
    }

    while (i < mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];

    for (int i = left; i <= right; i++) arr[i] = temp[i];
    return inv_cnt;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    int arr[] = { 3, 3, 1, 2 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int ans = inversion_count(arr, 0, n - 1); 
    cout << " Number of inversions are " << ans; 

    return 0;
}