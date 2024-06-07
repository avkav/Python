import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students   

#https://www.youtube.com/watch?v=PvNKKrPE0AI
#pip install pandas
#series  - son vectores, columnas o tablas


import pandas as pd #importamos librería como pd como se suele hacer
serie = pd.Series([1, 2, 3, 4])#aquí introducimos vectores
serie
serie.name = 'nombre'

#creamos la hoja de cálculo
datos={'Nombre':['Mariano','Johannes','Vale','Sharon','Justin'],'Calificación':['12','13','14','15','16']}
#convertimos la tabla en dataFrame - renglones y columnas, cuyo nombre será datos.
df=pd.DataFrame(datos)
print(df) # se imprime el df

