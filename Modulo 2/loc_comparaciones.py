import pandas as pd

sales_superstore = pd.read_csv('Superstore Sales Dataset.csv')

solo_ventas = sales_superstore[["Sales","City", "Customer Name"]]  #selecciona las columnas 'Sales', 'city', y 'customer Name' del DataFrame

ventas_altas = solo_ventas["Sales"] > 500  #filtra las filas donde la columna 'Sales' es mayor a 500

print("Ventas altas (Sales > 500):")
print(ventas_altas)

print("+" * 90) 

ventas_altas_filtradas = solo_ventas.loc[ventas_altas] #filtra las filas del DataFrame solo_ventas utilizando el DataFrame ventas_altas como filtro

print(solo_ventas.loc[ventas_altas, "Customer Name"])  #muestra los nombres de los clientes con ventas mayores a 500

ventas_altas_loc = solo_ventas.loc[solo_ventas["Sales"] > 500, ["Customer Name"]] #filtra las filas del DataFrame solo_ventas donde la columna 'Sales' es mayor a 500 usando .loc

print(ventas_altas_loc)

ventas_cliente_filtro = solo_ventas.loc[(solo_ventas["Sales"] > 500) & (solo_ventas["Customer Name"] == "Sylvia Foulston")
                                | (solo_ventas["Sales"] < 50) & (solo_ventas["Customer Name"] == "Brosina Hoffman")]  #filtra las filas del DataFrame solo_ventas donde la columna 'Sales' es mayor a 500 y el 'Customer Name' es 'Sylvia Foulston' o donde la columna 'Sales' es menor a 50 y el 'Customer Name' es 'Brosina Hoffman'
print("*" * 90)
print(ventas_cliente_filtro)
    

df = sales_superstore = pd.read_csv('Superstore Sales Dataset.csv')

resultado = df[(df["Category"] == "Furniture") & (df["State"] == "Kentucky") & (df["Sales"] > 500)]

print(resultado)

# iloc se usa para acceder a filas y columnas por posición entera (índice)
# loc se usa para acceder a filas y columnas por etiquetas (nombres)
#.at se usa para acceder a un solo valor en un DataFrame utilizando etiquetas de fila y columna


solo_ventas.iloc[0]  #Esto devuelve un dataframe con la fila en la posición 0
solo_ventas.iloc[-1]  #Esto devuelve un dataframe con la última fila
sales_superstore.iloc[10].at["Customer Na"]