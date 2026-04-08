usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0

while intentos < 3:
    usuario_ingresado = input("Ingrese el usuario correcto: ").strip()
    clave_ingresada = input("Ingrese la clave correcta: ").strip()

    if usuario_ingresado == "" or clave_ingresada == "":
        print("Error: el usuario o la clave no pueden estar en blanco")
        print("")
    elif usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido.")
        print("")
        break
    else:
        intentos += 1
        print(f"El usuario o la clave son incorrectos. Intento {intentos}/3")
        print("")

if intentos < 3:
    print("1) Estado de inscripción")
    print("2) Cambiar clave")
    print("3) Mensaje")
    print("4) Salir")
    print("")
    
    while True:
        opcion = input("Elija su opción: ").strip()

        if opcion == "":
            print("Error: tiene que ser una opcion valida.")
            print("")
        elif opcion not in ["1", "2", "3", "4"]:
            print("Error: elección fuera del rango.")
            print("")    
        elif not opcion.isdigit():
            print("Error: no puede ser un numero decimal.")
            print("")    
        else:
            if opcion == "1":
                print("Inscripto.")
                print("")
            elif opcion == "2":
                nueva_clave = input("Ingrese aqui su nueva clave (minimo 6 caracteres): ").strip()
                if nueva_clave == "":
                    print("Error: no puede estar vacía.")
                    print("")
                elif len(nueva_clave) < 6:
                    print("Error: la clave debe ser mayor a 6 caracteres.")
                    print("")
                else:
                    print("Clave cambiada con exito.")   
                    print("")
            elif opcion == "3":
                print("El esfuerzo de hoy es el éxito de mañana")
                print("")
            elif opcion == "4":
                print("Saliendo...")
                exit()                  
else:
    print("Acceso denegado.")