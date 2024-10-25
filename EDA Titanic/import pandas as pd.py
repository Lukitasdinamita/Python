import pandas as pd

# Cargar el dataset
df = pd.read_csv('"C:\Users\lucas\OneDrive\Escritorio\Master\DataSet\Titanic\titanic\test.csv"')

# Primer vistazo a los datos
print(df.head())

# Información general del dataset
print(df.info())

# Estadísticas descriptivas
print(df.describe())

# Verificar valores nulos
print(df.isnull().sum())

# Filtrar filas donde una columna tenga un valor específico
filtro = df[df['edad'] > 30]
print(filtro.head())

# Eliminar filas con valores nulos
df_sin_nulos = df.dropna()

# Guardar el dataset modificado
df_sin_nulos.to_csv('nuevo_archivo.csv', index=False)
