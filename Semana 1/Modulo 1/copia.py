# =========================================
# DEMOSTRACIÓN DE COPIA DE LISTAS EN PYTHON
# =========================================

# Creamos una lista original
original = [1, 2, 3]

# -------------------------------------------------
# COPIA FALSA (referencia)
# Aquí NO se crea una nueva lista.
# copia_falsa solo apunta al MISMO espacio en memoria que original.

copia_falsa = original

# Agregamos un valor a copia_falsa
copia_falsa.append(100)

print("Después de modificar copia_falsa:")
print(f"Original: {original}")
print(f"Copia falsa: {copia_falsa}")

# -------------------------------------------------
# COPIA REAL
# .copy() crea una lista completamente nueva en memoria

copia_real = original.copia()
    
# Agregamos un valor solo a la copia real
copia_real.append(200)

print("\nDespués de modificar copia_real:")
print(f"Original: {original}")
print(f"Copia real: {copia_real}")
