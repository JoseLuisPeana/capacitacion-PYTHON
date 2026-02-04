# ERROR 1: La suma imposible (TypeError)
# Intentar sumar texto con números sin convertir
try:
    edad = "25"
    proximo_año = edad + 1
except TypeError as e:
    print(f"Error 1 (Suma): No puedes sumar str con int. Python no sabe si quieres 26 o '251'.")
    print(f"Mensaje oficial: {e}\n")


# ERROR 2: El float con coma (ValueError)
# Muy común en México/Latinoamérica usar la coma en lugar del punto
try:
    precio = float("45,50")
except ValueError as e:
    print(f"Error 2 (Conversión): Python solo entiende el punto '.' para decimales.")
    print(f"Mensaje oficial: {e}\n")


# ERROR 3: El diccionario inexistente (KeyError)
# Intentar acceder a un dato que no definimos en el registro
usuario = {"nombre": "Angel", "puesto": "Soporte TI"}
try:
    print(usuario["sueldo"])
except KeyError as e:
    print(f"Error 3 (Diccionario): Intentaste pedir la llave {e} pero no existe en el diccionario.")
    print("Tip: Usa siempre el nombre exacto.\n")


# ERROR 4: Modificar lo inmodificable (TypeError)
# Intentar cambiar un valor en una Tupla
coordenadas_puebla = (19.04, -98.20)
try:
    coordenadas_puebla[0] = 20.00
except TypeError as e:
    print(f"Error 4 (Tupla): Las tuplas son inmutables. Si necesitas cambiar datos, usa una Lista.")
    print(f"Mensaje oficial: {e}\n")


# ERROR 5: El "None" traicionero (AttributeError / TypeError)
# Intentar operar con un dato que no llegó (común en limpieza de datos)
valor_sensor = None
try:
    resultado = valor_sensor + 10
except TypeError as e:
    print(f"Error 5 (Nulos): No puedes hacer matemáticas con 'None'.")
    print("Primero hay que limpiar los datos nulos.\n")

print("--- Fin de la demostración de errores ---")