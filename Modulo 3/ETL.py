import pandas as pd 

'''
El proces ETL es para Extraer datos (Extract), Transformaslos y limpiarlos (transform)
y finalmente cargarlos, compartilos en algun lado (Load)
'''

cafe = pd.read_csv('dirty_cafe_sales.csv')

print("--- Información general ---")
info = cafe.info()
print(info)

# Observación todos los datos son string (str)

print("\n --- Conteo de nulos ---")
print(cafe.isnull().sum())

'''
.isnull() -> me regresa valores nulos
.sum() -> suma todos los valores nulos encontrados en las columnas
'''

# Columnas Payment Method y Location tienen mas de 2000 valores nulos

cafe['Item'] = cafe['Item'].str.strip().str.title()


# print("\n --- Valores unicos en Item ---")
item_unicos = cafe['Item'].unique() # -> unique() solo aplica para UNA COLUMNA
# print(item_unicos)

# print("\n --- Valores unicos en Total Spent")
spent_unicos = cafe['Total Spent'].unique()

# print(spent_unicos)

columna_numericas = ['Quantity', 'Price Per Unit', 'Total Spent']

for col in columna_numericas:
    cafe[col] = pd.to_numeric(cafe[col], errors='coerce')

basura = ['Unknown', 'Error']
cafe['Item'] = cafe['Item'].replace(basura, pd.NA)

# item_unicos = cafe['Item'].unique() # -> unique() solo aplica para UNA COLUMNA
# print(item_unicos)

# print("--- A cotinuacion pagos unicos ---")
pagos_unicos = cafe['Payment Method'].unique()
# print(pagos_unicos)
moda_pago_unico = cafe['Payment Method'].mode()
# print(moda_pago_unico)
relleno_NAN = moda_pago_unico[0]
cafe['Payment Method'] = cafe['Payment Method'].fillna(relleno_NAN) #.dropna
# print('Metodos de pago rellenos')
pagos_unicos = cafe['Payment Method'].unique()
# print(pagos_unicos)

gasto_unico = cafe['Total Spent'].unique()
gasto_unico_moda = cafe['Total Spent'].mode()
print("---- Gasto unico -----")
print(gasto_unico_moda)

# Total Spent = Quantity * Price Per Unit

mask = cafe['Total Spent'].isna() & cafe['Quantity'].notna() & cafe['Price Per Unit'].notna()
# devolvera un 1 (True) si cumple la condicion y un 0 (False) si no la cumple

cafe.loc[mask,'Total Spent'] = cafe['Quantity'] * cafe['Price Per Unit']

cafe['Transaction Date'] = pd.to_datetime( cafe['Transaction Date'], errors='coerce')

columnas_de_interes = ['Item', 'Quantity', 'Total Spent', 'Payment Method', 'Transaction Date']
print ('---Informacion de las columnas de interes despues de la limpieza---')
print(cafe[columnas_de_interes].info())

print("---Valores unicos---")
print(cafe[columnas_de_interes].nunique())
print('---Valores nulos de las columnas de interes---')
print(cafe[columnas_de_interes].isnull().sum())

#print("\n --- Conteo de nulos despues de limpiar la columna Total Spent ---")
#print(cafe.isnull().sum()

#############
#Reducir los NAN de >"Item tomando como base el valor de Price Per Unit"
#cafe.to_csv("Ventas de cafe limpio.csv"),index = False

#############