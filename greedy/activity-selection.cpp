#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

vector<pair<int, int>> selectOptimalSchedule(int start[], int finish[], int n)
{
    /* Sort the arrays based on finish times */
    for (int i = 0; i < n; i++)
    {
        int min_index = i;
        for (int j = i+1; j < n; j++)
        {
            if (finish[j] < finish[min_index])
            {
                min_index = j;
            }
        }
        
        int temp1 = finish[i];
        finish[i] = finish[min_index];
        finish[min_index] = temp1;

        int temp2 = start[i];
        start[i] = start[min_index];
        start[min_index] = temp2;
    }

    /* Data structure for storing scheduled activity pairs */
    vector<pair<int, int>> schedule;
    schedule.push_back({start[0], finish[0]});

    int k = 0;

    for (int i = 1; i < n; i++)
    {
        if (start[i] >= finish[k])
        {
            schedule.push_back({start[i], finish[i]});
            k = i;
        }
    }

    return schedule;
}

int main()
{
    int start[] = {1, 3, 0, 5, 8, 5};
    int finish[] =  {2, 4, 6, 7, 9, 9};

    int n = sizeof(start) / sizeof(start[0]);

    vector<pair<int, int>> schedule = selectOptimalSchedule(start, finish, n);

    for (auto val: schedule)
    {
        cout << val.first << ' ' << val.second << endl;
    }

    return 0;
}