#IMPORTACIONES
import time
import os
from colorama import init, Fore

#VARIABLES
portada = """
                                 ██████████████████████████                                         
                        ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████                                  
                     ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████                                  
                     ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                     ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                     ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                     ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                     ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                      ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                       ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                       ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                       ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                       ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                       ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                       ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████                                  
                       ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████                                  
                       ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████                                  
                       ████▓▓█████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                       ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                        ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                        ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████                                  
                        ███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████████████                              
            ███████▓▓▓▓▓▓█▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                   
        █▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████                 
           ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓█████████████████████                       
                       ███▓▓▓▓▓▒▒▒▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒██████▒▓▓▒█                                
                      █▓▓█▓▓▓▓▓██▓▓▓▓▓█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓█▓▓▓▒▒▒▒▒▒█                               
                      ▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒▒▒█▓▓▒▒█                              
                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒█                              
                      █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▒▒▒▒█                              
                      █▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                               
                       █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█                                
                        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▒██                                 
                        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████                                 
                        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████                                 
                        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████                                
                        █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████████                           
                    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████████████                      
                   █▓▓▓███▒▒▒▒▒▒▒▒▒▓███████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█████████████▓▓▓                     
                   █▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                     
                    ▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                     
                    █▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                      
                     ▓▓▓▓▓████████▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▓▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                       
                     █▓▓▓▓███████████████████▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                       
                      ▓▓▓▓▓█████████▓▓▓▓█▓▓▓▓▓▓▓▓██▓▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                        
                      █▓▓▓▓████████▓▒▒▒▒█▓▓▓▓█▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█                         
                       █▓▓▓▓██████▓▒▒▒▒█▓█▓▓▓▓▓█▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███                         
                        █▓▓▓▓█▓▓▓▒▓▒▒▒▒▓▒█▒█▓█▓▓▒▒▒▒█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓█  

"""

#inicia colorama
init(autoreset=True)

clases = {}

#FUNCIONES
#PAUSA LA EJECUCION HASTA QUE SE PRESIONE ENTER
def esperar():
    input(Fore.CYAN + "Pulsa ENTER para continuar: ")
    os.system("cls" if os.name == "nt" else "clear")

#CREAR NUEVAS CLASES
def agregar_clase(nombre_clase):
    nombre_clase = nombre_clase.lower()
    if nombre_clase not in clases:
        clases[nombre_clase] = []
        print(Fore.GREEN + f"Clase '{nombre_clase}' añadida.")
    else:
        print(Fore.RED + "La clase ya existe.")
    esperar()

#CREAR NUEVOS ALUMNOS
def agregar_alumno(nombre_clase, nombre_alumno):
    nombre_clase = nombre_clase.lower()
    nombre_alumno = nombre_alumno.lower()
    if nombre_clase in clases:
        clases[nombre_clase].append(nombre_alumno)
        print(Fore.GREEN + f"Alumno '{nombre_alumno}' añadido a la clase '{nombre_clase}'.")
    else:
        print(Fore.RED + "La clase no existe.")
    esperar()

#CORRIGE AUTOMATICAMENTE LOS EXAMENES
def corregir_examen(respuestas_correctas, respuestas_alumno):
    total_preguntas = len(respuestas_correctas)
    valor_correcta = 10 / total_preguntas
    penalizacion = valor_correcta / 3
    aciertos = 0
    errores = 0
    no_respondidas = 0

    for correcta, alumno in zip(respuestas_correctas, respuestas_alumno):
        if alumno == "X":
            no_respondidas += 1
        elif correcta == alumno:
            aciertos += 1
        else:
            errores += 1
    
    nota = (aciertos * valor_correcta) - (errores * penalizacion)
    nota = max(0, round(nota, 2))
    
    print(Fore.YELLOW + f"Aciertos: {aciertos}, Errores: {errores}, No respondidas: {no_respondidas}")
    return nota

#CREA UN NUEVO EXAMEN
def nuevo_examen():
    nombre_clase = input(Fore.CYAN + "¿A qué clase corresponde el examen? ").lower()
    if nombre_clase not in clases:
        print(Fore.RED + "La clase no existe.")
        esperar()
        return
    
    try:
        num_preguntas = int(input(Fore.CYAN + "¿Cuántas preguntas tiene el examen? "))
    except ValueError:
        print(Fore.RED + "Debes introducir un número válido.")
        esperar()
        return

    respuestas_correctas = list(input(Fore.CYAN + "Introduce la secuencia de respuestas correctas (ejemplo: ABCDX): ").upper())
    
    if len(respuestas_correctas) != num_preguntas:
        print(Fore.RED + "La cantidad de respuestas no coincide con el número de preguntas.")
        esperar()
        return
    
    while True:
        nombre_alumno = input(Fore.CYAN + "Nombre del alumno (o 'fin' para terminar): ").lower()
        if nombre_alumno == "fin":
            break

        if nombre_alumno not in clases[nombre_clase]:
            print(Fore.RED + "El alumno no está en la clase.")
            continue
        
        respuestas_alumno = list(input(Fore.CYAN + f"Introduce las respuestas del alumno {nombre_alumno} (X para no contestadas): ").upper())
        
        if len(respuestas_alumno) != num_preguntas:
            print(Fore.RED + "Número de respuestas incorrecto.")
            continue
        
        nota = corregir_examen(respuestas_correctas, respuestas_alumno)
        print(Fore.GREEN + f"Nota de {nombre_alumno}: {nota}/10")
        esperar()

#MUESTRA LA PORTADA
def mostrar_portada():
    # Aquí se debe añadir el ASCII de la portada
    print(Fore.MAGENTA + "=== BIENVENIDO AL SISTEMA DE CORRECCIÓN DE EXÁMENES: GODOFREDO===")
    print(portada)
    time.sleep(2)
    esperar()

#IMPRIME EL MENU PRINCIPAL Y CONTROLA LAS OPCIONES
def menu():
    mostrar_portada()

    while True:
        print(Fore.BLUE + "\n1. Añadir clase")
        print(Fore.BLUE + "2. Añadir alumno")
        print(Fore.BLUE + "3. Nuevo examen")
        print(Fore.BLUE + "4. Salir")
        opcion = input(Fore.CYAN + "Selecciona una opción: ")

        if opcion == "1":
            clase = input(Fore.CYAN + "Nombre de la clase: ")
            agregar_clase(clase)

        elif opcion == "2":
            clase = input(Fore.CYAN + "Nombre de la clase: ")
            alumno = input(Fore.CYAN + "Nombre del alumno: ")
            agregar_alumno(clase, alumno)

        elif opcion == "3":
            nuevo_examen()

        elif opcion == "4":
            print(Fore.MAGENTA + "Saliendo...")
            esperar()
            break
        
        else:
            print(Fore.RED + "Opción no válida.")
            esperar()

menu()
