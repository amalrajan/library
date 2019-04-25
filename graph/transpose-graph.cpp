#include <iostream>
#include <vector>

using namespace std;

void transposeGraph(vector<int> adj[], vector<int> transpose[], int v)
{
    for (int i = 0; i < v; i++)
    {
        for (auto j: adj[i])
        {
            transpose[j].push_back(i);
        }
    }
}

void displayGraph(vector<int> adj[], int v)
{
    for (int i = 0; i < v; i++)
    {
        cout << i << " --> ";
        for (auto j: adj[i])
        {
            cout << j << " ";
        }
        cout << '\n';
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
    vector<int> transpose[v];

    for (int i = 0; i < v; i++)
    {
        adj[i].clear();
    }

    while (e--)
    {
        cin >> a >> b;
        
        adj[a].push_back(b);
    }

    cout << "Initial graph:\n";
    displayGraph(adj, v);
    transposeGraph(adj, transpose, v);
    cout << "Transposed graph:\n";
    displayGraph(transpose, v);


    return 0;
}