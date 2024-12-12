
posicion_actual_argentina = 0
posicion_actual_mexico = 0
posicion_actual_polonia = 0
posicion_actual_arabia = 0

print("Bienvenido al programa del Mundial de la copa 2022.")

while True:

    
    print("""Tiene 5 opciones para elegir:  
            1 - Añadir figura de Argentina
            2 - Añadir figura de Mexico
            3 - Añadir figura de Arabia Saudita
            4 - Añadir figura de Polonia 
            5 - Salir del programa.         
            """)

    opcion = int(input("Ingrese una opción: "))

    if int(opcion) == 5:
        print("Saliendo del Programa. Gracias.")
        break



    if int(opcion) == 1:
        
        total_unidades = 19

        argentina = [None] * total_unidades
        while True:
            
            if posicion_actual_argentina == total_unidades:
                print("Felicidades completaste el equipo!")
                print(f"Figuritas: {posicion_actual_argentina}/{posicion_actual_argentina}")

            figuritas = input(f"Ingrese las unidades o (exit) para salir: ")

            if figuritas.lower() == "exit":
                print("Volviendo al menu principal.")
                break

            if figuritas in argentina:
                print(f"La figurita {figuritas} ya la tenes.")
            elif posicion_actual_argentina < total_unidades:
                argentina[posicion_actual_argentina] = figuritas 
                posicion_actual_argentina += 1
                print(f"Figurita añadida: {figuritas}")
            else:
                print("Este equipo ya esta completo.")
                break

            porcentaje = (posicion_actual_argentina / total_unidades) * 100

            print(f"Figuritas de Argentina: {argentina}")

            print(f"Usted tiene completado un {porcentaje:.2f} % de las figuras de Argentina")


    elif int(opcion) == 2:

        posicion_actual = 0
        total_unidades = 19
        mexico = [None] * total_unidades

        while True:

            if posicion_actual_mexico == total_unidades:
                print("Felicidades completaste el equipo!")
                print(f"Figuritas: {posicion_actual_mexico}/{posicion_actual_mexico}")
            
            figuritas = input(f"Ingrese las unidades o (exit) para salir: ")

            if figuritas.lower() == "exit":
                print("Volviendo al menu principal.")
                break

            if figuritas in mexico:
                print(f"La figurita {figuritas} ya la tenes.")
            elif posicion_actual_mexico < total_unidades:
                mexico[posicion_actual_mexico] = figuritas 
                posicion_actual_mexico += 1
                print(f"Figurita añadida: {figuritas}")
            else:
                print("Este equipo ya esta completo.")
                break

            porcentaje = (posicion_actual_mexico / total_unidades) * 100

            print(f"Figuritas de Mexico: {mexico}")

            print(f"Usted tiene completado un {porcentaje:.2f} % de las figuras de mexico")

    elif int(opcion) == 3:
        posicion_actual = 0
        total_unidades = 19


        arabia_saudita = [None] * total_unidades    
        while True:

            if posicion_actual_arabia == total_unidades:
                print("Felicidades completaste el equipo!")
                print(f"Figuritas: {posicion_actual_arabia}/{posicion_actual_arabia}")
            
            figuritas = input(f"Ingrese las unidades o (exit) para salir: ")

            if figuritas.lower() == "exit":
                print("Volviendo al menu principal.")
                break

            if figuritas in arabia_saudita:
                print(f"La figurita {figuritas} ya la tenes.")
            elif posicion_actual_arabia < total_unidades:
                arabia_saudita[posicion_actual_arabia] = figuritas 
                posicion_actual_arabia += 1
                print(f"Figurita añadida: {figuritas}")
            else:
                print("Este equipo ya esta completo.")
                break

            porcentaje = (posicion_actual_arabia / total_unidades) * 100

            print(f"Figuritas de Arabia Saudita: {arabia_saudita}")

            print(f"Usted tiene completado un {porcentaje:.2f} % de las figuras de arabia_saudita")

    elif int(opcion) == 4:

        posicion_actual = 0
        total_unidades = 19
        polonia = [None] * total_unidades

        while True:
            
            if posicion_actual_polonia == total_unidades:
                print("Felicidades completaste el equipo!")
                print(f"Figuritas: {posicion_actual_polonia}/{posicion_actual_polonia}")
        
            figuritas = input(f"Ingrese las unidades o (exit) para salir: ")

            if figuritas.lower() == "exit":
                print("Volviendo al menu principal.")
                break

            if figuritas in polonia:
                print(f"La figurita {figuritas} ya la tenes.")
            elif posicion_actual_polonia < total_unidades:
                polonia[posicion_actual_polonia] = figuritas 
                posicion_actual_polonia += 1
                print(f"Figurita añadida: {figuritas}")
            else:
                print("Este equipo ya esta completo.")
                break

            porcentaje = (posicion_actual_polonia / total_unidades) * 100

            print(f"Figuritas de Polonia: {polonia}")

            print(f"Usted tiene completado un {porcentaje:.2f} % de las figuras de polonia")





        

        
             