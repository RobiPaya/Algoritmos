import pandas as pd
class entrenadores:
    def registrar(nombre,sexo,fechadenacimiento,estado):
        try:
            with open("entrenadores.csv") as archivo:
                pass
            datos={"nombre":nombre,"sexo":sexo,"fecha_de_nacimiento":fechadenacimiento,"estado":estado}
            dt=pd.DataFrame(datos)
            dt.to_csv("entrenadores.csv", mode='a', index=False, header=False)
        except:
            datos={"nombre":nombre,"sexo":sexo,"fecha_de_nacimiento":fechadenacimiento,"estado":estado}
            dt=pd.DataFrame(datos)
            dt.to_csv("entrenadores.csv", mode='a', index=False)
    def consultar(posicion):
        archivo=pd.read_csv("entrenadores.csv")
        return archivo.iloc[posicion]
    def editar(posicion,columna,datoentrada):
        archivo=pd.read_csv("entrenadores.csv")
        archivo.loc[[posicion],[columna]]=datoentrada
        archivo.to_csv("entrenadores.csv",mode="w",index=False)  