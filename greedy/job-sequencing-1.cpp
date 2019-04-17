#include <iostream>
#include <algorithm>

using namespace std;

struct Job
{
    char id;
    int deadline;
    int profit;
};

bool comparison(Job a, Job b)
{
    /* Desceding order using Algorithms STL */
    return (a.profit > b.profit);
}

void jobScheduling(Job arr[], int n)
{
    sort(arr, arr+n, comparison);

    int result[n];
    bool slot[n] = {false};

    for (int i = 0; i < n; i++)
    {
        for (int j = min(n, arr[i].deadline) - 1; -1; j--)
        {
            if (slot[j] == false)
            {
                slot[j] = true;
                result[j] = i;
                break;
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        if (slot[i] == true)
        {
            cout << arr[result[i]].id << ' ';
        }
    }
}

int main()
{
    Job arr[] = { {'a', 2, 100}, {'b', 1, 19}, {'c', 2, 27}, 
                   {'d', 1, 25}, {'e', 3, 15}}; 
    int n = sizeof(arr)/sizeof(arr[0]);

    jobScheduling(arr, n);

    return 0;
}