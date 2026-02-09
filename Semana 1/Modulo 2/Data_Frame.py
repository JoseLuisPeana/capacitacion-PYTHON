import pandas as pd

int_values =[1,2,3,4,5]
text_values = ['alpha','beta','gamma','delta','epsilon']
float_values = [0.0,0.25,0.5,0.75,1.0]

df = pd.DataFrame(    #se crea el DataFrame
    {
        'Integers': int_values,
        'Text': text_values,
        'Floats': float_values
    }   
)

df_2 = pd.DataFrame(    #se crea otro DataFrame
    [[1.2],[4,5],[7,8]],

    index = ["cobra","viper","sidewinder"],
    columns =["max_speed","shield"]
)


sales_superstore = pd.read_csv('Superstore Sales Dataset.csv')

print(f"DataFrame 1:\n{df}\n")    
print(f"DataFrame 2:\n{df_2}\n")    
print(f"Sales Superstore Sales DataFrame:\n{sales_superstore}\n")
  
numero_filas = 5
filas = sales_superstore.head(1)  #muestra las primeras filas del DataFrame
fila_slice = sales_superstore[:numero_filas]  #muestra un slice de filas del DataFrame

#print(f"Estas son las primeras{numero_filas}filas del DataFrame:\n{filas}\n")

#ultimaas_filas = sales_superstore.tail(10)  #muestra las ultimas filas del DataFrame 

#ultimas_slice = sales_superstore[-10:]  #muestra un slice de las ultimas filas del DataFrame

#ultimas_slice_file = sales_superstore[10]
ultimas_slice = sales_superstore.tail(10)

print(f"Estas son las últimas 10 filas del DataFrame:\n{ultimas_slice}") 
#NAN significa Not a Number (No es un número) y se utiliza para representar valores faltantes o indefinidos en un DataFrame de pandas.
#NAT significa Not a Time (No es un tiempo) y se utiliza para representar valores de tiempo faltantes o indefinidos en un DataFrame de pandas.
 

# ================== TAREA ==================

# Seleccionamos las 3 columnas que queremos mostrar
columnas = ["Order ID", "Product Name", "Sales"]

# -------------------------------------------------
# 1️⃣ PRIMEROS 3 RENGLONES
# Usamos .loc para obtener filas 0 a 2 (primeros 3)
# y solo las columnas definidas arriba

primeros_3 = sales_superstore.loc[0:2, columnas]

print("\nPrimeros 3 renglones:")
print(primeros_3)
columnas = ["Order ID", "Product Name", "Sales"]
# -------------------------------------------------
# 2️⃣ RENGLONES DEL MEDIO

# Obtenemos el índice del centro del DataFrame
medio = len(sales_superstore) // 2

# Tomamos 5 filas alrededor del centro (2 arriba y 2 abajo)
enmedio = sales_superstore.loc[medio-2:medio+2, columnas]

print("\nRenglones del medio:")
print(enmedio)

# -------------------------------------------------
# 3️⃣ ÚLTIMOS 4 RENGLONES

# .tail(4) obtiene las últimas 4 filas
# Luego seleccionamos solo las columnas deseadas
ultimos_4 = sales_superstore.tail(4)[columnas]

print("\nÚltimos 4 renglones:")
print(ultimos_4)

# -------------------------------------------------
# 4️⃣ EJEMPLO USANDO .at

# .at sirve para obtener UN SOLO VALOR específico
# Aquí sacamos la venta (Sales) de la primera fila

print("\nEjemplo usando .at (venta del primer registro):")
print(sales_superstore.at[0, "Sales"])
