import pandas as pd
import numpy as np 

df = pd.read_csv('Superstore Sales Dataset.csv')

#df.apply(Funcion)
# .apply se usa para aplicar una función a lo largo de un eje del DataFrame (filas o columnas)
# .applymap se usa para aplicar una función a cada elemento individual de un DataFrame

df["City_length"] = df["City"].apply(len)  #aplica la función len a cada elemento de la columna 'City' y crea una nueva columna 'City_length' con los resultados
#len = función incorporada de Python que devuelve la longitud (número de caracteres) de una cadena de texto


#print(df["Sales"].describe())  #muestra estadísticas descriptivas de la columna 'Sales' del DataFrame
        # .appy(lambda x: len(x))  #también se puede usar una función lambda para aplicar la función len a cada elemento de la columna 'City'
df["Sales_String"] = df["Sales"].apply(str)  #convierte cada elemento de la columna 'Sales' a una cadena de texto y crea una nueva columna 'Sales_String' con los resultados
                                #str = función incorporada de Python que convierte un valor a una cadena de texto
#.describe()  #muestra estadísticas descriptivas del DataFrame 
#print(df["Sales_String"].describe())  #muestra estadísticas descriptivas de la columna 'Sales_String' del DataFrame

df["Raiz Ventas"] = df["Sales"].apply(np.sqrt)  #aplica la función np.sqrt (raíz cuadrada) a cada elemento de la columna 'Sales' y crea una nueva columna 'Raiz Ventas' con los resultados
print(df["Raiz Ventas"].head(15))  #muestra las primeras 15 filas de la columna 'Raiz Ventas' del DataFrame


'''
1.- Normalización Logarítmica
En análisis de datos, las ventas suelen tener valores muy dispersos. 
Una técnica común es aplicar el logaritmo natural para "suavizar" los datos.

2.- Redondeo al Entero Superior (Techo)
Imagina que para logística necesitas calcular cuántas cajas usar, y cualquier decimal requiere una caja extra.

3.- En el dataset de Superstore, la columna Profit (Ganancias) puede tener valores negativos. 
Queremos saber rápidamente si la operación fue positiva, negativa o cero.

Reto: Crea una columna llamada Profit_Sign usando la función np.sign. 
Esta función devuelve 1 si es positivo, -1 si es negativo y 0 si es cero.

4.- Valores Absolutos para Análisis de Impacto
A veces no importa si perdimos o ganamos, sino la magnitud del movimiento de dinero.

5.- Para fines contables conservadores, quieres ignorar los decimales de las ventas y 
quedarte solo con la parte entera hacia abajo.

6.- Transformación Logarítmica SeguraEl logaritmo natural falla si el valor es 0. 
NumPy tiene una función llamada np.log1p que calcula $log(1 + x)$, 
lo cual es más estable para datos de ventas.
Reto: Aplica np.log1p a la columna Sales y guarda el resultado en Sales_Log_Stable.

7.- ndo la lógica es muy específica, lo mejor es definir una función con def y luego pasarla por nombre al apply.

Reto: Crea una función llamada calcular_iva que multiplique el valor por 0.16. Luego, aplícala a la columna Sales.
'''


# EJERCICIO "NORMALIZACION LOGARITMICA"
# Suavizar valores grandes de ventas usando logaritmo

df["Ventas_Log"] = np.log(df["Sales"])
df["Ventas_log"] =df["Sales"].apply(np.log)  #también se puede usar apply para aplicar np.log a cada elemento de la columna 'Sales'
# np.log aplica logaritmo natural a cada valor
# Se crea columna nueva llamada Sales_Log

# EJERCICIO 2 "Redondeo al entero superior (Techo)
# Redondear ventas hacia arriba (ideal para cajas)

df["Sales_Ceil"] = np.ceil(df["Sales"]) #ninguna funcion acepta dataframe como argumento,
                                        #por eso se aplica a cada elemento de la columna 'Sales' usando apply
df["Logistica"] = df["Sales"].apply(np.ceil) 
# np.ceil siempre redondea hacia arriba
# 2.3 → 3

# EJERCICIO 3 "Signo de la ganancia"
# Determinar si Profit es positivo, negativo o cero

df["Profit_Sign"] = np.sign(df["Profit"])
df["Profit sign"] = df["Profit"].apply(np.ceil)
# Resultado:
# Ganancia → 1
# Pérdida → -1
# Cero → 0

# EJERCICIO 4 "Valores absolutos para análisis de impacto"
# Obtener magnitud del dinero sin importar el signo

df["Profit_Abs"] = np.abs(df["Profit"])
df["Abs"] = df["Abs"].apply(np.abs)
# np.abs elimina el signo
# -150 → 150
abs(df["Sales"])

# EJERCICIO 5 "Redondeo hacia abajo (piso)"
# Quitar decimales bajando siempre

df["Sales_Floor"] = np.floor(df["Sales"])

# np.floor siempre redondea hacia abajo
# 4.9 → 4

# EJERCICIO 6 "Logaritmo seguro" 
# Logaritmo estable que funciona incluso con ceros

df["Sales_Log_Stable"] = np.log1p(df["Sales"])

# log1p calcula:
# log(1 + x)

# EJERCICIO 7 "Función personalizada para IVA"
# Crear función para calcular IVA

def calcular_iva(valor):
    # Recibe un valor de ventas
    # Devuelve el 16% (IVA)
    return valor * 0.16

# Aplicar función a la columna Sales

df["Sales_IVA"] = df["Sales"].apply(calcular_iva)

# apply envía cada valor a la función

df.head(10)
df[["Sales", "Profit", "Sales_IVA"]].head()

'''
IMPRIMIR VALORES
RETO: USAR LOC o ILOC PARA REALIZAR FILTROS ESPECIFICOS
'''
