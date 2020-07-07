#include <bits/stdc++.h>

#define MAX 1000005
#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


void prime_factorization(int n) {
    // 100 = (2 ^ 2) * (5 ^ 2)
    
    // if N is composite, there is at least 1 prime less than or equal to sqrt(n)
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            int cnt = 0;
            while (n % i == 0) {
                n /= i;
                cnt += 1;
            }
            cout << "(" << i << "^" << cnt << ") ";
        }
    }

    if (n > 1)
        cout << "(" << n << "^1" << ") ";
    cout << '\n';
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    prime_factorization(100);
    prime_factorization(1009);

    return 0;
}