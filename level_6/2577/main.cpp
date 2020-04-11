#include <iostream>
#include <map>

int main(){

    int buf;
    int multi = 1;
    std::map<int,int> number_map;

    int temp;

    for(int n=0;n<10;n++) number_map.insert(std::pair<int,int>(n,0));
    
    for(int n=0;n<3;n++){
        std::cin >> buf;
        multi = multi * buf;
    }
    while(multi > 0){
        temp = multi % 10;
        multi = multi / 10;
        number_map[temp] = number_map[temp]+1;
    }
    for(auto it=number_map.begin();it!=number_map.end();it++){
        std::cout << it->second << std::endl;
    }
    
    return 0;
}