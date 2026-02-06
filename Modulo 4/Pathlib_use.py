import pandas  as pd    
from pathlib import Path  
 


donde_estoy = Path.cwd()

ruta_carpeta = Path('./Sales_Data')

archivos_csv = list(ruta_carpeta.glob("Sales_*.csv"))

print(f"Se encontraron {len(archivos_csv)} archivos para procesos")

lista_df = []
for archivo in archivos_csv:
    df_mes = pd.read_csv(archivo)
    lista_df.append(df_mes)

    print(F"Archivo{archivo.name} cargando ...")

df_anual = pd.concat(lista_df, ignore_index= True)
print ("datos unidos")
print(df_anual.info())