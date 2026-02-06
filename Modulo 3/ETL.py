import pandas as pd

'''
El proceso ETL es para extraer datos (Extract), transformarlos (Transform) y limpiarlos y finalmente cargarlos o compartirlos en algun lado
 (Load) '''

cafe = pd.read_csv('dirty_cafe_sales.csv')

print("--- Informacion general ---")
info = cafe.info()
print(info)

#Obsercion todos los datos son string (str)

print("\n--- Conteo de nulos ---")
print(cafe.isnull().sum())

#columna payment y method y location tienen mas de 2000 valores nulos strip corta espacios en blancos y 
# split divide lista en una cadena

print("\n--- Valores unicos en item ---")
item_unicos = cafe['Item'].unique()

print(item_unicos)

#print("\n -- valores unicos en Total Spent")
spent_unicos = cafe ["Total Spent"].unique()

print(spent_unicos)

columnas_numericas = ['Quantity', 'Price PER  Unit', 'Total Spent']

for col in columna_numericas:
    cafe[col] = pd.to_numeric(cafe[col], errors = 'coerce') 

    basura = 'Unknown','Error'
    cafe['Item'] = cafe ['Item'].replace(basura, pd.NA)

    item_unicos = cafe ['Item'].unique() #--> unique()solo aplica para una Columna
    

    pagos_unicos = ['Paymenth Method'].unique()
    print(pagos_unicos)
    moda_pago_unico = cafe ['Payment Method'].mode()
    print(moda_pago_unico)
    relleno_NAN = moda_pago_unico[0]
    cafe ('Payment') = cafe['Payment Method'].fillna(relleno_NAN) #dropna


    gasto_unico = cafe ['Total Spent'] 

