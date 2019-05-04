#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Graph
{
    int v;
    vector<int> *adj;
    bool isCyclicUtil(int, bool*, int);

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

void Graph::addEdge(int a, int b)
{
    adj[a].push_back(b);
    adj[b].push_back(a);
}

bool Graph::isCyclicUtil(int v, bool visited[], int parent)
{
    visited[v] = true;

    for (auto i: adj[v])
    {
        // Notice here how nested ifs make a difference, rather than writing on the same line.
        if (!visited[i])
        {
            if (isCyclicUtil(i, visited, v))
                return true;
        }
        else if (i != parent)
            return true;
    }

    return false;
}

bool Graph::isCyclic()
{
    bool visited[v];
    for (int i = 0; i < v; i++)
        visited[i] = false;

    for (int i = 0; i < v; i++)
    {
        if (!visited[i])
        {
            if (isCyclicUtil(i, visited, -1))
            {
                return true;
            }
        }
    }

    return false;
}

int main()
{ 
    Graph g1(5); 
    g1.addEdge(1, 0); 
    g1.addEdge(0, 2); 
    g1.addEdge(2, 0); 
    g1.addEdge(0, 3); 
    g1.addEdge(3, 4); 
    g1.isCyclic()? cout << "Graph contains cycle\n": 
                   cout << "Graph doesn't contain cycle\n"; 
  
    Graph g2(3); 
    g2.addEdge(0, 1); 
    g2.addEdge(1, 2); 
    g2.isCyclic()? cout << "Graph contains cycle\n": 
                   cout << "Graph doesn't contain cycle\n"; 
  
    return 0; 
} 