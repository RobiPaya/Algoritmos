import json as js
class clientes():
    def __init__(self,idcodigo,idnombre,iddireccion,idtelefono,idsaldo):
        self.idcodigo=idcodigo
        self.idnombre=idnombre
        self.iddireccion=iddireccion
        self.idtelefono=idtelefono
        self.idsaldo=idsaldo
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
    def buscarclientes():
        pass
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

        
