#include <iostream>
#include <algorithm>

using namespace std;

struct Job
{
    char id;
    int deadline;
    int profit;
};

struct DisjointSet
{
    int *parent;

    DisjointSet(int n)
    {
        parent = new int[n+1];

        for (int i = 0; i <= n; i++)
            parent[i] = i;
    }

    int find(int s)
    {
        if (s == parent[s])
            return s;
        parent[s] = find(parent[s]);
    }

    void merge(int u, int v)
    {
        parent[v] = u;
    }
};

bool cmp(Job a, Job b)
{
    return (a.profit > b.profit);
}

int findMaxDeadline(Job arr[], int n)
{
    int ans = -1;
    for (int i = 0; i < n; i++)
    {
        ans = max(ans, arr[i].deadline);
    }
    return ans;
}

int jobScheduling(Job arr[], int n)
{
    int maxDeadline = findMaxDeadline(arr, n);
    sort(arr, arr+n, cmp);

    DisjointSet ds(maxDeadline);

    for (int i = 0; i < n; i++)
    {
        int availableSlot = ds.find(arr[i].deadline);

        if (availableSlot > 0)
        {
            ds.merge(ds.find(availableSlot - 1), availableSlot);
            cout << arr[i].id << ' ';
        }
    }
}

int main()
{
    Job arr[] =  { { 'a', 2, 100 }, { 'b', 1, 19 },  
                   { 'c', 2, 27 },  { 'd', 1, 25 },  
                   { 'e', 3, 15 } }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    cout << "Following jobs need to be "
         << "executed for maximum profit\n"; 
    jobScheduling(arr, n); 
    return 0; 
}