#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Graph
{
    int v;
    vector<int> *adj;
    bool isCyclicUtil(int, bool*, bool*);

public:
    Graph(int v);
    void addEdge(int, int);
    bool isCyclic();
};

Graph::Graph(int v)
{
    this->v = v;
    adj = new vector<int>[v];
}

void Graph::addEdge(int u, int v)
{
    adj[u].push_back(v);
}

bool Graph::isCyclicUtil(int v, bool visited[], bool *recStack)
{
    if (!visited[v])
    {
        visited[v] = true;
        recStack[v] = true;

        for (auto i: adj[v])
        {
            if (!visited[i] && isCyclicUtil(i, visited, recStack))
            {
                return true;
            }
            else if (recStack[i])
            {
                return false;
            }
        }
    }

    recStack[v] = false;
    return false;
}

bool Graph::isCyclic()
{
    bool *visited = new bool[v];
    bool *recStack = new bool[v];
    
    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
        recStack[i] = false;
    }

    for (int i = 0; i < v; i++)
    {
        if (isCyclicUtil(i, visited, recStack))
        {
            return true;
        }
    }

    return false;
}