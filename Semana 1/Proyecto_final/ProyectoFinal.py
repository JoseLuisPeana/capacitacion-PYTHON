import pandas as pd #LIBRERIA PRINCIPAL PARA MANIPULAR DATAFRAME
import numpy as np #IMPORTA NUMPY PARA MANEJAR VALORES NUMERICOS Y NaN
import re  # IMPORTA EXPRESIONES  REGULARES PARA LIMPIAR TEXTO(PRECIOS,NUMEROS DENTROS DE STRING)
def cargar_datos(archivo):#DEFINE UNA FUNCION QUE RECIBE LA RUTA DE ARCHIVO CSV
    # Carga el archivo y maneja error si no existe
   
    try: #INTENTA EJECUTAR EL BLOQUE DE CODIGO
        
        return pd.read_csv(archivo)#LEE EL ARCHIVO CSV Y LO DEVUELVE COMO DATAFRAME
    
    except FileNotFoundError: #SI EL ARCHIVO NO EXISTE ENTRA AQUI

        print("ERROR: Archivo no encontrado")#MUESTRA UN MENSAJE DE ERROR AL USUARIO
        
        return None #REGRESA None PARA EVITAR QUE EL PROGRAMA CONTINUE CON DATOS INEXISTENTES

#funcion para limpiar precio quitando simbolos y se vuelve float
def limpiar_precio(valor):#FUNCION QUE LIMPIA PRECIOS QUE VIENEN COMO TEXTO 
    # Limpia precios tipo "$1,234.00" → 1234.0
    if pd.isna(valor): #SI EL VALOR ES NULO (NaN), SE REGRESA Nan
        return np.nan
    valor = re.sub(r'[^\d.]', '', str(valor)) #ELIMINA TODO LO QUE NO SEA NUMERO O PUNTO (QUITA $, COMAS,TEXTO, ETX)

    try: #INTENTA CONVERTIR EL VALOR LIMPIO A FLOAT
        return float(valor) 
    except ValueError:
        return np.nan


# Convierte porcentajes tipo '85%' a decimal (0.85)
def limpiar_porcentaje(valor):
    # Convierte porcentajes tipo "85%" → 0.85
    if pd.isna(valor):
        return np.nan
    try:
        return float(str(valor).replace('%', '')) / 100
    except ValueError:
        return np.nan

# Intenta inferir el número de baños cuando el dato falta
def inferir_banos(fila):

    # Busca números dentro del texto descriptivo
    if pd.notna(fila['bathrooms']):
        return fila['bathrooms']

    if pd.notna(fila.get('bathrooms_text')):
        nums = re.findall(r'\d+\.?\d*', str(fila['bathrooms_text']))
        if nums:
            return float(nums[0])
        
# Estima baños usando el número de habitaciones
    if pd.notna(fila.get('bedrooms')):
        return max(1.0, fila['bedrooms'] / 2)

    return 1.0

# Agrupa los tipos de propiedad en categorías simples
def crear_categoria(propiedad, habitacion):
    # Agrupa tipos de propiedad en categorías simples
    if pd.isna(propiedad):
        return 'Desconocido'
    p = str(propiedad).lower()
    if 'apartment' in p or 'condo' in p:
        return 'Departamento'
    if 'house' in p or 'villa' in p:
        return 'Casa'
    if 'hotel' in p or 'hostel' in p:
        return 'Hotel'
    if habitacion == 'Private room':
        return 'Habitación privada'
    if habitacion == 'Shared room':
        return 'Habitación compartida'
    return 'Otro'

# Función principal que ejecuta todo el proceso de limpieza
def limpiar_todo(archivo_entrada, archivo_salida):
    df = cargar_datos(archivo_entrada)

    if df is None:
        return

    # Dataset original
    print("\n=== DATASET SUCIO ===")
    df.info()
    print(df.head())

    # Limpia columnas numericas que vienen como texto
    df['price'] = df['price'].apply(limpiar_precio)
    ## se usa para aplicar logica personalizadas

    if 'host_response_rate' in df.columns:
        df['host_response_rate'] = df['host_response_rate'].apply(limpiar_porcentaje)

    if 'host_acceptance_rate' in df.columns:
        df['host_acceptance_rate'] = df['host_acceptance_rate'].apply(limpiar_porcentaje)

    # Conversión de columnas de fecha a formato datatime
    columnas_fechas = ['last_scraped', 'host_since', 'first_review', 'last_review']
    for col in columnas_fechas:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    # Normalización de columnas booleanas True -> False
    columnas_bool = ['host_is_superhost','host_has_profile_pic','host_identity_verified','instant_bookable']

    for col in columnas_bool:
        if col in df.columns:
            df[col] = df[col].map({'t': True, 'f': False})

    # Inferencia de valores faltantes usando logica por fila
    df['bathrooms'] = df.apply(inferir_banos, axis=1)

    # Creación de nueva  variable categórica
    df['categoria'] = df.apply(
        lambda f: crear_categoria(f['property_type'], f['room_type']),
        axis=1
    )

    # Calcular estadisticas usando groupby
    print("\nPrecio promedio por categoría:")
    print(df.groupby('categoria')['price'].mean().round(2))

    # Selección de columnas finales pars analisis final
    columnas_finales = ['id', 'name', 'host_name', 'neighbourhood_cleansed',
    'latitude', 'longitude', 'property_type', 'room_type', 'categoria', 'accommodates', 'bathrooms', 'bedrooms',
    'beds', 'price', 'minimum_nights', 'maximum_nights','number_of_reviews', 'review_scores_rating', 'last_scraped', 'host_since', 'first_review', 'last_review' ]

    df_limpio = df[[c for c in columnas_finales if c in df.columns]].copy()

    # Eliminación de precios extremos
    df_limpio = df_limpio[
        (df_limpio['price'] >= 10) & (df_limpio['price'] <= 50000)
    ]

    # Relleno de valores numéricos faltantes usando mediana
    for col in df_limpio.select_dtypes(include=[np.number]).columns:
        df_limpio[col] = df_limpio[col].fillna(df_limpio[col].median())

    # Guardar dataset limpio en un nuevo csv
    df_limpio.to_csv(archivo_salida, index=False)

    #Muestr  Dataset limpio
    print("\n=== DATASET LIMPIO ===")
    df_limpio.info()
    print(df_limpio.head())

    print(f"\nArchivo generado: {archivo_salida}")
    print(f"Filas originales: {len(df)}")
    print(f"Filas finales: {len(df_limpio)}")


if __name__ == "__main__":
    limpiar_todo("AIRBNB.csv", "AIRBNB_limpio.csv")
