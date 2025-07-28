import math

#Ejemplo 1: Calcular el área de un tríangulo

base = 6.9
altura = 8.2

area = (base * altura) / 2
area= round(area)
print(area)

#Redondear hacia arriba
area = math.ceil(area)
print(area)
#Redondear hacia abajo
area = math.floor(area)
print(area)

#Ejemplo 2: Encontrar la hipoteniusa de un triángulo rectángulo

"""Problema: Un árbitro corre 30 metros hacia el norte y luego 40 metros hacia el este. 
¿Cuál es la distancia directa desde el punto incial?		
"""
	
distancia_norte = 30
distancia_este = 40
hipotenusa = math.sqrt(distancia_norte**2 + distancia_este**2)
hipotenusa = round(hipotenusa, 2)
print(f"La distancia directa desde el punto inicial es: {hipotenusa} metros")

#Situación: Calcular cuántos taxis necesitas para un grupo de personas

personas = 10
capacidad_taxi = 4

operacion= personas / capacidad_taxi
print("Sin redondear:", operacion)
taxis_necesarios = math.ceil(personas / capacidad_taxi)
print("Necesitas", taxis_necesarios, "taxis.")

#Situación: Divividir porciones de una pizza
porciones_pizza = 24
personas = 7
porciones_por_persona = math.floor(porciones_pizza / personas)


print(f"Cada uno recibe {porciones_por_persona} trozos.")


"""
Un archivo de 500 MB se descarga a 6.3 MB/s.
¿Cuántos has descargado en MB en 60 segundos?
"""
velocidad_descarga = 6.3  # MB/s
tiempo_descarga = 60  # segundos
mb_descargados = math.floor(velocidad_descarga * tiempo_descarga)

print(f"En {tiempo_descarga} segundos, se han descargado {mb_descargados} MB.")



#Tiempo estimado de entrega de un paquete

tiempo_real = 3.2 # días 

entrega_round = round(tiempo_real) # 3 días
entrega_ceil = math.ceil(tiempo_real) # 4 días

print(f"Estimado cliente su entrega llegará en {entrega_ceil} días.")








