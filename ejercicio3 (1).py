#prediccion de compra en un tienda en linea este codigo pretende evaluar el rendimineto 
#en datos compras en linea es decir si un cliente realizara la compra 
#teimpo_sitio:tiempo en minutos que el usurio paso en el sitio web 
#visitas producto:numeros de productos que el usuario ha visto 
#origen:oirigen del usuario(cero para directo,uno para redes sociales,dos para publicidad)
#compra:cero no compro 1 compro 



#clasificacion de riesgo de credito 
#con este ejercicion, ayudaras a un banco a clasificas a sus clientes segun su riesgo de credito 
#tienen los siguientes datos: edad,ingresos,deudas,historial crediticio (donde 1 significa buen historial y 0 mal historial.).abs
#la variabvle objetivo es riesgo crediticio es 1  para clientes de bajo riesgo y 0 para clientes de alto riesgo 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
import matplotlib.pyplot as plt
# Crear un conjunto de datos ficticio
df = pd.read_csv('trabajo3.csv')
X = df[['tiempo_sitio','visitas_producto','origen']]  # Variables independientes
y = df['compra']   # Variable dependiente


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42 )
# Crear el modelo de árbol de decisión
model =DecisionTreeRegressor(random_state=42 )
model.fit(X_train, y_train)
# Hacer predicciones
predicciones = model.predict(X_test)

# Imprimir las predicciones
print("Predicciones:", predicciones)

# Visualizar el árbol de decisión
plt.figure(figsize=(12,8))
tree.plot_tree(model,filled=True ,feature_names=X.columns,fontsize=10)
plt.title('Árbol de Decisión')
plt.show()
#class_names=['No', 'Sí']