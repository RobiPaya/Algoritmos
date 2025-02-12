#include <iostream>
using namespace std;

int numerito = 0;

int main(){
    cout<< "Mete un numero : " <<endl;
    cin>> numerito;
    for (int i=1; i < 11; ++i){
        cout<<numerito<< " * "<<i<< " = "<< (numerito * i)<< endl;
    }
return 0;}