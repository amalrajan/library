#include <iostream>
#include <vector>
#include <queue>

#define MAX 100005

using namespace std;

vector<int> adj[MAX];
bool visited[MAX];

void addEdge(int a, int b)
{
    adj[a].push_back(b);
    adj[b].push_back(a);
}

void BFS(int u)
{
    visited[u] = true;

    queue<int> q;
    q.push(u);

    while (!q.empty())
    {
        int s = q.front();
        cout << s << ' ';
        q.pop();

        for (auto i: adj[s])
        {
            if (!visited[i])
            {
                visited[i] = true;
                q.push(i);
            }
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

    // Breadth-First-Search starting from vertex 0.
    BFS(0);

    return 0;
}