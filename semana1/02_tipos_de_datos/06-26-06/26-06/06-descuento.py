# Datos del ejercicio
precio_pantalon = 4599
precio_zapatos = 7999

descuento_ropa = 20     # en porcentaje
descuento_calzado = 15  # en porcentaje

# Cálculo de precios finales
precio_final_pantalon = precio_pantalon * (1 - descuento_ropa / 100)
precio_final_zapatos = precio_zapatos * (1 - descuento_calzado / 100)

# Cálculo de ahorro
ahorro_pantalon = precio_pantalon - precio_final_pantalon
ahorro_zapatos = precio_zapatos - precio_final_zapatos
ahorro_total = ahorro_pantalon + ahorro_zapatos

# Resultados en consola
print(f"Precio final del pantalón: ${precio_final_pantalon:.2f}")
print(f"Precio final de los zapatos: ${precio_final_zapatos:.2f}")
print(f"¡Ahorraste ${ahorro_total:.2f} en total!")
