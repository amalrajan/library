#include <iostream>
#include <vector>
#include <queue>

#define MAX 100005

using namespace std;

vector<int> adj[MAX];
bool visited[MAX];
int level[MAX];

void BFS(int u)
{
    queue<int> q;
    q.push(u);

    visited[u] = true;

    while (!q.empty())
    {
        int s = q.front();
        q.pop();
        
        for (auto i: adj[s])
        {
            if (!visited[i])
            {
                level[i] = level[s] + 1;
                q.push(i);
                visited[i] = true;
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
        level[i] = 0;
        adj[i].clear();
    }

    while (e--)
    {
        cin >> a >> b;
        
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    BFS(0);

    int n, cnt;
    while (true)
    {
        cnt = 0;

        cout << "Enter the level #: ";
        cin >> n;

        for (int i = 0; i < v; i++)
        {
            if (level[i] == n)
            {
                cnt++;
            }
        }

        cout << cnt << '\n';
    }

    return 0;
}