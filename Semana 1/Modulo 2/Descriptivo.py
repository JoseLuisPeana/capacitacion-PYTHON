import pandas as pd
sales_superstore = pd.read_csv('Superstore Sales Dataset.csv')

#print(sales_superstore.info())  #muestra información general sobre el DataFrame

#print(sales_superstore.describe())  #muestra estadísticas descriptivas del DataFrame

#print(sales_superstore.describe(include = "object","string"))  #muestra estadísticas descriptivas del DataFrame incluyendo datos no numéricos


solo_ventas = sales_superstore[["Sales","city", "customer Name"]]  #selecciona las columnas 'Sales', 'city', y 'customer Name' del DataFrame
print(solo_ventas.head()) #muestra las primeras filas del DataFrame solo_ventas
print(solo_ventas.tail())  #muestra las últimas filas del DataFrame solo_ventas

print(solo_ventas.describe(include=["object","string"]))  #muestra estadísticas CUALITATIVA 
print(solo_ventas.describe())  #muestra estadísticas CUANTITATIVA   


print(solo_ventas.loc[30])  #Esto devuelve un dataframe con la fila en el índice 0

print([solo_ventas.iloc[30]])  #Esto devuelve el valor en la fila 0 y la columna 2 del DataFrame solo_ventas

df_2 = pd.DataFrame(    #se crea otro DataFrame
    [[1.2],[4,5],[7,8]],

    index = ["cobra","viper","sidewinder"],
    columns =["max_speed", "shield"]
)

print(sales_superstore.loc[200,"Product Name"])  #Esto devuelve el valor en la fila 200 y la columna 'product Name' del DataFrame sales_superstore
print(sales_superstore.iloc[0].at["Customer Name"])  #Esto devuelve el valor en la fila 0 y la columna 'customer Name' del DataFrame sales_superstore
    #.at = ""es similar a .loc pero se usa para acceder a un solo valor en un DataFrame   

                                            