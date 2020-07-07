#include <bits/stdc++.h>

#define MAX 1000005
#define ll long long
#define watch(x) cout << (#x) << " is " << (x) << endl

using namespace std;

vector<int> s;

void dfs(vector<vector<int>> &adj, bool visited[], int u) {
	visited[u] = true;

	for (auto i = adj[u].begin(); i != adj[u].end(); i++) {
		if (!visited[*i]) {
			dfs(adj, visited, *i);
		}
	}

	s.push_back(u);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

	int v, e;
	cin >> v >> e;

	vector<vector<int>> adj;
	adj.assign(v, vector<int>());

	int a, b;
	for (int i = 0; i < e; i++) {
		cin >> a >> b;
		adj[a].push_back(b);
	}

	bool visited[v];
	fill(visited, visited + v, false);

	for (int i = 0; i < v; i++) {
		if (!visited[i]) {
			dfs(adj, visited, i);
		}
	}

	for (auto i = s.rbegin(); i != s.rend(); i++) {
		cout << *i << " ";
	}

    return 0;
}