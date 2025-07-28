"""
CADENAS:
- Manipulación de texto: Nombres, direcciones, mensajes.
- Interacción con usuarios: Inputs, formularios.
- Procesamiento de datos: Limpieza y análisis de archivos.
https://www.w3schools.com/python/python_ref_string.asp
"""

# 1. CONCATENACIÓN Y FORMATEO (F-STRINGS)

nombre = "Eve"
saludo = "¡Hola, " + nombre + "! Bienvenido."
print("Concatenación:", saludo)

# Usando f-strings para interpolar variables (método moderno y recomendado)
producto = "camiseta"
precio = 19.55
resumen_producto = f"El {producto} cuesta ${precio}"
#print(resumen_producto)
resumen_producto = f"El {producto} cuesta ${precio:.1f}"
#print(resumen_producto)


# 2. ACCESO, SLICING E INVERSIÓN DE CADENAS
# El slicing permite extraer subcadenas usando la sintaxis [inicio:fin:paso].

texto = "Aprendiendo Python"
print(f"Extrayendo primer caracter de \"{texto}\": {texto[0]}") # 'A' (El primer caracter)
print(f"Extrayendo ultimo caracter de \"{texto}\": {texto[-1]}")
print(f"Slicing básico: {texto[0:11]}")
print(f"Slicing hasta el final: {texto[12:]}")
print(f"Slicing con paso: {texto[::2]} ")
print(f"Invertir una cadena: {texto[::-1]}")


# 3. MÉTODOS DE TRANSFORMACIÓN
texto = "buenas TardEs"
# .upper(), .lower(), .title() para cambiar capitalización 

print("Mayusculas:", texto.upper())
print("Minusculas:", texto.lower())
print("Capitalización:", texto.capitalize())
print("Título:", texto.title())

# .strip() para eliminar espacios en blanco al inicio y al final

usuario_input = "   se usa en limpieza de datos    "
print(f" Sin limpiar: '{usuario_input}'")
print(f"Limpio con strip(): '{usuario_input.strip()}'")


# 4. BÚSQUEDA Y REEMPLAZO : Para encontrar, contar o sustituir partes de una cadena

# Verificar si una subcadena está presente en otra cadena.
texto = "Python es genial"
condicion = "es" in texto
if(condicion):
    print(type(condicion))
    print(condicion)
    print("Python sí es genial!")

print("Java" not in texto)

# Ejemplo: Buscar si un correo es gmail o no
email = "usuario@gmail.com"
es_gmail = "@gmail.com" in email
print(f"¿El email es de Gmail?: {es_gmail}")


# .find() para obtener el índice de la primera aparición de una subcadena
# Devuelve -1 si no la encuentra.
indice_arroba = email.find("@")
print(f"El @ está en el indice: {indice_arroba}")

#Metodo Len() para contar caracteres
#len () para obtener la longitud de una cadena
password = "abcxy"
print(len(password))  # Devuelve 5
if len(password) < 6:
    print("La contraseña es demasiado corta. Debe tener al menos 6 caracteres.")    
    print(f"Longitud de la contraseña: {len(password)}")
     
