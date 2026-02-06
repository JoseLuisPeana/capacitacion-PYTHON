producto = {
    "sku": "AC12345",
    "nombre": "Auriculares Bluetooth",
    "stock": 150,
    "precio":1200.50
}

busqueda = "descuento"
 #valor = producto[busqueda]  # Esto causará un KeyError ya que "descuento" no es una clave en el diccionario
valor_get = producto.get(busqueda)
valor_get = producto.get(busqueda, 0)
valor_get = producto.get(busqueda,"No disponible")

print(f"Valor usando get: '{valor_get}'")  # Esto no lanzará un error
  # Usando get para evitar el error

ventas_semana = [
    {"dia": "Lunes", "monto": 150.0},
    {"dia": "Martes", "monto": 200.0},
    {"dia": "Miércoles", "monto": 180.0}
]

indice_dia = 2
indice_monto = 2
venta_1 = ventas_semana[indice_dia]["monto"["indicie_monto"]]  # Accediendo al monto del miércoles
dia_venta = ventas_semana[indice_dia]["dia"]

#print(f"Venta {indice_monto + 1} del: ${venta_1}")

total_lunes = sum(ventas_semana[0],["monto"])

venta_max_martes = max(ventas_semana[1]["monto"])

venta_total_por_semana = 0

for venta in ventas_semana:
    venta_total_por_semana += sum(dia["monto"])   