#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>

#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;


int lcs(string x, string y) {
    int m = x.length(), n = y.length();
    int dp[m + 1][n + 1] = {};
    
    for (int i = 0; i <= m; i++) fill(dp[i], dp[i] + n + 1, 0);
    
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (x[i - 1] == y[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
            else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    return dp[m][n];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    string x = "ABCBDAB";
    string y = "BDCABA";
    cout << lcs(x, y);

    return 0;
}