usuario_raw =       "anGEL rOdriGuez Altamarina"         # -> Variable de tipo String 

nombre_limpio = usuario_raw.strip().title() #-> Quita espacios y pone mayusculas al inicio de cada palabra

usuario_minusculas = usuario_raw.strip().lower() #-> Convierte todo a minusculas
usuario_mayusculas = usuario_raw.strip().upper() #-> Convierte todo a mayusculas

print(f"Usuario original: '{usuario_raw}'")
print(f"Usuario limpio(Usando tittle): '{nombre_limpio}'")  #title() pone mayusculas al inicio de cada palabra
print(f"Usuario en minusculas: '{usuario_minusculas}'")
print(f"Usuario en mayusculas: '{usuario_mayusculas}'")

precio = "1500.5"
impuesto = 1.16

total = precio + impuesto  # Concatenación de strings
total_2 = precio + "100"  # Concatenación de strings

concatenar  = "banana" + "del " + "chocolate"


print(f"Total (concatenación): {total_2}")
print(f"Concatenación de strings: {concatenar}")
print(f"El tipo de 'precio' es: {type(precio)}") 