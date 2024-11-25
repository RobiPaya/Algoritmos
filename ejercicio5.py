#clasificACION DE RIEGS DE Invcuplimineto  en prestamos  usando arboles de desiscion
#objetivo: entrenar un modelo de arbol de desicion para predecir si unn solicitante de prestamo podria incumplkir en funcin dee las variables como el monto de prestamo , historial crediticio y otros datos 


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree
import matplotlib.pyplot as plt
# Crear un conjunto de datos ficticio
df = pd.read_csv('trabajo5.csv')
X = df[['monto_prestamo','historial_crediticio','ingreso_anual','edad']]  # Variables independientes
y = df['incumplimiento']   # Variable dependiente


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