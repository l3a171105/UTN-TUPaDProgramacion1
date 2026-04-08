while True:
    nombre_operador = input("Escriba el nombre del operador: ").strip()

    if nombre_operador == "":
        print("Error: no debe estar vacio.\n")
    elif not nombre_operador.isalpha():
        print("Error: no debe tener numeros.\n")
    else:
        break

print("1. Reservar turno")
print("2. Cancelar turno (por nombre)")
print("3. Ver agenda del día")
print("4. Ver resumen general")
print("5. Cerrar sistema\n")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


while True:
    opcion = input("Elija su opción: ").strip()

    if opcion == "":
        print("Error: no debe estar vacio.\n")
    elif opcion not in ["1", "2", "3", "4", "5"]:
        print("Error: esa elección no es una opción.\n")
    else:
        if opcion == "1":
            dia_elegido = input("Elija un dia para reservar turno (1 (Lunes) o 2 (Martes)): ")

            if dia_elegido == "":
                print("Error: no debe estar vacio.\n")
            elif dia_elegido not in ["1", "2"]:
                print("Error: esa elección no es una opción.\n")   
            else:
                if dia_elegido == "1": 
                    if lunes1 != "" and lunes2 != "" and lunes3 != "" and lunes4 != "":
                        print("No hay turnos disponibles para Lunes.\n")
                        continue
                elif dia_elegido == "2": 
                    if martes1 != "" and martes2 != "" and martes3 != "":
                        print("No hay turnos disponibles para Martes.\n")
                        continue

                print("Día elegido con éxito.\n")

                nombre_paciente = input("Ahora, diga el nombre del paciente: ").strip().lower()

                if nombre_paciente == "":
                    print("Error: no debe estar vacio.\n")
                elif not nombre_paciente.isalpha():
                    print("Error: no debe tener numeros.\n")
                else:
                    if dia_elegido == "1":
                        if (nombre_paciente == lunes1 or
                            nombre_paciente == lunes2 or
                            nombre_paciente == lunes3 or
                            nombre_paciente == lunes4):
                            print("Error: este paciente ya tiene turno en Lunes.\n")
                            continue

                    elif dia_elegido == "2":
                        if (nombre_paciente == martes1 or
                            nombre_paciente == martes2 or
                            nombre_paciente == martes3):
                            print("Error: este paciente ya tiene turno en Martes.\n")
                            continue

                    if dia_elegido == "1":  
                        if lunes1 == "":
                            lunes1 = nombre_paciente
                        elif lunes2 == "":
                            lunes2 = nombre_paciente
                        elif lunes3 == "":
                            lunes3 = nombre_paciente
                        elif lunes4 == "":
                            lunes4 = nombre_paciente
                    elif dia_elegido == "2":  
                        if martes1 == "":
                            martes1 = nombre_paciente
                        elif martes2 == "":
                            martes2 = nombre_paciente
                        elif martes3 == "":
                            martes3 = nombre_paciente
                    print("Turno reservado con éxito.\n")

        elif opcion == "2":
            dia_a_cancelar = input("¿De cuál día es el turno que quiere cancelar? (1 (Lunes) o 2(Martes)): ").strip()

            if dia_a_cancelar == "":
                print("Error: no debe estar vacio.\n")
            elif dia_a_cancelar not in ["1", "2"]:
                print("Error: esa elección no es una opción.\n")
            else:
                if dia_a_cancelar == "1":  
                    if lunes1 == "" and lunes2 == "" and lunes3 == "" and lunes4 == "":
                        print("No hay turnos para cancelar en Lunes.\n")
                        continue  

                elif dia_a_cancelar == "2": 
                    if martes1 == "" and martes2 == "" and martes3 == "":
                        print("No hay turnos para cancelar en Martes.\n")
                        continue
                else:
                    nombre_cancelar = input("¿De quién es el turno que quiere cancelar?: ").strip().lower()

                    if nombre_cancelar == "":
                        print("Error: no debe estar vacio.\n")
                    elif not nombre_cancelar.isalpha():
                        print("Error: no debe tener numeros.\n")
                    else:
                        if nombre_cancelar == lunes1:
                            lunes1 = ""
                            print("Turno eliminado con exito.\n")
                        elif nombre_cancelar == lunes2:
                            lunes2 = ""
                            print("Turno eliminado con exito.\n")
                        elif nombre_cancelar == lunes3:
                            lunes3 = ""
                            print("Turno eliminado con exito.\n")
                        elif nombre_cancelar == lunes4:
                            lunes4 = ""
                            print("Turno eliminado con exito.\n")
                        else:
                            print("Error: ese paciente no tiene turno en lunes.")
                            continue
                        if nombre_cancelar == martes1:
                            martes1 = ""
                            print("Turno eliminado con exito.\n")
                        elif nombre_cancelar == martes2:
                            martes2 = ""
                            print("Turno eliminado con exito.\n")
                        elif nombre_cancelar == martes3:
                            martes3 = ""
                            print("Turno eliminado con exito.\n")
                        else:
                            print("Error: ese paciente no tiene turno en martes.")
                            continue

        elif opcion == "3":
            print("Agenda Lunes:")
            print(f"Turno 1: {lunes1 if lunes1 != '' else 'Libre'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else 'Libre'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else 'Libre'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else 'Libre'}\n")
            print("Agenda Martes:")
            print(f"Turno 1: {martes1 if martes1 != '' else 'Libre'}")
            print(f"Turno 2: {martes2 if martes2 != '' else 'Libre'}")
            print(f"Turno 3: {martes3 if martes3 != '' else 'Libre'}\n")
            
        elif opcion == "4":
            ocupados_lunes = 0
            ocupados_lunes += 1 if lunes1 != "" else 0
            ocupados_lunes += 1 if lunes2 != "" else 0
            ocupados_lunes += 1 if lunes3 != "" else 0
            ocupados_lunes += 1 if lunes4 != "" else 0
            disponibles_lunes = 4 - ocupados_lunes

            ocupados_martes = 0
            ocupados_martes += 1 if martes1 != "" else 0
            ocupados_martes += 1 if martes2 != "" else 0
            ocupados_martes += 1 if martes3 != "" else 0
            disponibles_martes = 3 - ocupados_martes

            print("Resumen General")
            print(f"Lunes: Ocupados: {ocupados_lunes}, Disponibles: {disponibles_lunes}")
            print(f"Martes: Ocupados: {ocupados_martes}, Disponibles: {disponibles_martes}")

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos ocupados: Lunes\n")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos ocupados: Martes\n")
            else:
                print("Empate: ambos días tienen la misma cantidad de turnos ocupados\n")