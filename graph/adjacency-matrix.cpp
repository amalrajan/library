#include <iostream>
#include <algorithm>

using namespace std;

void displayGraph(int v, int *adj)
{
    for (int i = 0; i < v; i++)
    {
        for (int j = 0; j < v; j++)
        {
            cout << *((adj + i * v) + j) << ' ';
        }
        cout << endl;
    }
}

void clearGraph(int v, int *adj)
{
    for (int i = 0; i < v; i++)
    {
        for (int j = 0; j < v; j++)
        {
            *((adj + i * v) + j) = 0;
        }
    }
}

int main()
{
    int v, e;
    int a, b;
    
    cout << "Enter the number of vertices: ";
    cin >> v;
    cout << "Enter the number of edges: ";
    cin >> e;

    cout << "Enter the edge details:\n";

    // Initialize the adjacency matrix.
    int adj[v][v];
    clearGraph(v, *adj);

    while (e--)
    {
        cin >> a >> b;

        // Assuming the graph is undirected.
        adj[a-1][b-1] = 1;
        adj[b-1][a-1] = 1;
    }

    displayGraph(v, *adj);

    return 0;
}