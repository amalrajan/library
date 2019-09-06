#include <iostream>
#include <vector>
#include <deque>
#include <climits>

using namespace std;

const int MAX = 100005;

vector<int> adj[MAX];
int dist[MAX];


void initialize(int v) {
    for (int i = 0; i < v; i++) {
        adj[i].clear();
        dist[i] = INT_MAX;
    }
}

void zeroOneBFS(int src) { 
    deque <int> Q; 
    dist[src] = 0; 
    Q.push_back(src); 
  
    while (!Q.empty()) { 
        int v = Q.front(); 
        Q.pop_front(); 
  
        for (int i=0; i<edges[v].size(); i++) { 
            if (dist[edges[v][i].to] > dist[v] + edges[v][i].weight) { 
                dist[edges[v][i].to] = dist[v] + edges[v][i].weight; 
  
                if (edges[v][i].weight == 0) 
                    Q.push_front(edges[v][i].to); 
                else
                    Q.push_back(edges[v][i].to); 
            } 
        } 
    }
} 

int main() {
    int v, e;
    cin >> v >> e;

    int a, b, wt;
    for (int i = 0; i < v; i++) {
        cin >> a >> b >> wt;

        adj[a].push_back({b, wt});
        adj[b].push_back({a, wt});
    }

    zeroOneBFS(0);

    cout << "Distances: " << endl;
    for (auto i: dist) {
        cout << i << ' ';
    }

    return 0;
}