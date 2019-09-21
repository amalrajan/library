#include <iostream>
#include <string>
#include <alogrithm>

using namespace std;

int lis(int arr[], int n) {
    if (n == 0) {
        return 0;
    }
    if (arr[n] > arr[n - 1]) {
        return 1 + lis(arr, n - 1);
    }
    return max(lis(arr, n - 1))
}