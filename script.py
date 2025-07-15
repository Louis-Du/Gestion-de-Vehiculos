from datetime import datetime

# Establecemos los cupos máximos por cada tipo de vehículo
limite_cupos_normal = 50
limite_cupos_pesado = 30
limite_cupo_motocicleta = 60

# Establecemos los cupos ocupados por cada tipo de vehículo
vehiculos_ocupados_normal = 0
vehiculos_ocupados_pesados = 0
vehiculos_ocupados_motocicleta = 0

# Se establece la tarifa a cobrar por minutos de cada tipo de vehículos
tarifa_normal = 160
tarifa_pesado = 200
tarifa_motocicleta = 141

# Listas de vehículos ingresados, placas y los vehículos que salen
vehiculos_ingresados = []
placas_ingresadas = []
vehiculos_salidos = []

# Acumulador de dinero total
total_recaudado = 0

print("--- ¡Bienvenido al Sistema de Gestión de Parqueadero! ---") # se muestra el mensaje de bienvenida a comienzo del programa

def entradas_vehiculos(tipo_vehiculo): # Definimos la función encargada de registrar el ingreso de los vehículos y establecemos el parametro de tipo de vehículo
    global vehiculos_ocupados_normal, vehiculos_ocupados_pesados, vehiculos_ocupados_motocicleta, registro_vehiculo, vehiculos_ingresados # "Global" permitimos que las variables dentro de la función afecte fuera de ella
    if tipo_vehiculo == "normal": # Si el tipo de vehículo que se ingresa en el parametro es normal
        if vehiculos_ocupados_normal < limite_cupos_normal:
            while True:
                placa_vehiculo = input("Ahora, ingrese el número de la placa del vehículo: ").upper()
                if placa_vehiculo in placas_ingresadas:
                    print(f"La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue # Si la placa que ingresa el usuario ya se encuentra en el sistema se muestra un mensaje y vuelve a solicitar la placa
                else:
                    vehiculos_ocupados_normal += 1
                    placas_ingresadas.append(placa_vehiculo)
                    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Obtenemos la fecha y hora de la entrada haciendo uso de la función datetime seguido del metodo .now() que se encarga de obtener la información actual y el metodo .strftime() que convierte el objeto de la fecha y hora en un string
                    registro_vehiculo = {
                        "tipo": tipo_vehiculo,
                        "placa": placa_vehiculo,
                        "fecha_hora_entrada": fecha_hora_actual
                    }
                    vehiculos_ingresados.append(registro_vehiculo) # Se crea un diccionario con la información del vehículo ingresado (tipo, placa y fecha/hora de entrada) y se guarda en la lista de vehículos ingresados
                    print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (tipo: {tipo_vehiculo}) registrado.")
                    print(f"Cupos ocupados para 'normal': {vehiculos_ocupados_normal}/{limite_cupos_normal}")
                    break
        else:
            print("Lo sentimos, ya no hay cupos disponibles para vehículos de tipo 'normal'.") # En caso de que no haya vehículos disponibles se muestra un mensaje al usuario
            
    elif tipo_vehiculo == "pesado": # Si el tipo de vehículo que ingresa en el parametro es pesado se repite el proceso anterior
        if vehiculos_ocupados_pesados < limite_cupos_pesado:
            while True:
                placa_vehiculo = input("Ahora, ingrese el número de la placa del vehículo: ").upper()
                if placa_vehiculo in placas_ingresadas:
                    print(f"La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue
                else:
                    vehiculos_ocupados_pesados += 1
                    placas_ingresadas.append(placa_vehiculo)
                    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    registro_vehiculo = {
                        "tipo": tipo_vehiculo,
                        "placa": placa_vehiculo,
                        "fecha_hora_entrada": fecha_hora_actual
                    }
                    vehiculos_ingresados.append(registro_vehiculo)
                    print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (tipo: {tipo_vehiculo}) registrado.")
                    print(f"Cupos ocupados para 'pesado': {vehiculos_ocupados_pesados}/{limite_cupos_pesado}")
                    break
        else:
            print("Lo sentimos, ya no hay cupos disponibles para vehículos de tipo 'pesado'.")

    elif tipo_vehiculo == "motocicleta": # Lo mismo sucede si el vehículo es una motocicleta
        if vehiculos_ocupados_motocicleta < limite_cupo_motocicleta:
            while True:
                placa_vehiculo = input("Ahora, ingrese el número de la placa del vehículo: ").upper()
                if placa_vehiculo in placas_ingresadas:
                    print(f"La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue
                else:
                    vehiculos_ocupados_motocicleta += 1
                    placas_ingresadas.append(placa_vehiculo)
                    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    registro_vehiculo = {
                        "tipo": tipo_vehiculo,
                        "placa": placa_vehiculo,
                        "fecha_hora_entrada": fecha_hora_actual
                    }
                    vehiculos_ingresados.append(registro_vehiculo)
                    print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (tipo: {tipo_vehiculo}) registrado.")
                    print(f"Cupos ocupados para 'motocicleta': {vehiculos_ocupados_motocicleta}/{limite_cupo_motocicleta}")
                    break
        else:
            print("Lo sentimos, ya no hay cupos disponibles para vehículos de tipo 'motocicleta'.")

    else:
        print("Error: El tipo de vehículo ingresado no es válido. Por favor, elija entre: normal, pesado, motocicleta.") # Mensaje de error si se ingresa un vehículo no válido

while True:
    try:
        print("\n--- Menú Principal ---") # Se muestra el menú principal del sistema con las opciones disponibles
        print("1. Registrar ingreso de un vehículo")
        print("2. Mostrar estado actual de los cupos")
        print("3. Ver vehículos que han ingresado")
        print("4. Registrar salida de vehículo y calcular tarifa")
        print("5. Ver historial de entrada y salida de vehículos")
        print("6. Salir del sistema")

        opcion = input("Selecciona el número de una de las opciones: ")

        if opcion == "1": # Opción 1 registrar ingreso de un vehículo
            print("\n--- Registro de Ingreso de Vehículo ---")
            print("Seleccione la opción")
            print("1. Registrar un vehículo")
            print("2. Regresar al menú principal")
            subopcion = input("Selecciona el número de una de las opciones: ") #  Nos aseguramos de que el usuario quiere registra un vehículo o prefiere regresar al menú principal

            if subopcion == "1": # En caso de que se asegure de que el usuario quiere registrar un vehículo se procede con el proceso
                print("\nTipos de vehículos permitidos: normal, pesado, motocicleta")
                entrada_vehiculo = input("Ingrese el tipo de vehículo: ").lower()
                entradas_vehiculos(entrada_vehiculo) # Invocamos la función entradas_vehiculos e ingresamos en el parametro el tipo de vehículo

            elif subopcion == "2": # Si el usuario ingresa esta opción se regresa al menú principal
                print("Regresando al menú principal...")
                continue

            else:
                print("Opción no válida. Por favor, ingrese '1' o '2'.")
                continue

        elif opcion == "2": # Opción 2 mostrar estado actual de los cupos
            print("\n--- Estado Actual de Cupos ---")
            print(f"Tipo: Normal | Ocupados: {vehiculos_ocupados_normal}/{limite_cupos_normal} | Disponibles: {limite_cupos_normal - vehiculos_ocupados_normal}")
            print(f"Tipo: Pesado | Ocupados: {vehiculos_ocupados_pesados}/{limite_cupos_pesado} | Disponibles: {limite_cupos_pesado - vehiculos_ocupados_pesados}")
            print(f"Tipo: Motocicleta | Ocupados: {vehiculos_ocupados_motocicleta}/{limite_cupo_motocicleta} | Disponibles: {limite_cupo_motocicleta - vehiculos_ocupados_motocicleta}")
            # Mostramos el estado actual de los cupos ocupados y disponibles por cada tipo de vehículo

        elif opcion == "3": # Opción 3 ver vehículos que han ingresado
            print("\n--- Listado de Vehículos Ingresados ---")
            if vehiculos_ingresados:
                for indice, vehiculo in enumerate(vehiculos_ingresados, 1): # Usamos enumerate para mostrar el índice y la información en el diccionario de cada vehículo ingresado
                    print(f"{indice}. Tipo: {vehiculo['tipo'].capitalize()}, Placa: {vehiculo['placa']}, Entrada: {vehiculo['fecha_hora_entrada']}") # Invocamos el dicionario y mostramos la información que contiene donde la primera clave es el tipo, la segunda la placa y la tercera la fecha/hora de entrada. El metodo .capitalize() se usa para que la primera letra del tipo de vehículo esté en mayúscula
            else:
                print("Aún no se ha registrado ningún vehículo en el sistema.") # En caso de que no haya vehículos ingresados se muestra un mensaje al usuario y 
                continue

        elif opcion == "4": # Opción 4 registrar salida de vehículo y calcular tarifa
                print("\n--- Registro de Salida de Vehículo ---")
                print("1. Seleccione el tipo de vehículo para calcular la tarifa:")
                print("2. Regresar al menú principal:")
                subopcion = input("Ingrese el número de la opción: ") # Nos aseguramos de que el usuario quiere registrar la salida de un vehículo o prefiere regresar al menú principal
                
                if subopcion == "1": # En caso de que se asegure de que el usuario quiere registrar la salida de un vehículo se procede con el proceso
                    placa_salida = input("Ingrese la placa del vehículo que desea registrar su salida: ").upper()
                    for i, vehiculo in enumerate(vehiculos_ingresados): # Recorremos la lista de vehiculos_ingresados que contiene un diccionario con la información por cada vehículo ingresado

                        if vehiculo['placa'] == placa_salida: # En caso de que haya un diccionario en la lista que contenga la misma placa que se ingresó en la salida se procede con el siguiente proceso
                            fecha_hora_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Obtenemos la fecha y hora de la salida haciendo uso de la función datetime seguido del metodo .now() que se encarga de obtener la información actual y el metodo .strftime() que convierte el objeto de la fecha y hora en un string 
                            tiempo_entrada = datetime.strptime(vehiculo['fecha_hora_entrada'], "%Y-%m-%d %H:%M:%S") # Ahora convertimos el string de la fecha y hora de nuevo en un objeto 
                            tiempo_salida = datetime.strptime(fecha_hora_salida, "%Y-%m-%d %H:%M:%S") # Hacemos lo mismo con la fecha y hora de salida convirtiendola de un string a un objeto
                            duracion = (tiempo_salida - tiempo_entrada).total_seconds() / 60 # Calculamos la duración de la estadia del vehículo restando tiempo_salida menos tiempo_entrada y convirtiendo el resultado a segundos con .total_seconds() y luego dividiendolo entre 60.
                            tipo = vehiculo['tipo']
                            if tipo == "normal":
                                tarifa = tarifa_normal
                                vehiculos_ocupados_normal -= 1
                            elif tipo == "pesado":
                                tarifa = tarifa_pesado
                                vehiculos_ocupados_pesados -= 1
                            elif tipo == "motocicleta":
                                tarifa = tarifa_motocicleta
                                vehiculos_ocupados_motocicleta -= 1
                            else:
                                tarifa = 0

                            total = int(duracion) * tarifa # Convertimos duración a un entero y lo multiplicamos por la tarifa a cobrar por el tipo de vehículo para asignarlo a total
                            print(f"Vehículo con placa '{placa_salida}' salió del parqueadero.")
                            print(f"Tiempo de estadía: {int(duracion)} minutos.")
                            print(f"Tarifa por minuto: {tarifa}")
                            print(f"Total a pagar: {total}")
                            total_recaudado += total # se asigna y se suma todas las tarifas recaudadas
                            
                                
                            # Guardar registro de salida
                            vehiculo['fecha_hora_salida'] = fecha_hora_salida # Añadimos una nueva clave al diccionario de vehiculo y le asignamos fecha_hora_salida
                            vehiculos_salidos.append(vehiculo) # El diccionario vehiculo se le asigna a la lista vehiculos_salidos
                            vehiculos_ingresados.pop(i) # Se elimina el vehiculo en la lista de vehiculos_ingresados mediante su indice
                            placas_ingresadas.remove(placa_salida) # Elimina placa_salida de la lista placa_ingresadas

                            break
                    else:
                        print(f"No se encontró la placa '{placa_salida}' en el registro.")
                elif subopcion == "2":
                    print("Regresando al menú principal...")
                    continue
                else: 
                    print("Opción no válida. Por favor, ingrese '1' o '2'.")
                    continue
                
        elif opcion == "5": # Opción 5 ver historial de entrada y salida de vehículos
            print("\n--- Historial de Entrada y salida de Vehículos ---")
            if vehiculos_ingresados:
                print("Vehículos actualmente ingresados")
                for i, vehiculo in enumerate(vehiculos_ingresados, 1): # Recorremos la lista de vehiculos_ingresados que contiene un diccionario con la información por cada vehículo ingresado
                    print(f"{i}. Tipo: {vehiculo['tipo'].capitalize()} | "
                            f"Placa: {vehiculo['placa']} | "
                            f"Entrada: {vehiculo['fecha_hora_entrada']}") # Mostramos la información de cada vehículo ingresado donde la primera clave es el tipo, la segunda la placa y la tercera la fecha/hora de entrada. El metodo .capitalize() se usa para que la primera letra del tipo de vehículo esté en mayúscula
            else:
                print("No hay vehículos ingresados")
            
            if vehiculos_salidos:
                print("\nVehículos que ya salieron:")
                for i, vehiculo in enumerate(vehiculos_salidos, 1):
                    print(f"{i}. Tipo: {vehiculo['tipo'].capitalize()} | "
                            f"Placa: {vehiculo['placa']} | "
                            f"Salida:  {vehiculo['fecha_hora_salida']}") # Recorremos la lista de vehiculos_salidos que contiene un diccionario con la información por cada vehículo salido
            else:
                print("Aún no hay salidas registradas.")
            
            print(f"En total se ha recaudado {total_recaudado} pesos")
                    
                             
        elif opcion == "6": # Opción 6 salir del sistema
            print("Saliendo del sistema. ¡Gracias por usar el gestor de parqueadero!")
            break
        
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número del 1 al 6.") # En caso de que el usuario ingrese un valor no válido se muestra un mensaje y se vuelve a solicitar una opción
        continue