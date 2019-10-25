/*
 * algorytm03.cpp
 */


#include <iostream>

int main(int argc, char **argv)
{
	float stopien, radian;
    stopien = 0.0;
    do 
    {
        radian= stopien * M_PI / 180;
        cout << "cos(" << stopien << ") = " << cos(radian) << endl;
        stopien += 10.0;
    }
    
    while (cos(radian) != 0.0);
    
	return 0;
}

