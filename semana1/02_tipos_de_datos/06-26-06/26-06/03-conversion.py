#Las conversiones (int(), float(), str(),etc son como disfraces que le ponemos a los datos)

edad = 28 
edad_txt= str(edad) # Convertimos el numero a texto
print("Tengo "+edad_txt+" años.")# Concatenamos el texto


# De str a int (texto a número)
puntaje = "70"
bonus = float(puntaje) * 1.1
print("El puntaje es: ", bonus)

#De float a int (número a entero)
peso = 2.9 
peso_entero = int(peso) # Convertimos el número a entero
print("El peso es: ", peso_entero)

#booleano

print(bool(0)) # False
print(bool(1)) # True
print(bool("")) # False
print(bool("Hola")) # True
print(bool([])) # False
print(bool([1, 2, 3])) # True


