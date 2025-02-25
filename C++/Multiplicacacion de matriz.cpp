#include <iostream>
using namespace std;

int multiplicacion = 1;
int suma;
int total;

int main() {
    int matriz [2][3] = {
        {1,2,3},
        {4,5,6}
    };
    int matriz2 [2][3] = {
        {7,8,9},
        {10,11,12}
    };
    int filas = sizeof(matriz) / sizeof(matriz[0]); 
    int columnas = sizeof(matriz[0]) / sizeof(matriz[0][0]); 
    for(int i= 0; i<filas; ++i){
        for(int j = 0; j<columnas; ++j){
            suma = matriz[i][j];
            multiplicacion = multiplicacion * suma;
        }
    }
    int filas2 = sizeof(matriz2) / sizeof(matriz2[0]); 
    int columnas2 = sizeof(matriz2[0]) / sizeof(matriz2[0][0]); 
    for(int i= 0; i<filas2; ++i){
        for(int j = 0; j<columnas2; ++j){
            suma = matriz2[i][j];
            multiplicacion = multiplicacion * suma;
        }
    }
    cout << multiplicacion << endl;
return 0;}