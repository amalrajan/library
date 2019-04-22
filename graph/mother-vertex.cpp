#include <iostream>
#include <vector>

#define MAX 100005

using namespace std;

// Using Kosaraju's strongly connected components algorithm.

vector<int> adj[MAX];
bool visited[MAX];

void addEdge(int a, int b)
{
    // Assuming the graph is directed.
    adj[a].push_back(b);
}

void DFS(int u)
{
    visited[u] = true;

    for (auto i: adj[u])
    {
        if (!visited[i])
        {
            DFS(i);
        }
    }
}

int findMotherVertex(int v)
{
    int last_vertex = 0;
    for (int i = 0; i < v; i++)
    {
        if (!visited[i])
        {
            DFS(i);
            last_vertex = i;
        }
    }

    for (int i = 0; i < v; i++)
        visited[i] = false;
    
    DFS(last_vertex);

    for (int i = 0; i < v; i++)
    {
        if (!visited[i])
        {
            return -1;
        }
    }

    return last_vertex;
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

    cout << findMotherVertex(v);

    return 0;
}