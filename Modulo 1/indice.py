meses=["enero","febrero","marzo"]

indice = 6

if indice <len(meses):
    print(f"El mes en el índice {indice} es: {meses[indice]}")
else:
   print(f"Error: el índice {indice} no existe. La lista tiene {len(meses)} elementos.")