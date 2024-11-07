import json as js
import datetime as dt
import tkinter as tk
class abonos:
    def buscarclientes(codigo_entrada, abono_entrada,text_area):
        esta=0
        codigo_entradita=codigo_entrada.get()
        with open("cleintes.json","r") as archivo:
            data=js.load(archivo)
            for x in data:
                if x==codigo_entradita:
                    abono_entrada.config(state="normal")
                    nombre=data[x]["nombre"]
                    direccion=data[x]["direccion"]
                    telefono=data[x]["telefono"]
                    saldomostrar=data[x]["saldo"]
                    esta=1
        if esta==1:
            reporte=f"Nombre: {nombre}\nDireccion :{direccion}\nTelefono: {telefono}"
            saldo=f"Saldo: ${saldomostrar}"
        else:
            abono_entrada.config(state="disabled")
            text_area.delete("1.0",tk.END)
            reporte="NO SE ENCONTRO"
            saldo=""
        return reporte,saldo   
    def registrarabono(codigo_entrada,abono_entrada):
        try:
            esta=0
            codigo_entradita=codigo_entrada.get()
            abono_entradita=abono_entrada.get()
            sticky=dt.datetime.now()
            datos={codigo_entradita:{"fechas":[sticky.strftime("%d-%m-%Y")],"abonos":[abono_entradita]}}
            try:
                with open("abonos.json","r") as archivo:
                    data=js.load(archivo)
                    for x in data:
                        if x==codigo_entradita:
                            esta=1
                    if esta==1:
                        fechas=data[codigo_entradita]["fechas"]
                        abonos=data[codigo_entradita]["abonos"]
                        fechas.append(sticky.strftime("%d-%m-%Y"))
                        abonos.append(abono_entradita)
                        data[codigo_entradita]["fechas"]=fechas
                        data[codigo_entradita]["abonos"]=abonos
                        with open("abonos.json","w") as archivo2:
                            js.dump(data,archivo2,indent=4)
                    else:
                        with open("abonos.json","r") as archivo:
                            data=js.load(archivo)
                            data.update(datos)
                        with open("abonos.json","w") as archivo:
                            js.dump(data,archivo,indent=4)
                with open("cleintes.json","r") as archivo:
                    data=js.load(archivo)
                    for x in data:
                        if x==codigo_entradita:
                            saldo=data[x]["saldo"]
                            nuevosaldo=saldo-int(abono_entradita)
                            data[x]["saldo"]=nuevosaldo
                            with open("cleintes.json","w") as archivo2:
                                js.dump(data,archivo2,indent=4)
            except:
                print(2)
                with open("cleintes.json","r") as archivo:
                    data=js.load(archivo)
                    for x in data:
                        if x==codigo_entradita:
                            saldo=data[x]["saldo"]
                            nuevosaldo=saldo-int(abono_entradita)
                            data[x]["saldo"]=nuevosaldo
                            with open("cleintes.json","w") as archivo2:
                                js.dump(data,archivo2,indent=4)
                with open("abonos.json","w") as archivo:
                    js.dump(datos,archivo,indent=4)
            return nuevosaldo
        except:
            return "NO PUEDES ABONAR PORQUE NO EXISTE"
    def mostrarregistro(codigo_entrada):
        registro=""
        codigo_entradita=codigo_entrada.get()
        with open("abonos.json","r") as archivo:
                    data=js.load(archivo)
                    for x in data:
                        if x==codigo_entradita:
                            fechas=data[codigo_entradita]["fechas"]
                            abonos=data[codigo_entradita]["abonos"]
                            for x in range(len(fechas)):
                                registro+=f"{fechas[x]}   :   ${abonos[x]}\n"
        return registro


