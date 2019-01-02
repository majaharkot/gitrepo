#include <iostream>

using namespace std;

int i, n, p1, p2, fib;

int main()
{
    cout << "Podaj n: ";
    cin >> n;
    fib = 0;
    if(n<3 && n>0)
		fib=1;
	else
	{
		p1=p2=1;
		i=3;
		while(i<=n)
		{
			fib=p1+p2;
			p2=p1;
			p1=fib;
			i++;
		}
	}
	cout << "F(" << n << ")=" << fib << endl;
    return 0;
}
