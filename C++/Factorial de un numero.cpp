#include <iostream>
using namespace std;

int numerito = 0;
int resultado=1;

int main(){
    cout<< "Mete un numero : " <<endl;
    cin>> numerito;
    for (int i=1; i < numerito+1; ++i){
        resultado= i * resultado;
    }
    cout<<"El factorial de "<<numerito<<" es: "<<resultado<<endl;
return 0;}