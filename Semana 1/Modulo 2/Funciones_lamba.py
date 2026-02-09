import pandas as pd
import numpy as np 

df = pd.read_csv('Superstore Sales Dataset.csv')

'''
FORMAS DE DECLARAR FUNCIONES EN PYTHON

FORMA 1: def
FORMA 2: lambda

DIFERENCIAS:

def SERA UNA FUNCION UTILIZABLE

MIENTRAS QUE lambda SERA UNA FUNCION UNICA Y DESECHABLE

LAS FUNCIONES lambda NO DEBERIAN TENER LOGICA COMPLEJA.

SUGERENCIAS: SI ESTAS USANDO lambda MAS DE 3 VECES , ES CONVENIENTE USAR FUNCION def.

'''

lambda x: "Alta" if x>500 else "baja"
def else_if(x):
    if x >500:
        return "Alta"
    else:
        return "Baja"
    

df["Nivel Venta"] = df["Sales"].apply(lambda x: x*1.16)

df["Venta IVA"] = df["Sales"]*1.16 


#df["Primer Nombre"] =  df["Customer Name"].apply(lambda x: (x*0.1)) if isinstance (x,(int,float)) and x >100

def calcular_bono_limpio(valor): 
    try:
        #Variables temporales  para claridad
        umbral = 100
        float(valor)
        tasa  = 0.1

        if valor > umbral:
            return valor * tasa 
        return 0
    except Exception:
        return None 
    


'''
1. Limpieza de Texto (Extracción)

A veces las columnas de ID tienen códigos que necesitamos separar. Supongamos que el Order ID tiene un formato como "CA-2016-152156".
Reto: Crea una columna llamada Market_Code que extraiga solo las dos primeras letras del Order ID.

2. Imagina que solo los productos de la categoría "Technology" tienen un impuesto adicional del 15% sobre el precio de venta.
Reto: Crea la columna Tax Amount.
Si Category es igual a 'Technology', multiplica Sales por 0.15. Si no, el valor es 8.

3.- Quieres crear una etiqueta amigable para una gráfica que combine la ciudad y el estado.
Reto: Crea la columna
Location Full que combine las columnas City y State en el formato: "Ciudad, Estado".

'''
# EJERCICIO 1: Crear columna Market_Code

# Tomamos la columna "Order ID" y usamos .str[:2]
# .str permite aplicar funciones de texto sobre cada valor de la columna
# [:2] significa "desde el inicio hasta el segundo carácter" (los dos primeros)
df["Market_Code"] = df["Order ID"].str[:2]

# Revisamos las primeras filas para confirmar#
print(df[["Order ID", "Market_Code"]].head())
#print("*" * 90)
df["Market_code"] = df["Order ID"].apply(lambda ID: ID[:2]) # ESTO ES PARA UNA SOLA COLUMNA


# EJERCICIO 2: Crear columna Tax Amount

# Usamos .apply() para recorrer cada fila del DataFrame
# axis=1 indica que trabajamos fila por fila
# La función lambda define la regla:add
# - Si la categoría es "Technology", el impuesto es Sales * 0.15
# - Si no, el impuesto es un valor fijo de 0
df["Tax Amount"] = df.apply(lambda fila: fila["Sales"] * 0.15 if fila["Category"] == "Technology" else 0, axis=1)
#ESTO ES PARA TRABAJAR CON VARIAS COLUMNA DEL Dataframe (df.apply)
# Revisamos las primeras filas para confirmar

print(df[["Category", "Sales", "Tax Amount"]].head())
print("*" * 90)
# EJERCICIO 3: Crear columna Location Full

# Concatenamos las columnas City y State
# Usamos el operador + para unir cadenas
# Agregamos ", " entre ellas para dar formato "Ciudad, Estado"
df["Location Full"] = df["City"] + ", " + df["State"]

# Revisamos las primeras filas para confirmar
print(df[["City", "State", "Location Full"]].head())
print("*" * 90)