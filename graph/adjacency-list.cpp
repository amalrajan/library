#include <iostream>
#include <vector>

#define MAX 10005

using namespace std;

vector<int> adj[MAX];

void add_edge(int a, int b)
{
    // Assuming the graph is undirected.
    adj[a].push_back(b);
    adj[b].push_back(a);
}

void clearGraph(int v)
{
    for (int i = 0; i <= v; i++)
    {
        adj[i].clear();
    }
}

void displayGraph(int v)
{
    for (int i = 0; i < v; i++)
    {
        cout << i << " --> ";
        for (auto j: adj[i])
        {
            cout << j << " --> ";
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

    clearGraph(v);

    while (e--)
    {
        cin >> a >> b;
        add_edge(a, b);
    }

    displayGraph(v);

    return 0;
}