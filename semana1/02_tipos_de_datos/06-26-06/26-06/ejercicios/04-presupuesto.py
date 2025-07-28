# Datos del ejercicio
rendimiento_km_por_litro = 12.5# Consumo del auto (km/l)
precio_bencina_por_litro = 1240
presupuesto = 15000

# Cálculos
litros_comprables = presupuesto / precio_bencina_por_litro
km_recorridos = litros_comprables * rendimiento_km_por_litro

# Salida en consola
print(f"Con ${presupuesto} puedes recorrer {km_recorridos:.2f} km!")
