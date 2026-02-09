import pandas as pd 

# ETL es para Extraer datos (Extract), Transformarlos y limpiarlos (Transform)
# y finalmente cargarlos o compartirlos en algún lado (Load)

cafe = pd.read_csv('dirty_cafe_sales.csv')

print("--- Información general ---")
info = cafe.info()
print(info)

# Observación: todos los datos son string (object), necesitamos convertir a números

print("\n--- Conteo de nulos ---")
print(cafe.isnull().sum())

# .isnull() -> me regresa valores nulos (True/False)
# .sum() -> suma todos los valores nulos encontrados en las columnas

# Columnas Payment Method y Location tienen más de 2000 valores nulos

# Limpiamos la columna Item: quitamos espacios y ponemos mayúsculas iniciales
cafe['Item'] = cafe['Item'].str.strip().str.title()

# print("\n--- Valores únicos en Item ---")
# item_unicos = cafe['Item'].unique()  # unique() solo aplica para UNA COLUMNA
# print(item_unicos)

# print("\n--- Valores únicos en Total Spent ---")
# spent_unicos = cafe['Total Spent'].unique()
# print(spent_unicos)

# Convertimos las columnas numéricas de texto (object) a números reales
columnas_numericas = ['Quantity', 'Price Per Unit', 'Total Spent']

for col in columnas_numericas:
    # to_numeric convierte texto a número
    # errors='coerce' significa: si no puedes convertir, pon NaN (vacío)
    cafe[col] = pd.to_numeric(cafe[col], errors='coerce')

# Reemplazamos palabras basura por valores vacíos
basura = ['Unknown', 'Error']
cafe['Item'] = cafe['Item'].replace(basura, pd.NA)

# item_unicos = cafe['Item'].unique()
# print(item_unicos)

# print("--- A continuación pagos únicos ---")
# pagos_unicos = cafe['Payment Method'].unique()
# print(pagos_unicos)

# Encontramos el método de pago más común (moda)
moda_pago_unico = cafe['Payment Method'].mode()
# print(moda_pago_unico)

# Tomamos el primer valor de la moda para rellenar vacíos
relleno_NAN = moda_pago_unico[0]

# Rellenamos los Payment Method vacíos con el valor más común
cafe['Payment Method'] = cafe['Payment Method'].fillna(relleno_NAN)  # .dropna eliminaría las filas
# print('Métodos de pago rellenados')
# pagos_unicos = cafe['Payment Method'].unique()
# print(pagos_unicos)

# gasto_unico = cafe['Total Spent'].unique()
# gasto_unico_moda = cafe['Total Spent'].mode()
# print("---- Gasto único -----")
# print(gasto_unico_moda)

# Calculamos Total Spent donde falta pero tenemos Quantity y Price Per Unit
# Fórmula: Total Spent = Quantity * Price Per Unit

# Creamos una máscara (filtro) para encontrar filas donde:
# - Total Spent está vacío Y
# - Quantity NO está vacío Y  
# - Price Per Unit NO está vacío
mask = cafe['Total Spent'].isna() & cafe['Quantity'].notna() & cafe['Price Per Unit'].notna()
# Devolverá un True si cumple la condición y un False si no la cumple

# En las filas que cumplen la condición, calculamos Total Spent
cafe.loc[mask, 'Total Spent'] = cafe['Quantity'] * cafe['Price Per Unit']

# Convertimos la columna de fechas a formato datetime
cafe['Transaction Date'] = pd.to_datetime(cafe['Transaction Date'], errors='coerce')

# ============================================================================
# NUEVA SECCIÓN: Inferir Items faltantes usando Price Per Unit
# ============================================================================

print("\n--- Creando diccionario Precio → Producto ---")

# Paso 1: Filtramos solo las filas donde conocemos AMBOS: Item Y Price
# Esto nos da una base confiable para crear el diccionario
item_por_precio = cafe.dropna(subset=['Item', 'Price Per Unit']) \
                      .groupby('Price Per Unit')['Item'] \
                      .agg(lambda x: x.mode()[0] if not x.mode().empty else None)

# .dropna(subset=[...]) -> elimina filas donde Item o Price estén vacíos
# .groupby('Price Per Unit') -> agrupa todas las filas con el mismo precio
# ['Item'] -> de cada grupo, nos enfocamos en la columna Item
# .agg(lambda...) -> para cada precio, encuentra el Item que más se repite (moda)

print("Relación Precio → Producto encontrada:")
print(item_por_precio)

# Paso 2: Creamos una función para rellenar Items vacíos
def rellenar_item(fila):
    """
    Esta función decide qué Item poner en cada fila:
    1. Si ya tiene Item, no lo toca
    2. Si no tiene Item pero sí Price, busca en el diccionario
    3. Si no puede hacer nada, lo deja vacío
    """
    # Si la fila YA tiene Item, devolvemos ese mismo Item
    if pd.notna(fila['Item']):
        return fila['Item']
    
    # Si la fila NO tiene Item pero SÍ tiene Price Per Unit
    # Y ese precio existe en nuestro diccionario
    if pd.notna(fila['Price Per Unit']) and fila['Price Per Unit'] in item_por_precio.index:
        # Devolvemos el Item que corresponde a ese precio según nuestro diccionario
        return item_por_precio[fila['Price Per Unit']]
    
    # Si no podemos inferir nada, dejamos el Item como está (vacío)
    return fila['Item']

# Paso 3: Aplicamos la función a TODAS las filas del DataFrame
# axis=1 significa "aplica la función fila por fila" (horizontal)
cafe['Item'] = cafe.apply(rellenar_item, axis=1)

print("--- Items faltantes rellenados usando el precio ---")

# ============================================================================

# Seleccionamos solo las columnas de interés para el análisis final
columnas_de_interes = ['Item', 'Quantity', 'Total Spent', 'Payment Method', 'Transaction Date']

print('\n--- Información de las columnas de interés después de la limpieza ---')
print(cafe[columnas_de_interes].info())

print("\n--- Valores únicos ---")
print(cafe[columnas_de_interes].nunique())

print('\n--- Valores nulos de las columnas de interés ---')
print(cafe[columnas_de_interes].isnull().sum())

# print("\n--- Conteo de nulos después de limpiar la columna Total Spent ---")
# print(cafe.isnull().sum())

# Guardamos el archivo limpio
# index=False significa: no guardes el número de fila como columna
cafe.to_csv("ventas_cafe_limpio.csv", index=False)

print("\n Archivo guardado como 'ventas_cafe_limpio.csv'")