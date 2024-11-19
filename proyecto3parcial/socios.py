import pandas as pd
class socios:
    def registrar(nombre,pago,sexo,edad,entrenador):
        try:
            with open("socios.csv") as archivo:
                pass
            datos={"nombre":nombre,"pagos":pago,"sexo":sexo,"edad":edad,"entrenador":entrenador}
            dt=pd.DataFrame(datos)
            dt.to_csv("socios.csv", mode='a', index=False, header=False)
        except:
            datos={"nombre":nombre,"pagos":pago,"sexo":sexo,"edad":edad,"entrenador":entrenador}
            dt=pd.DataFrame(datos)
            dt.to_csv("socios.csv", mode='a', index=False)
    def consultar():
        