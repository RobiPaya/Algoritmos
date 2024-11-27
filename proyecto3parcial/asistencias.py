import pandas as pd
import datetime as dt
class asistencias:
    def registro(codigo):
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
        pass