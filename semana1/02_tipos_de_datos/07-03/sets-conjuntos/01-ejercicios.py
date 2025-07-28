# Crear el set con los días de la semana
dias = {"lunes", "martes", "miércoles", "jueves", "viernes", "sábado"}

# Añadir "domingo" si no está presente
if "domingo" not in dias:
    dias.add("domingo")

# Eliminar un día cualquiera (por ejemplo, "miércoles")
dias.remove("lunes")  # O usa discard() si no estás seguro de que existe

# Verificar si "lunes" está en el set
if "lunes" in dias:
    print("Lunes está en el set.")
else:
    print("Lunes NO está en el set.")

# Mostrar el set final (opcional)
print(dias)
