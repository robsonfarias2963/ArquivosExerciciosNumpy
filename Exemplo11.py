import numpy as np 

array = np.array([1,2,3,4,5,6])

condicao = array != 2

filtro_array = array[condicao]

print("Filtro array:",filtro_array)