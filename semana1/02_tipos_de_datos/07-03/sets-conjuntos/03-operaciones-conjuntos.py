# Alimentos favoritos de estudiantes
estudiantes = {"pizza", "hamburguesa", "sushi", "tacos", "ensalada"}

# Alimentos favoritos de deportistas
deportistas = {"pollo", "ensalada", "sushi", "batidos", "huevos"}

# Intersección: alimentos que gustan a ambos grupos
comunes = estudiantes & deportistas
print("Alimentos en común:", comunes)

# Diferencia: alimentos que solo gustan a los estudiantes
solo_estudiantes = estudiantes - deportistas
print("Solo estudiantes:", solo_estudiantes)

# Diferencia: alimentos que solo gustan a los deportistas
solo_deportistas = deportistas - estudiantes
print("Solo deportistas:", solo_deportistas)

# Diferencia simétrica: alimentos exclusivos de un solo grupo (no compartidos)
exclusivos = estudiantes ^ deportistas
print("Exclusivos de un solo grupo:", exclusivos)


