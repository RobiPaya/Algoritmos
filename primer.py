import pandas as pd

# Especificar la ruta correcta al archivo
archivo = 'C:/Users/S8-M41/Documents/zayraochoa5C/edad.csv'

# Intentar leer el archivo con la codificación correcta
try:
    df = pd.read_csv(archivo, encoding='ISO-8859-1')  # Intentar con latin1 para caracteres especiales
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

# Mostrar las primeras filas del DataFrame para inspección inicial
print("Datos originales:")
print(df.head())
print("\nInformación sobre los datos originales:")
print(df.info())

# Verificar los primeros valores de cada columna
print("\nPrimeras filas de 'clave':")
print(df['clave'].head())
print("\nPrimeras filas de 'descripcion':")
print(df['descripcion'].head())

# Revisar valores únicos en las columnas
print("\nValores únicos en 'clave':")
print(df['clave'].unique())
print("\nValores únicos en 'descripcion':")
print(df['descripcion'].unique())

# Limpieza y conversión de la columna 'clave'
df['clave'] = pd.to_numeric(df['clave'], errors='coerce')  # Convertir a numérico, NaN para valores no convertibles
print("\nValores únicos en 'clave' después de conversión:")
print(df['clave'].unique())

# Limpieza y aseguramiento del formato de la columna 'descripcion'
df['descripcion'] = df['descripcion'].astype(str).str.strip()  # Eliminar espacios en blanco alrededor
print("\nPrimeras filas de 'descripcion' después de aseguramiento de formato:")
print(df['descripcion'].head())

# Eliminar filas con valores nulos en las columnas de interés
df_cleaned = df.dropna(subset=['clave', 'descripcion'])
print("\nDatos después de eliminar filas con valores nulos:")
print(df_cleaned.head())
print("\nInformación sobre los datos después de eliminar valores nulos:")
print(df_cleaned.info())

# Eliminar filas duplicadas
df_cleaned = df_cleaned.drop_duplicates()
print("\nDatos después de eliminar filas duplicadas:")
print(df_cleaned.head())
print("\nInformación sobre los datos después de eliminar duplicados:")
print(df_cleaned.info())

# Volver a asegurar que la columna 'clave' sea numérica y eliminar filas con NaN en 'clave'
df_cleaned['clave'] = pd.to_numeric(df_cleaned['clave'], errors='coerce')
df_cleaned = df_cleaned.dropna(subset=['clave'])  # Eliminar filas donde 'clave' es NaN después de la conversión
print("\nDatos después de asegurar que 'clave' sea numérico y eliminar NaNs:")
print(df_cleaned.head())
print("\nInformación sobre los datos después de asegurar la columna 'clave':")
print(df_cleaned.info())

# Guardar el DataFrame limpio en un nuevo archivo CSV
try:
    df_cleaned.to_csv('C:/Users/S8-M41/Documents/zayraochoa5C/edad_limpia.csv', index=False, encoding='ISO-8859-1')
    print("\nArchivo guardado correctamente como 'edad_limpia.csv'.")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")
