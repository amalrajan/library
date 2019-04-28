#include <iostream>
#include <vector>

using namespace std;

bool isCyclicUtil(vector<int> adj[], bool visited[], bool rec_stack[], int u)
{
    if (visited[u] == false)
    {
        visited[u] = true;
        rec_stack[u] = true;

        for (auto i: adj[u])
        {
            if (!visited[i] && isCyclicUtil(adj, visited, rec_stack, i))
                return true;
            else if (rec_stack[i])
                return true;
        }
    }
    rec_stack[u] = false;
    return false;
}

bool isCyclic(vector<int> adj[], bool visited[], bool rec_stack[], int v)
{
    for (int i = 0; i < v; i++)
    {
        if (isCyclicUtil(adj, visited, rec_stack, i))
        {
            return true;
        }
    }
    return false;
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
    bool rec_stack[v];

    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
        rec_stack[i] = false;
        adj[i].clear();
    }

    while (e--)
    {
        cin >> a >> b;
        
        adj[a].push_back(b);
    }

    if (isCyclic(adj, visited, rec_stack, v))
        cout << "Graph is cyclic.";
    else
        cout << "Graph is not cyclic.";

    return 0;
}