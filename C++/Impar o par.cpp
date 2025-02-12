#include <iostream>
using namespace std;

int numerito = 0;

int main(){
    cout<< "Mete un numero : " <<endl;
    cin>> numerito;
    if (numerito % 2 == 0){
        cout<< "El número "<< numerito<< " es PAR"<< endl;
    }
    else{
        cout<< "El número "<< numerito<< " es IMPAR"<< endl;
    }
return 0;}