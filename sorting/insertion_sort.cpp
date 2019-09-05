#include <iostream>
using namespace std;

void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void insertion_sort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int tmp = arr[i];
        int j = i;

        while (j > 0 && tmp < arr[j-1]) {
            arr[j] = arr[j-1];
            j--;
        }

        arr[j] = tmp;
    }
}

int main() {
    const int N = 5;
    int arr[N] = {5, 1, 2, 0, 8};

    insertion_sort(arr, N);

    for (int i = 0; i < N; i++) cout << arr[i] << ' ';
    cout << endl;

    return 0;
}