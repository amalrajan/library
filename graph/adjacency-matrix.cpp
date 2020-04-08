#include <iostream>
#include <algorithm>

using namespace std;

void displayMatrix(int v, int *adj)
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

void displayGraph(int v, int *arr)
{
    for (int i = 0; i < v; i++)
    {
        cout << i << " --> ";
        for (int j = 0; j < v; j++)
        {
            if (*((arr + i * v) + j) == 1 && i != j)
            {
                cout << j << " --> ";
            }
        }
        cout << '\n';
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
        adj[a][b] = 1;
        adj[b][a] = 1;
    }

    displayMatrix(v, *adj);
    
    cout << '\n';

    displayGraph(v, *adj);

    return 0;
}