#include <iostream>
using namespace std;

int numerito = 0;

int main(){
    int contador = 0;
    cout<< "Mete un numero : " <<endl;
    cin>> numerito;
    for (int i=2; i < numerito; ++i){
        if(numerito % i == 0){
            contador+=1;
        }
    }
    if(contador == 0){
        cout << contador << endl;
        cout << "Hola" << endl;
    }
return 0;}