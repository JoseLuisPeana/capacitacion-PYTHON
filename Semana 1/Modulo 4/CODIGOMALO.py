import os  #operative system
import glob
import pandas as pd

donde_estoy = os.getcwd() #nos da ruta actual donde se esta ejecutando el codigo

print(donde_estoy)

ruta_carpeta = "./Sales_Data"

archivos_csv = glob.glob(os.path.join(ruta_carpeta, "*.csv"))
#glob retonar lista de caminos que coninciden con el patron que metes
cantidad_archivos = len(archivos_csv)

print(cantidad_archivos)

lista_df = []

for archivo in archivos_csv:
    df_mes = pd.read_csv(archivo)
    lista_df.append(df_mes)
    print(f"Archivo{os.path.basename(archivo)} cargando...")

df_anual = pd.concat(lista_df, ignore_index=True)

print("-----DATOS UNIDOS------ ")
print(df_anual.info())

#transformar las columnas Quantity Ordered,Price Each- a numero
# y trandormar la columna Order Date a fecha


df_anual = df_anual[df_anual["Order Date"] != "Order Date"]

df_anual["Quantity Ordered"] = pd.to_numeric(df_anual["Quantity Ordered"],errors="coerce")
df_anual["Price Each"] = pd.to_numeric(df_anual["Price Each"],errors="coerce")
#df_anual["Order ID"] = pd.to_numeric(df_anual["Order ID"],errors= "coerce")

# darle formato a order date 
# convertir  a entero  y no a float 64 la columna Order Id

# 1. Convertir Order Date a datetime
df_anual['Order Date'] = pd.to_datetime(df_anual['Order Date'], errors='coerce')

#  mostrarlo con un formato específico (ejemplo: YYYY-MM-DD)
df_anual['Order Date'] = df_anual['Order Date'].dt.strftime('%m-%d-%Y a%H:-%M-:%S', errors='coerce') 

# 2. Convertir Order Id a entero
# Primero asegúrate de que no haya valores nulos
df_anual['Order Id'] = df_anual['Order Id'].astype('Int64, errors= coerce')

df_anual["Order Date"] = pd.to_datetime(df_anual["Order Date"], errors= "coerce")

#pd.to_numeric() convierte strings como "2" o "11.95" en números reales.

print(df_anual.info())
