#include <iostream>
#include <algorithm>

using namespace std;

/* https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions */

void printEgyptianFraction(int num, int den)
{
    if (num == 0 || den == 0)
        return;
    if (den % num == 0)
    {
        cout << "1/" << den / num;
        return;
    }

    if (num % den == 0)
    {
        cout << num / den;
        return;
    }

    if (num > den)
    {
        cout << num / den + " + ";
        printEgyptianFraction(num % den, den);
        return;
    }

    int n = den / num + 1;
    cout << "1/" << n << " + ";
    printEgyptianFraction(num * n - den, den * n);
}

int main()
{
    int num, den;

    cout << "Enter the numerator: ";
    cin >> num;
    cout << "Enter the denominator: ";
    cin >> den;

    printEgyptianFraction(num, den);

    return 0;
}