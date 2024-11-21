from pagos import pagos
import datetime as dt
hoy=dt.datetime.now()
pagos.registro([300,300,300],[hoy,hoy,hoy])
