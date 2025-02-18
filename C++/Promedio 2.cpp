// Source: https://usaco.guide/general/io

#include <bits/stdc++.h>
#include <iostream>
using namespace std;

float numero = 0;
float total = 0;
float resultado;

int main() {
    cout<<"Ingresa los números para promediar : "<<endl;
	while(true){
        cin>>numero;
        if (cin.fail()){
            break;
        }
        else{
            resultado+=numero;
            total+=1;
        }
    }
    cout<<"Promedio : "<< (resultado/total) <<endl;
}
