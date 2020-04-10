#include <iostream>

using namespace std;

int main(){

    int m,h,r;

    cin >> h >> m;

    if(m < 45){
        r = m-45;
        if( h == 0 ){
            h = 23;
        }else{
            h = h-1;
        }
        m = 60 + r;
    }else{
        m = m - 45;
    }

    cout << h << " " << m << endl;


    return 0;

}