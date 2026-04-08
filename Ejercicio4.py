energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
anti_spam = 0

while True:
    nombre_agente = input("Agente, ¿cuál es tu nombre?: ").strip()

    if nombre_agente == "":
        print("Error: no puede estar vacío.\n")
    elif not nombre_agente.isalpha():
        print("Error: no puede incluir un número.\n")
    else:
        break

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print("--- Menu de acciones ---")
    print("1 - Forzar cerradura (costo: -20 energía, -2 tiempo)")
    print("2 - Hackear panel (costo: -10 energía, -3 tiempo")
    print("3 - Descansar (recompensa: +15 energía, -1 tiempo; si alarma ON: -10 energía extra)")

    accion_elegida = input("Elige tu acción: ").strip()

    if accion_elegida == "":
        print("Error: no puede estar vacío.\n")
    elif not accion_elegida.isdigit():
        print("Error: opción invalida.\n")
    elif accion_elegida not in ["1", "2", "3"]:
        print("Error: opción invalida.\n")
    else:
        if accion_elegida == "1":
            energia -= 20
            tiempo -= 2
            anti_spam += 1
            if anti_spam >= 3:   
                alarma = True
                print("¡Has abierto demasiadas cerraduras seguidas! la alarma ha sonado...\n")
            if not alarma:
                if energia < 40:
                    while True:
                        numero_usuario = input("Tienes poca energía para forzar la cerradura, elige un numero 1-3: ").strip()

                        if numero_usuario == "":
                            print("Error: no puede estar vacío.\n")
                        elif not numero_usuario.isdigit():
                            print("Error: opción invalida.\n")
                        elif numero_usuario not in ["1", "2", "3"]:
                            print("Error: opción invalida.\n")
                        else:
                            if numero_usuario == "3":
                                alarma = True
                                print("La alarma ha sonado...\n")
                                break
                            else:
                                print("Te has salvado, por ahora...\n")
                                break
                if not alarma:
                    cerraduras_abiertas += 1
                    print("¡Cerradura abierta con exito!\n")
        if accion_elegida == "2":
            energia -= 10
            tiempo -= 3
            anti_spam = 0
            for letras in range(4):
                print(f"Hackeando sistema... {letras+1}")
                codigo_parcial += "A"
            if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
                print("¡Hackeo exitoso! 1 cerradura abierta...\n")
        if accion_elegida == "3":
            if alarma:
                energia -= 10
                print("Has intentado descansar con la alarma activa pero no has podido... -10 de energia...\n")
            else:
                energia += 15
                print("¡Has podido descansar y recuperar 15 de energia!\n")
            anti_spam = 0
            tiempo -= 1

if energia <= 0 or tiempo <= 0:
    print("¡Has sido atrapado! perdiste...\n")
elif alarma == True and tiempo <= 3:
    print("¡El sistema se ha bloqueado! perdiste...\n")
elif cerraduras_abiertas == 3:
    print("¡Has ganado! ¡Has abierto todas las cerraduras! eres un gran agente...")