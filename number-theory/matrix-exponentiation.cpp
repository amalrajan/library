#include <bits/stdc++.h>

#define N 105
#define MAX 1000005
#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


int I[N][N];
int arr[N][N];


void multiply(int A[][N], int B[][N], int m) {
    int res[m + 1][m + 1];

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            res[i][j] = 0;
            for (int k = 0; k < m; k++) {
                res[i][j] += (A[i][k] * B[k][j]);
            }
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            A[i][j] = res[i][j];
        }
    }
}

void power_binary(int A[][N], int n, int m) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            if (i == j)
                 I[i][j] = 1;
            else
                I[i][j] = 0;
        }
    }

    while (n) {
        if (n & 1) {
            multiply(I, A, m);
            n -= 1;
        } else {
            multiply(A, A, m);
            n >>= 1;
        }
    }
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            cout << I[i][j] << " ";
        }
        cout << endl;
    }
}

void power(int A[][N], int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            if (i == j)
                 I[i][j] = 1;
            else
                I[i][j] = 0;
        }
    }

    for (int i = 0; i < n; i++) {
        multiply(I, A, m);
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            cout << I[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif

    int m, n;
    // Dimension and power
    cin >> m >> n;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    // power(arr, m, n);
    // cout << endl;
    power_binary(arr, m, n);

    return 0;
}
