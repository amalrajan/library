#include <iostream>
#include <vector>

#define MAX 100005

using namespace std;

vector<int> adj[MAX];
bool visited[MAX];

void addEdge(int a, int b)
{
    adj[a].push_back(b);
    adj[b].push_back(a);
}

void DFS(int u)
{
    visited[u] = true;
    cout << u << ' ';

    for (auto i: adj[u])
    {
        if (!visited[i])
        {
            DFS(i);
        }
    }
}

int main()
{
    int v, e;

    cout << "Enter the number of vertices: ";
    cin >> v;
    cout << "Enter the number of edges: ";
    cin >> e;

    cout << "Enter the edge details:\n";

    int a, b;

    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
        adj[i].clear();
    }

    while (e--)
    {
        cin >> a >> b;
        addEdge(a, b);
    }

    // Depth-First-Search starting from vertex 0.
    DFS(0);

    return 0;
}