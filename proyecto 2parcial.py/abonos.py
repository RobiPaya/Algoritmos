import json as js
import datetime as dt
class abonos:
    def buscarclientes(codigo_entrada):
        esta=0
        codigo_entradita=codigo_entrada.get()
        with open("cleintes.json","r") as archivo:
            data=js.load(archivo)
            for x in data:
                nombre=data[x]["nombre"]
                direccion=data[x]["direccion"]
                telefono=data[x]["telefono"]
                saldomostrar=data[x]["saldo"]
                if x==codigo_entradita:
                    esta=1
        if esta==1:
            reporte=f"Nombre: {nombre}\nDireccion :{direccion}\nTelefono: {telefono}"
            saldo=f"Saldo: ${saldomostrar}"
        else:
            reporte="NO SE ENCONTRO"
            saldo=""
        return reporte,saldo   
    def registrarabono(codigo_entrada):
        codigo_entradita=codigo_entrada.get()
        try:
            with open("abonos.json","r") as archivo:
                data=js.load(archivo)
                for x in data:
                    if x==codigo_entradita:
                        pass
        except:
            pass