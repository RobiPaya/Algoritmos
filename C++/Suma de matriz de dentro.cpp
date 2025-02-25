#include <iostream>
using namespace std;

int suma;

int main() {
    int matriz [2][3] = {
        {1,2,3},
        {4,5,6}
    };
    int filas = sizeof(matriz) / sizeof(matriz[0]); 
    int columnas = sizeof(matriz[0]) / sizeof(matriz[0][0]); 
    for(int i= 0; i<filas; ++i){
        for(int j = 0; j<columnas; ++j){
            suma+=matriz[i][j];
        }
    }
    cout << suma << endl;
return 0;}