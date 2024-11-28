import pandas as pd
class entrenadores:
    def registrar(nombre,sexo,fechadenacimiento,estado):#lomismoqueensocios
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
    def editar(posicion,columna,datoentrada):#lo mismo que en socios
        archivo=pd.read_csv("entrenadores.csv")
        archivo.loc[[posicion],[columna]]=datoentrada
        archivo.to_csv("entrenadores.csv",mode="w",index=False)
    def controldesocios():
        control_de_socios={}
        archivo=pd.read_csv("socios.csv")
        archivo_de_entrenadores=pd.read_csv("entrenadores.csv")
        for entrenador in archivo_de_entrenadores["nombre"]:
            cont=0
            for entrenador_seleccionado in archivo["entrenador"]:
                if entrenador==entrenador_seleccionado:
                    cont+=1
            control_de_socios[entrenador]=cont
        return control_de_socios #esto te regresa un diccionario con los entrenadores y cuantos socios cuida 😂
