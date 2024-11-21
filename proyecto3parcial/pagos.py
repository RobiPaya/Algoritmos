import pandas as pd
import datetime as dt
class pagos:
    def registro(pago,fechas):
        #Al momento de agregar se necesita verificar si el codigo ya esta en la base de datos, si esta solo se agrega el pago, pero si no, se tiene que agregar todo desde cero
        try:
            with open("pagos.csv") as archivo:
                pass
            datos={"pagos_del_socio":[pago],"fechas_de_pago":[fechas]}
            dt=pd.DataFrame(datos)
            dt.to_csv("pagos.csv", mode='a', index=False, header=False)
        except:
            datos={"pagos_del_socio":[pago],"fechas_de_pago":[fechas]}
            dt=pd.DataFrame(datos)
            dt.to_csv("pagos.csv", mode='a', index=False)
    def consulta():
        pass
    def cortediario():
        pass

