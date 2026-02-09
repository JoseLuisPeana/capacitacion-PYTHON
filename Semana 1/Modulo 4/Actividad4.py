import os
import glob
import pandas as pd

def concatenar_csv_simple(carpeta, archivo_salida):
    # Buscar todos los archivos que empiecen con Sales_
    archivos = glob.glob(os.path.join(carpeta, "Sales_*.csv"))

    if not archivos:
        print("No se encontraron archivos.")
        return None

    # Leer y juntar todos los CSV en uno solo
    df_unido = pd.concat([pd.read_csv(a) for a in archivos])

    # Guardar el resultado
    df_unido.to_csv(archivo_salida, index=False)
    print("Archivo guardado:", archivo_salida)

    return df_unido

# Ejemplo de uso
mi_csv_unido = concatenar_csv_simple("./Sales_Data", "Reporte_Ventas_2019.csv")