import json as js
import datetime as dt
import pandas as pd
class pagos:
    def registro(codigo,pago):#agrega el pago con el codigo 🎂🎂
        esta=0
        sticky=dt.datetime.now()
        fecha_limite=sticky+dt.timedelta(days=30)
        datos={codigo:{"pagos":[pago],"fechas":[sticky.strftime("%d-%m-%Y")],"fecha_limite":fecha_limite.strftime("%d-%m-%Y")}}
        try:
            with open("pagos.json","r") as archivo:
                data=js.load(archivo)
                for x in data:
                    if int(x)==codigo:
                        esta=1
                if esta==0:
                    with open("pagos.json","r") as archivo:
                        data=js.load(archivo)
                        data.update(datos)
                    with open("pagos.json","w") as archivo:
                        js.dump(data,archivo,indent=4)
                elif esta==1:
                    fechas=data[str(codigo)]["fechas"]
                    pagoss=data[str(codigo)]["pagos"]
                    fechas.append(sticky.strftime("%d-%m-%Y"))
                    pagoss.append(pago)
                    data[str(codigo)]["fechas"]=fechas
                    data[str(codigo)]["pagos"]=pagoss
                    data[str(codigo)]["fecha_limite"]=fecha_limite.strftime("%d-%m-%Y")
                    socios=pd.read_csv("socios.csv")
                    socios.loc[[int(codigo)],["estado"]]="activo"
                    with open("pagos.json","w") as archivo2:
                        js.dump(data,archivo2,indent=4)
        except:
            with open("pagos.json","w") as archivo: 
                js.dump(datos,archivo,indent=4)
        finally:
            archivo=pd.read_csv("socios.csv")
            archivo.loc[[codigo],["estado"]]="activo"
            archivo.to_csv("socios.csv",mode="w",index=False)   
    def consulta(codigo):
        with open("pagos.josn","r") as archivo:
            data=js.load(archivo)
            datos=data[codigo]
            return datos#te regresa el diccionario del socio con el id
    def cortediario():#reporte de las ganancias diarias
        total=0
        sticky=dt.datetime.now().strftime("%d-%m-%Y")
        with open("pagos.json","r") as archivo:
            data=js.load(archivo)
            for x in data:
                persona=data[x]["fechas"]
                for y in persona:
                    if y==sticky:
                        posicion=persona.index(y)
                        pago=data[x]["pagos"]
                        total+=pago[posicion]
        return total
    def cortemensual():#reporte de las ganancias mensuales
        total=0
        sticky=dt.datetime.now()
        mes=sticky-dt.timedelta(30)
        with open("pagos.json","r") as archivo:
            data=js.load(archivo)
            for x in data:
                persona=data[x]["fechas"]
                for y in persona:
                    fecha_descompuesta=y.replace("-"," ").split()
                    fecha=dt.datetime(int(fecha_descompuesta[2]),int(fecha_descompuesta[1]),int(fecha_descompuesta[0]))
                    if fecha>=mes:
                        posicion=persona.index(y)
                        pago=data[x]["pagos"]
                        total+=pago[posicion]
        return total

