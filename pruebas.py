import numpy as np

# Crear una lista vacía
mylist = []

# Generar un array de 1000 números aleatorios entre 0 y 1
num = np.random.rand(1, 1000)

# Añadir los elementos del array `num` a la lista `mylist`
mylist.extend(num[0])  # num[0] toma la primera fila del array

# Mostrar la lista actualizada
print(mylist)