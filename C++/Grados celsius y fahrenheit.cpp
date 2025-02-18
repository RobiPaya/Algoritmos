#include <iostream>
using namespace std;

float numerito = 0;
char grados = 'A';

int main(){
    cout<< "Convertir de Celsius a Fahrenheit (C) / Convertir de Fahrenheit a Celsius (F) : " <<endl;
    cin>> grados;
    if(grados == 'C'){
        cout << "Dame los grados Celsius que quieras convertir a Fahrenheit : " << endl;
        cin>> numerito;
        cout << numerito <<"°𝐶" <<" en grados Fahrenheit son : "<<(numerito * 9/5)+32 << "°𝐹" << endl;
    }
    else if(grados == 'F'){
        cout << "Dame los grados Fahrenheit que quieras convertir a Celsius : " << endl;
        cin>> numerito;
        cout << numerito <<"°𝐹" <<" en grados Celsius son : "<<(numerito - 32)* 5/9 << "°𝐶" << endl;
    }
    else{
        cout << "Error en la selección GG" << endl;
    }
return 0;}