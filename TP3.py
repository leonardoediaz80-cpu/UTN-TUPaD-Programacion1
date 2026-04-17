#EJERCICIO 1

nombre = input("Cliente: ").strip()

while nombre == "" or not nombre.isalpha():
    print("Por favor, ingrese un nombre que contenga solo letras")
    nombre = input("Cliente: ").strip()

cantidad_str = input("Ingrese la cantidad que desea comprar: ").strip()

while not cantidad_str.isdigit() or int(cantidad_str) ==0:
    print("Ingrese un numero entero positivo mayor a cero")
    cantidad_str = input("Ingrese la cantidad que desea comprar: ").strip()

cantidad_int = int(cantidad_str)

total_sin_descuento = 0
total_con_descuento = 0.0

for i in range(1,cantidad_int+1):
    precio_str = input(f"Producto {i} - Precio: ").strip()

    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("El precio no puede ser un valor cero o menor")
        precio_str = input(f"Producto {i} - Precio: ").strip()

    precio_int = int(precio_str)        

    desc = input("Descuento (S/N): ").strip().lower()

    while desc != "s" and desc != "n":
        print("Ingrese S para Si o N para No")
        desc = input("Descuento (S/N): ").strip().lower()

    total_sin_descuento += precio_int

    if desc == "s":
        precio_final = precio_int * 0.9
    else:
        precio_final = precio_int

    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento

promedio = total_con_descuento / cantidad_int

print()
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Total con descuento: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio: ${promedio:.2f}")




#EJERCICIO 2

print("Bienvenido al Campus, por favor identifiquese")

print()

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

# INGRESO DE USUARIO Y CLAVE
while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: usuario y/o clave incorrectos")
        intentos += 1
if acceso == False:
    print("Cuenta bloqueada")

else:
    while True:
        print("\nMenu de navegacion")
        print("1) Ver estado de inscripción  ", end="")
        print("2) Cambiar clave  ", end="")
        print("3) Mostrar mensaje motivacional  ", end="")
        print("4) Salir") 
        print()
        opcion = input("Por favor elija una opcion: ")
        print()

        if not opcion.isdigit():
            print("Debe elegir un numero")
            continue
        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Debe elegir un numero entre 1 y 4")
            continue

        if opcion == 1:
            print("Inscripto")
            continue
        if opcion == 2:
            clave_nueva = input("Ingrese una nueva clave: ")
            if len(clave_nueva) < 6:
                print("Ingrese una clave con un minimo de 6 caracteres")
            else:
                confirmacion = input("Confirme su clave: ")
                if clave_nueva == confirmacion:
                    clave_correcta = clave_nueva
                    print("Cambio de clave exitoso!")
                else:
                    print("Las claves no coinciden ")
        elif opcion == 3:
            print("Vamos con todo por eso que tanto deseas!!!!")  
        elif opcion == 4:
            print("Salida del sistema...")
            break               





#EJERCICIO 3


lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

nombre = input("Ingrese el nombre del operador: ")

while nombre == "" or not nombre.isalpha():
    print("Por favor, ingrese un nombre que contenga solo letras")
    nombre = input("Operador: ").strip()

opcion = ""
while opcion != "5":
    print(f"\n--- SISTEMA DE TURNOS (Operador: {nombre}) ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        if dia == "1" or dia == "2":
            paciente = input("Nombre del paciente: ")
            if paciente.isalpha():
                if dia == "1":
                    if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                        print("Error: El paciente ya tiene turno este día.")
                    elif lunes1 == "": lunes1 = paciente
                    elif lunes2 == "": lunes2 = paciente
                    elif lunes3 == "": lunes3 = paciente
                    elif lunes4 == "": lunes4 = paciente
                    else: print("Sin cupos para el Lunes.")
                else:
                    if paciente == martes1 or paciente == martes2 or paciente == martes3:
                        print("Error: El paciente ya tiene turno este día.")
                    elif martes1 == "": martes1 = paciente
                    elif martes2 == "": martes2 = paciente
                    elif martes3 == "": martes3 = paciente
                    else: print("Sin cupos para el Martes.")
            else:
                print("Nombre inválido.")
        else:
            print("Día no válido.")


    elif opcion == "2":
        dia = input("Elegir día para cancelar (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente: ")
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""
            elif lunes2 == paciente: lunes2 = ""
            elif lunes3 == paciente: lunes3 = ""
            elif lunes4 == paciente: lunes4 = ""
            else: print("Paciente no tiene turno.")
        elif dia == "2":
            if martes1 == paciente: martes1 = ""
            elif martes2 == paciente: martes2 = ""
            elif martes3 == paciente: martes3 = ""
            else: print("Paciente no tiene turno.") 


    elif opcion == "3":
        dia = input("Ver agenda (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")  


    elif opcion == "4":
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        
        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        
        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} disponibles.")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} disponibles.")
        
        if ocupados_lunes > ocupados_martes: print("El día con más turnos es: Lunes")
        elif ocupados_martes > ocupados_lunes: print("El día con más turnos es: Martes")
        else: print("Empate en cantidad de turnos.")

