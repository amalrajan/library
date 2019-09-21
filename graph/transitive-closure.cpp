#include <iostream>
#include <vector>

using namespace std;

void DFS(vector<int> adj[], vector<vector<int>> tc, int s, int v)
{
    tc[s][v] = 1;

    for (auto i: adj[v])
    {
        if (tc[s][i] == 0)
        {
            DFS(adj, tc, s, i);
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

    vector<int> adj[v];
    vector<vector<int>> tc(v, vector<int>(v, 0));
    vector<bool> visited(v, false);

    while (e--)
    {
        cin >> a >> b;
        
        adj[a].push_back(b);
    }


    // Breadth-First-Search starting from vertex 0.
    for (int i = 0; i < v; i++)
    {
        DFS(adj, tc, i, i);
    }

    for (int i = 0; i < v; i++)
    {
        for (int j = 0; j < v; j++)
        {
            cout << tc[i][j] << ' ';
        }
        cout << '\n';
    }

    return 0;
}