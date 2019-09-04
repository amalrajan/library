#include <iostream>

using namespace std;

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int min(int a, int b) {
    return a < b ? a : b;
}

void selection_sort(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        int min_index = i;
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[min_index]) {
                min_index = j;
            }
        }
        
        if (i != min_index)
            swap(arr[min_index], arr[i]);
    }
}

int main() {
    const int N = 5;
    int arr[N] = {1, 5, 2, 8, 0};

    selection_sort(arr, N);

    for (int i = 0; i < N; i++) cout << arr[i] << ' ';
    cout << endl;

    return 0;
}