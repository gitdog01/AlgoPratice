#include <iostream>

using namespace std;

int main(){
    int a;
    int b;
    int number,temp;

    cin >> a >> b;

    number = b;

    for(int i=0;i<3;i++){
        cout << (number%10)*a << endl;
        number = number/10;
    }
    cout << a*b << endl;
    return 0;
}