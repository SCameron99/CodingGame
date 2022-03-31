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
    int n {1};
    string value {"VALUE"};
    string add {"ADD"};
    string sub {"SUB"};
    string mult {"MULT"};
    cin >> n; cin.ignore();
    string operations [n] {};
    string args_1 [n] {};
    string args_2 [n] {};
    for (int i = 0; i < n; i++) {
        string operation;
        string arg_1;
        string arg_2;

        cin >> operation >> arg_1 >> arg_2; cin.ignore();
        operations[i] = operation;
        args_1[i] = arg_1;
        args_2[i] = arg_2;
    }  

    for (int i = 0; i < n; i++) {
        int arg_1_int {};
        int arg_2_int {};
        if (args_1[i].front() == '$') {
            args_1[i].erase(0,1);
            arg_1_int = stoi(args_1[i]);
            args_1[i] = args_1[arg_1_int];

        }
        if (args_2[i].front() == '$') {
            args_2[i].erase(0,1);
            arg_2_int = stoi(args_2[i]);
            args_2[i] = args_2[arg_2_int];
        }
        arg_1_int = stoi(args_1[i]);
        if (args_2[i] != "_") {
            arg_2_int = stoi(args_2[i]);
        }
        string output {};
        int output_int {};
        if (operations[i] == value) {
            cout << args_1[i] << endl;
        }
        if (operations[i] == add) {
            output_int = arg_1_int + arg_2_int;
            cout << output_int << endl;
        }
        if (operations[i] == sub) {
            output_int = arg_1_int - arg_2_int;
            cout << output_int << endl;
        }
        if (operations[i] == mult) {
            output_int = arg_1_int * arg_2_int;
            cout << output_int << endl;
        }
    }
}
