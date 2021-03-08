#include <iostream>

using namespace std;

int main(){

    int number;
    int max_order,max_number = 0;

    for(int n=0;n<9;n++){
        cin >> number;
        if(max_number < number){
            max_number = number;
            max_order  = n + 1;
        }
    }
    cout << max_number << endl;
    cout << max_order << endl;

    return 0;
}