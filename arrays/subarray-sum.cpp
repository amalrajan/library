#include <iostream>

using namespace std;

void printMaxSubarray(int arr[], int n, int req_sum)
{
    bool found = false;

    int curr_sum = arr[0];
    int start = 0;
    int i = 1;

    while (i <= n)
    {
        while (curr_sum > req_sum && start < i - 1)
        {
            curr_sum -= arr[start];
            start++;
        }

        if (curr_sum == req_sum)
        {
            found = true;
            cout << "Sum found between " << start << " and " << i - 1 << endl;
            break;
        }

        if (i < n)
        {
            curr_sum += arr[i];
        }

        i++;
    }

    if (!found)
    {
        cout << "No subarray found" << endl;
    }
}

int main()
{
    int arr[] = {13, 0, 1, 8, 9, 8, 11, 21}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    int req_sum = 23; 
    printMaxSubarray(arr, n, req_sum); 
    
    return 0; 
}