print("Sistema cerrado.")       



#EJERCICIO 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0

nombre_agente = input("Ingrese su nombre de agente: ")
while not nombre_agente.isalpha():
    print("El nombre solo debe contener letras.")
    nombre_agente = input("Ingrese su nombre de agente: ")

print(f"\nHola agente {nombre_agente}..")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    if alarma and tiempo <= 3:
        print("\n¡SISTEMA BLOQUEADO! La alarma agotó el tiempo de seguridad.")
        break


    print(f"\n--- ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'} ---")
    print("1. Forzar cerradura (-20 energía, -2 tiempo)")
    print("2. Hackear panel (-10 energía, -3 tiempo)")
    print("3. Descansar (+15 energía, -1 tiempo)")
    
    opcion = input("Elija una acción: ")
    while not opcion.isdigit():
        opcion = input("Opción inválida. Elija 1, 2 o 3: ")

    
    if opcion == "1":
        
        forzar_seguidas += 1
        energia -= 20
        tiempo -= 2
        
        if forzar_seguidas >= 3:
            print("¡La cerradura se trabó por forzar repetidamente! ALARMA ACTIVADA.")
            alarma = True
        else:
           
            if energia < 40:
                print("RIESGO DE ALARMA: Energía baja.")
                num = input("Elija un número (1-3) para estabilizar: ")
                while not num.isdigit():
                    num = input("Número inválido (1-3): ")
                if num == "3":
                    alarma = True
                    print("¡Error! Activaste la alarma.")
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con éxito!")

    elif opcion == "2":
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando...")
        for i in range(1, 5):
            codigo_parcial += "A"
            print(f"Progreso: {i*25}% - Código: {codigo_parcial}")
        
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Hackeo exitoso! Una cerradura se abrió automáticamente.")
            codigo_parcial = ""

    elif opcion == "3":
        forzar_seguidas = 0 
        tiempo -= 1
        descanso = 15
        if alarma:
            descanso -= 10
            print("El estrés de la alarma dificulta el descanso.")
        
        energia += descanso
        if energia > 100:
            energia = 100
        print(f"Has descansado. Energía actual: {energia}")

    else:
        print("Opción no válida.")


print("\n--- RESULTADO FINAL ---")
if cerraduras_abiertas >= 3:
    print(f"¡VICTORIA! El Agente {nombre_agente} ha abierto la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print(f"DERROTA: Te has quedado sin {'energía' if energia <= 0 else 'tiempo'}.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueó permanentemente.")



#EJERCICIO 5    


print("--- BIENVENIDO A LA ARENA ---")

nombre_ok = False
while not nombre_ok:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        nombre_ok = True
    else:
        print("Solo nombres")

hp_jugador = 100        
hp_enemigo = 100        
pociones = 3            
ataque_pesado = 15      
ataque_enemigo = 12     
juego_activo = True     
turno_gladiador = True  

print("\n=== INICIO DEL COMBATE ===")

while hp_jugador > 0 and hp_enemigo > 0:
    if turno_gladiador:
        print(f"\n{nombre} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

   
        opcion_valida = False
        opcion = ""
        while not opcion_valida:
            opcion = input("Opción: ")
            if opcion.isdigit():
                if opcion == "1" or opcion == "2" or opcion == "3":
                    opcion_valida = True
                else:
                    print("Error: Elija 1, 2 o 3.")
            else:
                print("Error: Ingrese un número válido.")

        
        if opcion == "1":
            
            danio_final = float(ataque_pesado)
            if hp_enemigo < 20:
                danio_final = ataque_pesado * 1.5 # Golpe Crítico (Float)
                print("¡GOLPE CRÍTICO!")
            
            hp_enemigo -= int(danio_final)
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

        elif opcion == "2":
            
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                hp_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")

        elif opcion == "3":
           
            if pociones > 0:
                hp_jugador += 30
                pociones -= 1
                print(f"¡Bebiste una poción! Tu HP ahora es {hp_jugador}")
            else:
                print("¡No quedan pociones! Pierdes el turno buscando en tu mochila.")

        
        if hp_enemigo > 0:
            print(f"\n>> ¡El enemigo contraataca por {ataque_enemigo} puntos!")
            hp_jugador -= ataque_enemigo
        
        print("=== FIN DEL TURNO ===")


if hp_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")
