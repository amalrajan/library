#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


const int s = (int) 1e6 + 1;
bool mark[s];
vector<ll> primes;


void simple_sieve() {
    fill(mark, mark + s, false);
    primes.push_back(2);

    for (ll i = 3; i <= s; i += 2) {
        if (!mark[i]) {
            primes.push_back(i);
            for (ll j = i * i; j <= s; j += (2 * i)) {
                mark[j] = true;
            }
        }
    }
}


void segmented_sieve(ll a, ll b) {
    fill(mark, mark + s, false);

    ll nsqrt = sqrt(b);
    if (a == 1) a++;

    for (ll i = 0; i < primes.size() && primes[i] <= nsqrt; i++) {
        ll p = primes[i];
        ll j = p * p;
        if (j < a) j = ((a + p - 1) / p) * p;

        for (; j <= b; j += p) {
            mark[j - a] = true;
        }
    }

    for (ll i = a; i <= b; i++) {
        if (!mark[i - a]) {
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

    ll tc, a, b;
    cin >> tc;

    simple_sieve();

    while (tc--) {
        cin >> a >> b;
        segmented_sieve(a, b);
        cout << '\n';
    }

    return 0;
}