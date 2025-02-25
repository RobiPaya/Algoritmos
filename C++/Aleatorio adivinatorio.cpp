#include <random>
#include <iostream>
using namespace std;

int numero;

int main() {
    random_device random;
    mt19937 gen(random());
    uniform_int_distribution<>dis(1,10);
    int aleatorio = dis(gen);
    cout << "Adivina un número del 1 al 10" << endl;
    cin>>numero;
    if(aleatorio == numero){
            cout << "Correcto el numero era " << aleatorio << endl;
    }
    else{
        cout << "Incorrecto, el número era : " << aleatorio << endl;
    }
return 0;}