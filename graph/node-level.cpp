#include <iostream>
#include <vector>
#include <queue>

#define MAX 10005

using namespace std;

vector<int> adj[MAX];
bool visited[MAX];
int level[MAX];

void initialize(int v) {
    for (int i = 0; i < v; i++) {
        visited[i] = false;
        level[i] = 0;
        adj[i].clear();
    }
}

void bfs(int u) {
    visited[u] = true;
    level[u] = 0;

    queue<int> q;
    q.push(u);

    while (!q.empty()) {
        int s = q.front();
        q.pop();

        for (auto i: adj[s]) {
            if (!visited[i]) {
                level[i] = level[s] + 1;
                visited[i] = true;
                q.push(i);
            }
        }
    }
}

int main() {
    int v, e;
    cin >> v >> e;

    initialize(v);

    int a, b;
    for (int i = 0; i < e; i++) {
        cin >> a >> b;

        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    bfs(0);

    cout << "Levels: " << endl;

    for (int i = 0; i < v; i++) {
        cout << "Node " << i << " is at level: " << level[i] << endl;
    }

    return 0;
}