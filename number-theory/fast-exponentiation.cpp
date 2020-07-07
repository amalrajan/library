#include <bits/stdc++.h>

#define MAX 1000005
#define ll long long
#define ull unsigned long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


ll fast_exponent(ll a, ll n) {
    if (a == 0)
        return 0;

    ull res = 1;

    while (n) {
        if (n & 1) {
            res *= a;
            n--;
        } else {
            a *= a;
            n >>= 1;
        }
    }

    return res;
}

ll fast_modular_exponent(ll a, ll n, ll mod) {
    if (a == 0)
        return 0;

    ull res = 1;

    while (n) {
        if (n & 1) {
            res = (res * a) % mod;
            n--;
        } else {
            a = (a * a) % mod;
            n >>= 1;
        }
    }

    return res;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    cout << fast_exponent(2, 3) << '\n';
    cout << fast_exponent(2, 30) << '\n';

    return 0;
}