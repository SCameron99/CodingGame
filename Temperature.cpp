#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int n; // the number of temperatures to analyse
    int min_temp = 10000;
    int temp_n = 0;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int t; // a temperature expressed as an integer ranging from -273 to 5526
        cin >> t; cin.ignore();
        int(u) = abs(t);
        if (u < min_temp) {
            temp_n = t;
            min_temp = u;
        } else if ((u == min_temp) && (t != temp_n)) {
            temp_n = abs(temp_n);
        }
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << temp_n << endl;
}
