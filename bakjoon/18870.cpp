// for checkg support C++ (using g++)
//
// g++ -std=c++98 main.cpp
// g++ -std=c++03 main.cpp
// g++ -std=c++0x main.cpp
// g++ -std=c++11 main.cpp
// g++ -std=c++14 main.cpp
// g++ -std=c++17 main.cpp
#include <iostream>
using namespace std;
int main(){
int cpp = (int) __cplusplus;
int year = cpp / 100; // 1997 ... 2017
int month = cpp % 100;
cout << "Year:" << year << " Month:" << month << endl;
return 0;
}