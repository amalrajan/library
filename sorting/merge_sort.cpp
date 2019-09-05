#include <iostream>
using namespace std;

void merge(int arr[], int start, int mid, int end) {
    int p = start;
    int q = mid + 1;

    int temp[end-start+1];
    int k = 0;

    for (int i = start; i <= end; i++) {
        if (p > mid)
            temp[k++] = arr[p++];
        else if (q > end)
            temp[k++] = arr[q++];
        else if ()
    }
}

int main() {
    
}