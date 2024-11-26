import json as js
import datetime as dt
class asistencias:
    def registro(codigo):
        sticky=dt.datetime.now()#.strftime("%d-%m-%Y") Para sacar la fecha
        hora=dt.datetime.now()#.strftime("%H:%M")  Para sacar las hora y minutos
        try:
            with open("pagos.json","r") as archivo:
                data=js.load(archivo)
                for x in data:
                    if int(x)==codigo:
                        esta=1
                if esta==0:
                    datos={codigo:{"fecha":[sticky.strftime("%d-%m-%Y")],"hora_entrada":[hora.strftime("%H:%M")],"hora_salida":[""]}}
                    with open("pagos.json","r") as archivo:
                        data=js.load(archivo)
                        data.update(datos)
                    with open("pagos.json","w") as archivo:
                        js.dump(data,archivo,indent=4)
                elif esta==1:
                    pass
        except:
            datos={codigo:{"fecha":[sticky.strftime("%d-%m-%Y")],"hora_entrada":[hora.strftime("%H:%M")],"hora_salida":[""]}}
            with open("pagos.json","w") as archivo: 
                js.dump(datos,archivo,indent=4)
        #entrada y salida
        
    def reporte():
        pass