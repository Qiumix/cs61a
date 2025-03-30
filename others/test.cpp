#include <iostream>
using namespace std;
int small(int n)
{
    int t;
    for (t = 2; t < n + 1; t++)
    {
        if ((n % t) == 0)
            break;
    }
    return t;
}
void print(int n)
{
    int t = small(n);
    cout << t << ' ';
    n /= t;
    if (n == 1)
        return;
    print(n);
}
int main()
{
    int n = 1, m = 2;
    auto temp = n;
    n = m, m = temp;
    cout << n << '\n' << m << '\n';
    n ^= m ^= n ^= m;
    cout << n << '\n' << m << '\n';
    return 0;
}