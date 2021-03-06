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
    string output_array [n] {};
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
        // int arg_1_int {};
        // int arg_2_int {};
        // string cur_arg_1 {args_1[i]};
        // string cur_arg_2 {args_2[i]};
        // while (cur_arg_1.front() == '$') {
        //     int arg_1_idx {};
        //     string arg_1_idx_str {};
        //     arg_1_idx_str = cur_arg_1.substr(1);
        //     arg_1_idx = stoi(arg_1_idx_str);
        //     //arg_1_int = stoi(args_1[i]);
        //     cur_arg_1 = args_1[arg_1_idx];
        // }
        // while (cur_arg_2.front() == '$') {
        //     int arg_2_idx {};
        //     string arg_2_idx_str {};
        //     arg_2_idx_str = cur_arg_2.substr(1);
        //     arg_2_idx = stoi(arg_2_idx_str);
        //     //arg_2_int = stoi(args_2[i]);
        //     cur_arg_2 = args_2[arg_2_idx];
        // }
        // arg_1_int = stoi(cur_arg_1);
        // if (cur_arg_2 != "_") {
        //     arg_2_int = stoi(cur_arg_2);
        // }
        // //cout << operations[i] << endl << cur_arg_1 << endl << cur_arg_2 << endl;
        // cout << args_1[i] << endl << args_2[i] << endl;
        // string output {};
        // int output_int {};
        if (operations[i] == value) { // Filling the non-ref
            if (args_1[i].front() != '$') {
                output_array[i] = args_1[i];
            }
        }
        if (operations[i] == add) {
            if ((args_1[i].front() != '$') && (args_2[i].front() != '$')) {
                int cur_arg_1 {};
                int cur_arg_2 {};
                cur_arg_1 = stoi(args_1[i]);
                cur_arg_2 = stoi(args_2[i]);
                output_array[i] = cur_arg_1 + cur_arg_2;
            }
        }
        if (operations[i] == sub) {
            if ((args_1[i].front() != '$') && (args_2[i].front() != '$')) {
                int cur_arg_1 {};
                int cur_arg_2 {};
                cur_arg_1 = stoi(args_1[i]);
                cur_arg_2 = stoi(args_2[i]);
                output_array[i] = cur_arg_1 - cur_arg_2;
            }
        }
        if (operations[i] == mult) {
            if ((args_1[i].front() != '$') && (args_2[i].front() != '$')) {
                int cur_arg_1 {};
                int cur_arg_2 {};
                cur_arg_1 = stoi(args_1[i]);
                cur_arg_2 = stoi(args_2[i]);
                output_array[i] = cur_arg_1 * cur_arg_2;
            }
        }
    }
    for (int i = 0; i < n; i++) { // Adding the ref
        int arg_1_int {};
        int arg_2_int {};
        string cur_arg_1 {args_1[i]};
        string cur_arg_2 {args_2[i]};
        while (cur_arg_1.front() == '$') {
            int arg_1_idx {};
            string arg_1_idx_str {};
            arg_1_idx_str = cur_arg_1.substr(1);
            arg_1_idx = stoi(arg_1_idx_str);
            cur_arg_1 = output_array[arg_1_idx];
        }
        while (cur_arg_2.front() == '$') {
            int arg_2_idx {};
            string arg_2_idx_str {};
            arg_2_idx_str = cur_arg_2.substr(1);
            arg_2_idx = stoi(arg_2_idx_str);
            cur_arg_2 = output_array[arg_2_idx];
        }
        cout << cur_arg_1 << cur_arg_2 << endl;
        if (operations[i] == value) {
            output_array[i] = cur_arg_1[i];
        } 
        int cur_arg_1_int {};
        int cur_arg_2_int {};
        cur_arg_1_int = stoi(cur_arg_1);
        if (cur_arg_2 != "_") {
            cur_arg_2_int = stoi(cur_arg_2);
        }
        if (operations[i] == add) {
            output_array[i] = cur_arg_1_int + cur_arg_2_int;
        }
        if (operations[i] == sub) {
            output_array[i] = cur_arg_1_int - cur_arg_2_int;
        }
        if (operations[i] == mult) {
            output_array[i] = cur_arg_1_int * cur_arg_2_int;
        }
    }
    for (int i = 0; i < n; i++) {
        cout << output_array[i] << endl;
    }
}
