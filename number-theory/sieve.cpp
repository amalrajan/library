#include <bits/stdc++.h>

#define MAX 1000005
#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


void sieve(int n) {
    // Check whether `num` is prime.
    // Prints primes in range (0, n].
    //O(log log n)
    
    bool primes[n + 1];
    fill(primes, primes + n + 1, true);

    primes[1] = false;
    primes[0] = false;

    for (int i = 2; i <= n; i++) {
        if (primes[i] == true) {
            for (int j  = i * i; j <= n; j += i) {
                primes[j] = false;
            }
        }
    }

    for (int i = 2; i <= n; i++) {
        if (primes[i] == true) {
            cout << i << '\n';
        }
    }
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    sieve(1005);

    return 0;
}