
#include <iostream>
// Online C++ compiler to run C++ program online
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
    for(int i = 0; i < fila; ++i){
        for(int j = 0; j < columna; ++j){
            cout << matriz[i][j] << endl;
        }
    }
    cout << "Matriz modificada : " << endl;

    for(int i = 0; i < fila; ++i){
        for(int j = 0; j < columna; ++j){
            cin>>matriz[i][j];
            cout << matriz[i][j] << endl;
        }
    }
    return 0;
}