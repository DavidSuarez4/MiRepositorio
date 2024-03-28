#Crear el archivo my_notes.txt
my_notes = open("my_notes.txt", "w")
#Creando nuevas lineas
my_notes.write("Liinea 1: Mi nombre es David \n")
#crear varias lineas
lineas = ["Linea 2: Tengo 19 años \n", "Linea 3: Me gusta programar\n"]

# Añadir las nuevas lineas
my_notes.writelines(lineas)

#usar el primer metodo para imprimir el resultado
print("-------------------------------------------")
print("-------------------------------------------")
print("Usando el primer metodo: .read()")
my_notes = open("my_notes.txt", "r")
print(my_notes.read())
my_notes.close()

#usar el segundo metodo para imprimir el resultado
print("-------------------------------------------")
print("-------------------------------------------")
print("Usando el segundo metodo: .readlines()")
my_notes = open("my_notes.txt", "r")
for linea in my_notes.readlines():
    print(linea.rstrip("\n"))
    my_notes.close()
