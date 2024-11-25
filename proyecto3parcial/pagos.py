import json as js
import datetime as dt
import pandas as pd
class pagos:
    def registro(codigo,pago):
        sticky=dt.datetime.now()
        fecha_limite=sticky+dt.timedelta(days=30)
        datos={codigo:{"pagos":[pago],"fechas":[sticky.strftime("%d-%m-%Y")],"fecha_limite":fecha_limite}}
        try:
            with open("pagos.json","r") as archivo:
                data=js.load(archivo)
                for x in data:
                    if x==codigo:
                        esta=1
                if not esta:
                    with open("abonos.json","r") as archivo:
                        data=js.load(archivo)
                        data.update(datos)
                    with open("abonos.json","w") as archivo:
                        js.dump(data,archivo,indent=4)
                else:
                    fechas=data[codigo]["fechas"]
                    pagoss=data[codigo]["pagos"]
                    fechas.append(sticky.strftime("%d-%m-%Y"))
                    pagoss.append(pago)
                    data[codigo]["fechas"]=fechas
                    data[codigo]["abonos"]=pagoss
                    data[codigo]["fecha_limite"]=fecha_limite
                    socios=pd.read_csv("socios.csv")
                    socios.loc[[codigo],["estado"]]="activo"
                    with open("abonos.json","w") as archivo2:
                        js.dump(data,archivo2,indent=4)
        except:
            with open("pagos.json","w") as archivo: 
                js.dump(datos,archivo,indent=4)
    def consulta():
        with open("pagos.josn","r") as archivo:
            data=js.load(archivo)
    def cortediario():
        pass

