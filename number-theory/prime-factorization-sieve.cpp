#include <bits/stdc++.h>

#define MAX 1000005
#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


void prime_factorization_sieve(int n) {
    int arr[n + 1];
    fill(arr, arr + n + 1, -1);

    for (int i = 2; i <= n; i++) {
        if (arr[i] == -1) {
            for (int j = i * i; j <= n; j += i) {
                arr[j] = i;
            }
        }
    }

    while (n > 1) {
        if (arr[n] == -1) {
            cout << n << " ";
            break;
        }
        cout << arr[n] << " " ;
        n /= arr[n];
    }

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    prime_factorization_sieve(105);
    // prime_factorization(1009);

    return 0;
}