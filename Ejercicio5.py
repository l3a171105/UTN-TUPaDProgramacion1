vida_gladiador = 100 
vida_enemigo = 100 
pociones = 3 
daño_base = 15 
daño_base_enemigo = 12 
turno_gladiador = True 

while True:
    nombre_gladiador = input("Ingrese su nombre aquí, gladiador: ").strip()

    if nombre_gladiador == "":
        print("Error: no puede estar vacio\n")
    elif not nombre_gladiador.isalpha():
        print("Error: solo se permiten letras\n")
    else:
        print("--- Empieza la batalla ---\n")
        print(f"Bienvenido, guerrero {nombre_gladiador}...\n")        
        break

while vida_enemigo > 0 and vida_gladiador > 0:
    print(f"{nombre_gladiador} (HP: {vida_gladiador} vs Espartaco (HP: {vida_enemigo}))")
    print("Elige tu acción, guerrero")
    print("1 - Ataque pesado")
    print("2 - Ráfaga veloz")
    print("3 - Curar")

    acción_elegida = input("Ingresa aqui tu acción: ").strip()

    if acción_elegida == "":
        print("Error: no puede estar vacio\n")
    elif not acción_elegida.isdigit():
        print("Error: es una opción invalida\n")
    elif acción_elegida not in ["1", "2", "3"]:
        print("Error: es una opción invalida\n")
    else:
        if acción_elegida == "1":
            if vida_enemigo < 20:
                vida_enemigo -= daño_base * 1.5
                print(f"¡Has conseguido un ataque critico! hiciste {daño_base * 1.5:.2f} de daño!!\n")
            else:
                vida_enemigo -= daño_base
                print(f"¡Atacaste al enemigo por {daño_base} puntos de daño!\n")
        if acción_elegida == "2":
            for ataques in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
            print("¡Has hecho un total de 15 de daño!\n")
        if acción_elegida == "3":
            if pociones > 0:
                pociones -= 1
                vida_gladiador += 30
                print(f"¡Has curado 30 puntos de vida tomando una poción! te quedan {pociones} pociones...\n")
            else:
                print("¡No tienes pociones!\n") 
    
    print(f"¡El enemigo atacó por {daño_base_enemigo} puntos de daño!\n")
    vida_gladiador -= daño_base_enemigo

    if vida_gladiador > 0 and vida_enemigo > 0:
        print("--- Nuevo turno ---\n")
    else:
        print("--- Fin de la partida ---\n")

if vida_gladiador > 0:
    print(f"¡VICTORIA! el ganador es... ¡{nombre_gladiador}!\n")
elif vida_gladiador <= 0:
    print("DERROTA... Has caido en combate...\n")
