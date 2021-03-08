#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main(){

    int a,b,n;
    string str_a,str_c;
    str_c = "-";
    n = 0;

    cin >> a;

    if(10>a){str_a = "0"+to_string(a);
    }else{str_a = to_string(a);}


    b = (int)(str_a.at(0))-48 + (int)(str_a.at(1))-48;
    str_c = str_a.at(1) + to_string(b%10);
    n++;

    while(str_a != str_c){
        b = (int)(str_c.at(0))-48 + (int)(str_c.at(1))-48;
        str_c = str_c.at(1) + to_string(b%10);
        n++;
    }

    cout << n << endl;

    return 0;
}
