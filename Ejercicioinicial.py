import os
#ejemplos de python
"""
print('hola')
print(2+3)
x = 15
if x > 0:
    print('Es mayor de cero')
else:
    print('error')
print("----------------------------------------------------------------------------------------------------------------")2
contador = 1
while contador <= 5:
    print("contador vale", contador)
    contador = contador + 1

print("----------------------------------------------------------------------------------------------------------------")
conteoenrango = [1,2,3,4,5,6,7,8,9,10]
for conteo in conteoenrango:
        print(conteo)
print("----------------------------------------------------------------------------------------------------------------")
conteoenrango.extend([11,12,13,14,15])
for conteo in conteoenrango:
        print(conteo)


print("----------------------------------------------------------------------------------------------------------------")

def sumamasiva(numeros):
    total = 0
    for numero in numeros:
        if isinstance(numero, int):
            total = numero + total
     
    return total

totales = [1,"cosa",3,"cosa",5,"cosa"]
imp = sumamasiva(totales);
print(imp)



usuario = input("Introduce tu nombre de usuario: ")

print("Hola ", usuario, "Bienvenido" )

"""
tareas = []
def showmenu():
    print("1 - Mostrar lista de tareas")
    print("2 - Agregar Tareas")
    print("3 - Eliminar Tareas")
    print("4 - Editar Tareas")
    print("5 - Salir")
def showtareas():
    linea = 0
    print("Tareas disponibles: ")
    for tarea in tareas:
        linea = linea + 1
        print( linea, " - ", tarea)

opcion = 0
os.system("cls")
showmenu()
opcion = int( input("Elija la opcion deseada: ") )
while opcion != "5":
    try:
        os.system("cls")
        match opcion:
            case "1":
                showtareas()
            case "2":
                tarea = input("Escriba la tarea que desea agregar: ")
                tareas.extend([tarea])
            case "3":
                os.system("cls")
                showtareas()
                op3 = int( input("¿ Que tarea desea eliminar ?: ") )
                op3 = op3 - 1
                eliminado = tareas.pop(op3)
                print( "Se elimino la tarea: ", eliminado)
            case "4":
                showtareas()
                op4 = int( input("¿ Que tarea desea editar ?: ") )
                tareas[op4] = input("Escriba la tarea: ")
            case "5":
                exit
    except:
        print("Selecione una opcion valida...")
    opcion2 = input("Presione ""Enter"" para continuar . . .")
    os.system("cls")
    showmenu()
    opcion = input("Elija la opcion deseada: ")
