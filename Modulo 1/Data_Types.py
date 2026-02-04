# Repaso de Data Types

'''
A continuación se veran los diferentes tipos de variales en Python.
'''

usuario_raw = "anGEL rOdriGuez Altamarina" # -> Variable de tipo String 

id_usuario = 2026 # -> Variable tipo integer. 
ventan_realizadas = 15 # -> Variable tipo integer. 

precio_producto = 450.754545435435435435 # -> Variable tipo float. 
tasa_iva = 0.16 # -> Variable tipo float 

nombre_producto = "Memoria USB 64 GB" # -> Variable tipo String
categoria = "Accesorios" # -> Variable tipo String

tiene_descuento = True # -> Variable tipo Boolean
es_importado = False # -> Variable tipo Boolean 
comentario_cleinte = None # Variable tipo noneType 

precios_semanales = [450.75, 440.0, 460.50, 450.75] # -> Variable tipo List
margen_seguridad = (100.0, 1000.0) # Variable tipo Tuple 
categorias_unicas = {"Accesorios", "Hardware", "Accesorios"} # Variable tipo Set

registro_ventas = {
    "id": id_usuario,
    "producto": nombre_producto,
    "monto": precio_producto,
    "aplico_descuento" : tiene_descuento,
    "comentario": comentario_cleinte, 
    "precio_semanal": precios_semanales, 
} # Variable tipo Dictionary

print(f"Analizando comentario del producto: {registro_ventas['precio_semanal']}")

if registro_ventas["comentario"] is None: 
    print("Alerta: el registro no tiene comentarios del cliente")

total = precio_producto * (1 + tasa_iva)
print(f"El total con IVA es: ${total} ({total:.2f})")

producto_1 = {
    "id": 101, 
    "nombre": "Teclado Inalámbrico",
    "precio": 850, 
    "en oferta": False, 
    "comentarios": None
}

inventario = [
    producto_1, # -> Diccionari 1
    {"id": 102, "nombre": "Mouse", "precio": 450.0, "en_oferta":True, "comentarios": "Buen producto"}, # -> Diccionario 2
    {"id": 103, "nombre": "Monitor", "precio": 3500.0, "en_oferta": False, "comentarios": None} # -> Diccionario 3
]
total_precios= 0
for p in inventario: 
    total_precios += p["precio"]

promedio_precios = total_precios / len(inventario)
print(f"El precio promedio del inventario es: ${promedio_precios:.2f}")

sin_comentarios = 0
for p in inventario:
    if p["comentarios"] is None: 
        sin_comentarios += 1

print(f"Analisis terminado: \n- Producto por revisar: {sin_comentarios} productos sin comentarios")
print(f"Precio promedio: ${promedio_precios:.2f} \n precio total: ${total_precios:.2f}")
