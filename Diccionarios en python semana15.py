    # Crear un diccionario base
informacion_personal = {
    "Nombre":"David",
    "Edad":19,
    "Ciudad":"Catacocha",
    "Provincia": "Loja",
}
    # imprimimos el diccionario base
print("Diccionario base")
print(informacion_personal)
print("---------------------------------------------------------------------------------------------------")

    #Modificar el valor de la ciudad
informacion_personal["Ciudad"] = "Cuenca"

    # Agregar una clave llamada profesion con su respectivo valor
informacion_personal["profesion"] = "Estudiante"

    # Si no encuentra una clave llamada Telefono entonces añadimos una
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "09948736846"

    # Borrar el numero de telefono
del informacion_personal["Telefono"]

    # Imprimimos el diccionario modificado
print("Diccionario modificado")
print(informacion_personal)
