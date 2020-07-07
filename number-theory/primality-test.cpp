#include <bits/stdc++.h>

#define MAX 1000005
#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


bool primality_naive(ll num) {
    if (num <= 1) return false;

    for (int i = 2; i < num; i++) {
        if (num % i == 0)
            return false;
    }

    return true;
}


bool primality_logn(ll num) {
    if (num <= 1) return false;
    if (num == 2) return true;

    for (int i = 3; i <= sqrt(num); i++) {
        if (num % i == 0)
            return false;
    }

    return true;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    cout << primality_naive(10001) << endl;
    cout << primality_logn(3) << endl;

    return 0;
}