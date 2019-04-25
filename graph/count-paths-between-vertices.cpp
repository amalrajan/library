#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int path_count = 0;

int countPaths(vector<int> adj[], bool visited[], int s, int d)
{
    /* Counting number of paths between two vertices using backtracking */

    visited[s] = true;

    if (s == d)
    {
        path_count++;
    }
    else
    {
        for (auto i: adj[s])
        {
            if (!visited[i])
            {
                countPaths(adj, visited, i, d);
            }
        }
    }

    visited[s] = false;
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
    bool visited[v];

    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
        adj[i].clear();
    }

    while (e--)
    {
        cin >> a >> b;
        
        adj[a].push_back(b);
    }

    int s, d;

    cout << "Enter the source: ";
    cin >> s;
    cout << "Enter the destination: ";
    cin >> d;


    countPaths(adj, visited, s, d);

    cout << "Number of paths: " << path_count << '\n';

    return 0;
}