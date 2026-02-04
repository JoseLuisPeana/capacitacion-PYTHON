precios = ["100", "200", "no hay precio", "400"]

for p in precios:
    try:
        total = float(p) * 1.16
        print(f"El precio con IVA es: ${total:.2f}")
    except ValueError:
        print(f"Error: el valor '{p}' no es un número válido.")
     