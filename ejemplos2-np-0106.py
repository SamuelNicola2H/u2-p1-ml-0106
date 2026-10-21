import numpy as np

print("---------Llenar matriz de ceros---------")
matriz=np.zeros([3, 5]) # 3 filas x 5 columnas
print(matriz)
print("---------Llenar matriz de unos---------")
matriz=np.ones([3, 5])
print(matriz)
print("---------Llenar matriz vacios---------")
matriz=np.empty([3, 5])
print(matriz)
print("---------Llenar arreglo con rango---------")
# el primer parametro es el valor inicial
# el segundo parametro es el valor final
# el tercer parametro es el incremento
lista=np.arange(0, 10, 2)
print(lista)
print("---------Llenar arreglo con rango no 2---------")
# el primer parametro es el valor inicial
# el segundo parametro es el valor final
# el tercer parametro es el incremento
lista=np.arange(0, 10, 1)
print(lista)
