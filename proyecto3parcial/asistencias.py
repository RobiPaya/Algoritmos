import pandas as pd
import datetime as dt
class asistencias:
    def registro(codigo): #solo necesita el id del socio para registrar su entrada
        fecha=dt.datetime.now().strftime("%d-%m-%Y")#Para sacar la fecha
        hora=dt.datetime.now().strftime("%H:%M")  #Para sacar las hora y minutos
        try:
            with open("asistencias.csv"):
                datos={"codigo":codigo,"fecha":fecha,"hora":hora}
                data=pd.DataFrame(datos)
                data.to_csv("asistencias.csv", mode='a', index=False, header=False)
        except:
            datos={"codigo":codigo,"fecha":fecha,"hora":hora}
            data=pd.DataFrame(datos)
            data.to_csv("asistencias.csv", mode='a', index=False)
    def reporte():
        posicion=0
        cont=0
        lista_ya_registrados=[]
        fecha_hoy=dt.datetime(dt.datetime.now().year,dt.datetime.now().month,dt.datetime.now().day)
        archivo=pd.read_csv("asistencias.csv")
        socios=pd.read_csv("socios.csv")
        for x in archivo["codigo"]:
            if x in lista_ya_registrados:
                posicion+=1
                pass
            else:
                fecha_a_descomponer=archivo.iloc[posicion]["fecha"]
                posicion+=1
                fecha_descompuesta=fecha_a_descomponer.replace("-"," ").split()
                fecha=dt.datetime(int(fecha_descompuesta[2]),int(fecha_descompuesta[1]),int(fecha_descompuesta[0]))
                if fecha==fecha_hoy:
                    lista_ya_registrados.append(x)
                    cont+=1
        porcentaje_de_asistencia=f"{(cont*100)/len(socios):.2f}"
        return porcentaje_de_asistencia #regresa solo el procentaje de asistencia de los socios 😒🤷‍♂️




