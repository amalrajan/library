#include <bits/stdc++.h>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


int partition(int*, int, int);
void quick_sort(int*, int, int);

int partition(int arr[], int start, int end) {
    int i = start + 1;
    int pivot = arr[start];

    for (int j = start + 1; j <= end; j++) {
        if (arr[j] < pivot) {
            swap(arr[j], arr[i]);
            i += 1;
        }        
    }
    
    swap(arr[start], arr[i - 1]);
    return i - 1;
}

void quick_sort(int arr[], int start, int end) {
    if (start < end) {
        int j = partition(arr, start, end);
        quick_sort(arr, start, j);
        quick_sort(arr, j + 1, end);
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

    quick_sort(arr, 0, n - 1);
    for (int i = 0; i < n; i++) cout << arr[i] << ' ';

    return 0;
}