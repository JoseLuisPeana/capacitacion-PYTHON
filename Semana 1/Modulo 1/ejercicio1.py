libreria = {
    "nombre": "Lectura Infinita",
    "sucursales": ["Centro", "Norte", "Online"],
    "catalogo": [
        {
            "id": "LIB001",
            "titulo": "El Quijote",
            "detalles": {"autor": "Cervantes", "paginas": 863},
            "precios": [15.0, 12.5, 10.0]  # Tapa dura, blanda, digital
        },
        {
            "id": "LIB002",
            "titulo": "Cien años de soledad",
            "detalles": {"autor": "Garcia Marquez", "paginas": 471},
            "precios": [20.0, 18.0] # Tapa dura, blanda
        },
        {
            "id": "LIB003",
            "titulo": "1984",
            "detalles": {"autor": "George Orwell"}, # Falta 'paginas'
            "precios": [12.0, 9.5, 7.0]
        }
    ]
}
nombre_libreria = libreria.get("nombre", "Libreria Generica") # Obtener nombre o valor por defecto
print(f"Libreria generica!")

autor_segundo_libro = libreria["catalogo"][1]["detalles"]["autor"] # Acceder al autor del segundo libro

print(f"El autor del segundo libro es: {"Garcia Marquez"}\n")

precio_final = libreria["catalogo"][0]["precios"][2] * 1.16  # Precio digital del primer libro con IVA 
print(f"El precio final del primer libro (tapa blanda con IVA) es: ${precio_final:.2f}")
print(f"precio_final")


L = [1,2,3,4,5] #
#acceder a -1  en negativo

print(L[:-1])  # Imprime 5
#print(L[])

#