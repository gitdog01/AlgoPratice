#include <iostream>

using namespace std;

int main(){
   int number;
   int n;
   int min = 1000001;
   int max = -1000001;
   
   cin>>n;
   
    while(cin>>number){
        max = number > max ? number : max;
        min = number < min ? number : min;
    }

    cout << min << " " << max << endl ;
    return 0;
}