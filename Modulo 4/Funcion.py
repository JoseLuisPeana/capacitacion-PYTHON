import pandas as pd 
from pathlib import Path 

def concatenar_archivos_csv(carpeta_input,nombre_archivo_salida):

    path_input = Path(carpeta_input)
    path_salida = Path(nombre_archivo_salida)

    patron = "Sales_*csv"
    archivos = list(path_input.glob("Sales_*.csv"))

    if not archivos:
        print(F"No se encontraron archivos en la ruta: {path_input.absolute()}")
        print(F"Ningun archivos cumple el patro {patron}")
        return None
    print(F"Iniciando proceso de {len(archivos)} archivos...")

    lista_temporal = []
    for file in archivos:
        df_mes = pd.read_csv(file)
        lista_temporal.append(df_mes)

        print(f"  Leyendo:{file.name}")
    df_unido = pd.concat(lista_temporal, ignore_index=True)

    path_salida.parent.mkdir(parents=True, exist_ok=True)
    df_unido.to_csv(path_salida,index =False)

    return df_unido
ruta_entrada = "./Sales_Data"
name_file_output = "Reporte_Ventas_2019.csv"
mi_csv_unido = concatenar_archivos_csv(ruta_entrada, name_file_output)
