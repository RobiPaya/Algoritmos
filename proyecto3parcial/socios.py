import pandas as pd
import datetime as dt
class socios:
    def registrar(nombre,sexo,fechadenacimiento,entrenador,estado):#coloca las cosas en forma de index 💋
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
    def editar(posicion,columna,datoentrada): #aqui tienes que especificar el codigo que es la posicion, y su columna y porque lo quieres cambiar💕💕
        archivo=pd.read_csv("socios.csv")
        archivo.loc[[posicion],[columna]]=datoentrada
        archivo.to_csv("socios.csv",mode="w",index=False)  
    def edades():
        clasificaciones=[]
        archivo=pd.read_csv("socios.csv")
        for x in archivo["fecha_de_nacimiento"]:
            fecha_descompuesta=x.replace("-"," ").split()
            fecha_de_nacimiento=dt.datetime(int(fecha_descompuesta[2]),int(fecha_descompuesta[1]),int(fecha_descompuesta[0]))
            fecha_actual=dt.datetime.now()
            edad=int((fecha_actual-fecha_de_nacimiento).days/365)
            if edad>60:
                clasificaciones.append("adulto mayor")
            elif edad<60 and edad>18:
                clasificaciones.append("adulto")
            elif edad<18 and edad>12:
                clasificaciones.append("adolescente")
            elif edad<12:
                clasificaciones.append("infante")
        adultos_mayores=clasificaciones.count("adulto mayor")
        adultos=clasificaciones.count("adulto")
        adolescente=clasificaciones.count("adolescente")
        infante=clasificaciones.count("infante")
        total=len(clasificaciones)
        estadisticas={"totales":{"adultos_mayores":adultos_mayores,"adultos":adultos,"adolescentes":adolescente,"infante":infante,"total":total},"porcentajes":{"adultos_mayores":f"{((adultos_mayores*100)/total):.2f}","adultos":f"{((adultos*100)/total):.2f}","adolescentes":f"{((adolescente*100)/total):.2f}","infante":f"{((infante*100)/total):.2f}"}}
        return estadisticas #esto te regresa un diccionario con el total de acda clasificacion y su porcentaje 😂