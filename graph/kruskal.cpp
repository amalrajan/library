#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int MAX = 10e4 + 5;
int parent[MAX];
int ranks[MAX];

int find(int x) {
    if (parent[x] == x)
        return x;
    return find(parent[x]);
}

int union1(int x, int y) {
    int xroot = find(x);
    int yroot = find(y);

    if (ranks[xroot] < ranks[yroot])
        parent[xroot] = yroot;
    else if (ranks[xroot] > ranks[yroot]) 
        parent[yroot] = xroot;
    else {
        parent[yroot] = xroot;
        ranks[xroot]++;
    }
}

bool compare(pair<int, pair<int, int>> &i, pair<int, pair<int, int>> &j) {
    return (i.first < j.first);
}

void kruskal(vector<pair<int, pair<int, int>>> graph, int nodes) {
    vector<pair<int, pair<int, int>>> result;

    int i = 0;
    int e = 0;

    sort(graph.begin(), graph.end(), compare);

    while (e < nodes - 1) {
        int wt = graph[i].first;
        int u = graph[i].second.first;
        int v = graph[i].second.second;

        i++;

        int x = find(u);
        int y = find(v);

        if (x != y) {
            e++;
            result.push_back({wt, {u, v}});
            union1(x, y);
        }
    }

    cout << "MST using Kruskal's algorithm: " << endl;

    for (auto i: result) {
        cout << i.second.first << ' ' << i.second.second << ' ' << i.first << endl;
    }
}

int main() {
    int nodes, edges;
    cin >> nodes >> edges;

    int a, b, wt;
    vector<pair<int, pair<int, int>>> graph;

    for (int i = 0; i < nodes; i++) {
        parent[i] = i;
        ranks[i] = 0;
    }

    for (int i = 0; i < edges; i++) {
        cin >> a >> b >> wt;

        graph.push_back({wt, {a, b}});
    }

    kruskal(graph, nodes);

    return 0;
}
