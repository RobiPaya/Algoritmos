import pandas as pd
class socios:
    def registrar(nombre,sexo,edad,entrenador):
        try:
            with open("socios.csv") as archivo:
                pass
            datos={"nombre":nombre,"sexo":sexo,"edad":edad,"entrenador":entrenador}
            dt=pd.DataFrame(datos)
            dt.to_csv("socios.csv", mode='a', index=False, header=False)
        except:
            datos={"nombre":nombre,"sexo":sexo,"edad":edad,"entrenador":entrenador}
            dt=pd.DataFrame(datos)
            dt.to_csv("socios.csv", mode='a', index=False)
    def consultar(posicion):
        archivo=pd.read_csv("socios.csv")
        return archivo.iloc[posicion]
    def editar(posicion):
        cliente=socios.consultar(posicion)
        print(cliente[0])
        
    
        