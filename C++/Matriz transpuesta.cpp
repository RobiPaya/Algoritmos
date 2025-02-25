
#include <iostream>
using namespace std;

int numero;

int main() {
    int matriz[2][3] = {
        {1,2,3},
        {4,5,6},
    };
    int fila = sizeof(matriz) / sizeof(matriz[0]);
    int columna = sizeof(matriz[0]) / sizeof(matriz[0][0]);
    for(int i = 0; i < columna; ++i){
        for(int j = 0; j < fila; ++j){
            cout << matriz[j][i] << " ";
        }
        cout << endl;
    }
    return 0;
}