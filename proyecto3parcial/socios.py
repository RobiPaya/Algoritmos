import pandas as pd
class socios:
    def registrar(nombre,sexo,fechadenacimiento,entrenador,estado):
        try:
            with open("socios.csv"):
                pass
            datos={"nombre":nombre,"sexo":sexo,"fecha_de_nacimiento":fechadenacimiento,"entrenador":entrenador,"estado":estado}
            dt=pd.DataFrame(datos)
            dt.to_csv("socios.csv", mode='a', index=False, header=False)
        except:
            datos={"nombre":nombre,"sexo":sexo,"fecha_de_nacimiento":fechadenacimiento,"entrenador":entrenador,"estado":estado}
            dt=pd.DataFrame(datos)
            dt.to_csv("socios.csv", mode='a', index=False)
    def consultar(posicion):
        archivo=pd.read_csv("socios.csv")
        return archivo.iloc[posicion]
    def editar(posicion,columna,datoentrada):
        archivo=pd.read_csv("socios.csv")
        archivo.loc[[posicion],[columna]]=datoentrada
        archivo.to_csv("socios.csv",mode="w",index=False)  