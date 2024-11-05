import json as js
class clientes():
    def registrarcliente(datos):
        try:
            with open("cleintes.json","r") as archivo:
                data=js.load(archivo)
                data.update(datos)
            with open("cleintes.json","w") as archivo:
                js.dump(data,archivo,indent=4)
        except:
            with open("cleintes.json","w") as archivo: 
                js.dump(datos,archivo,indent=4)
    def clienteid():
        lista=[]
        try:
            with open("cleintes.json","r") as archivo:
                data=js.load(archivo)
                for x in data:
                    lista.append(x)
                ultimocliente=int(max(lista))
                nuevocliente=ultimocliente+1
        except:
            nuevocliente=1
        return nuevocliente

        
