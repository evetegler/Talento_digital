# Datos del ejercicio
precio_manzana = 950       # Precio de venta por kg
precio_naranja = 1300

costo_manzana = 600        # Costo de compra por kg
costo_naranja = 850

kg_manzanas = 10           # Cantidad vendida
kg_naranjas = 15

costos_fijos = 5000        # Costos fijos del día

precio_manzanas = int(input("Ingrese precio actual de venta de manzanas:"))
precio_naranjas = int(input("Ingrese precio actual de vbenta de naranjas:"))
kilos_manzanas = int(input("Ingrese cuantos kilos vendió de manzanas:"))
kilos_naranjas = int(input("Ingrese cuantos kilos vendió de naranjas:"))

# Cálculos
ingresos_manzanas = precio_manzana * kg_manzanas
ingresos_naranjas = precio_naranja * kg_naranjas
ingresos_totales = ingresos_manzanas + ingresos_naranjas

costos_manzanas = costo_manzana * kg_manzanas
costos_naranjas = costo_naranja * kg_naranjas
costos_totales = costos_manzanas + costos_naranjas + costos_fijos

ganancia_neta = ingresos_totales - costos_totales

# Salida en consola
print("===== RESUMEN DE GANANCIAS DE LA FRUTERÍA =====")
print(f"Ingresos por manzanas:     ${ingresos_manzanas}")
print(f"Ingresos por naranjas:     ${ingresos_naranjas}")
print(f"Ingresos totales:          ${ingresos_totales}")
print("----------------------------------------------")
print(f"Costos por manzanas:       ${costos_manzanas}")
print(f"Costos por naranjas:       ${costos_naranjas}")
print(f"Costos fijos:              ${costos_fijos}")
print(f"Costos totales:            ${costos_totales}")
print("----------------------------------------------")
print(f"Ganancia neta:             ${ganancia_neta}")