from datetime import datetime

# Cupos máximos por cada tipo de vehículo
limete_cupos_normal = 5
limite_cupos_pesado = 3
limete_cupo_motocicleta = 6

# Cupos ocupados por cada tipo de vehículo
vehiculos_ocupados_normal = 0
vehiculos_ocupados_pesados = 0
vehiculos_ocupados_motocicleta = 0

# Se establece la tarifa por minutos de cada tipo de vehículos
tarifa_normal = 160
tarifa_pesado = 200
tarifa_motocicleta = 141

# Listas de vehículos ingresados y placas
vehiculos_ingresados = []
placas_ingresadas = []

# Menú principal
print("--- ¡Bienvenido al Sistema de Gestión de Parqueadero! ---")

while True:
    print("\n--- Menú Principal ---")
    print("1. Registrar ingreso de un vehículo")
    print("2. Mostrar estado actual de los cupos")
    print("3. Ver vehículos que han ingresado")
    print("4. Registrar salida de vehículo y calcular tarifa")
    print("5. Salir del sistema")

    opcion = input("Selecciona el número de una de las opciones: ")

# Codigo de la opción 1
    if opcion == "1":
        print("\n--- Registro de Ingreso de Vehículo ---")
        print("Seleccione la opción")
        print("1. Registrar un vehículo")
        print("2. Regresar al menú principal")
        
        if opcion == "1":
            print("\nTipos de vehículos permitidos: normal, pesado, motocicleta")
            entrada_vehiculo = input("Ingrese el tipo de vehículo: ").lower()

            def entradas_vehiculos(vehiculos_ocupados, tipo_vehiculo): # Definimos la función para registrar el ingreso de vehículos
                while vehiculos_ocupados < limete_cupos_normal:
                    placa_vehiculo = input("Ahora, ingrese el número de la placa del vehículo: ").upper()
                    # Verificar si la placa ya está registrada
                    if placa_vehiculo in placas_ingresadas:
                        print(f"La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                        continue #Vuelve a solicitar la placa
                    else:
                        vehiculos_ocupados += 1
                        placas_ingresadas.append(placa_vehiculo)
                        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        registro_vehiculo = {
                            "tipo": entrada_vehiculo,
                            "placa": placa_vehiculo,
                            "fecha_hora_entrada": fecha_hora_actual
                        }
                        vehiculos_ingresados.append(registro_vehiculo)
                        print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (tipo: {tipo_vehiculo}) registrado.")
                        print(f"Cupos ocupados para 'normal': {vehiculos_ocupados}/{limete_cupos_normal}")
                        break
                    
        elif opcion == "2":
            print("Regresando al menú principal...")
            continue
        
        else:
            print(f"Lo sentimos, ya no hay cupos disponibles para vehículos de tipo {entrada_vehiculo}")
            continue

        if entrada_vehiculo == "normal":
            entradas_vehiculos(vehiculos_ocupados_normal, "normal")

        elif entrada_vehiculo == "pesado":
            entradas_vehiculos(vehiculos_ocupados_pesados, "pesado")

        elif entrada_vehiculo == "motocicleta":
            entradas_vehiculos(vehiculos_ocupados_motocicleta, "motocicleta")

        else:
            print("Error: El tipo de vehículo ingresado no es válido. Por favor, elija entre: normal, pesado, motocicleta.")


    elif opcion == "2": # Mostrar estado actual de los cupos
            print("\n--- Estado Actual de Cupos ---")
            print(f"Tipo: Normal | Ocupados: {vehiculos_ocupados_normal}/{limete_cupos_normal} | Disponibles: {limete_cupos_normal - vehiculos_ocupados_normal}")
            print(f"Tipo: Pesado | Ocupados: {vehiculos_ocupados_pesados}/{limite_cupos_pesado} | Disponibles: {limite_cupos_pesado - vehiculos_ocupados_pesados}")
            print(f"Tipo: Motocicleta | Ocupados: {vehiculos_ocupados_motocicleta}/{limete_cupo_motocicleta} | Disponibles: {limete_cupo_motocicleta - vehiculos_ocupados_motocicleta}")

    elif opcion == '3': # Ver vehiculos ingresados
        if vehiculos_ingresados:
            print("\n--- Listado de Vehículos Ingresados ---")
            for lista, vehiculo in enumerate(vehiculos_ingresados, 1):
                print(f"{lista}. Tipo: {vehiculo['tipo'].capitalize()}, Placa: {vehiculo['placa']}, Entrada: {vehiculo['fecha_hora_entrada']}")
        else:
            print("Aún no se ha registrado ningún vehículo en el sistema.")
            continue

    elif opcion == '4': # Registrar salida de vehículo y calcular tarifa
        print("\n--- Registro de Salida de Vehículo ---")
        print("1. Seleccione el tipo de vehículo para calcular la tarifa:")
        print("2. Regresar al menú principal:")
        opcion = input("Ingrese el número de la opción: ")
        if opcion == "1":
            placa_salida = input("Ingrese la placa del vehículo que desea registrar su salida: ").upper()
            for vehiculo in vehiculos_ingresados:
                if vehiculo['placa'] == placa_salida:
                    fecha_hora_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    tiempo_entrada = datetime.strptime(vehiculo['fecha_hora_entrada'], "%Y-%m-%d %H:%M:%S")
                    tiempo_salida = datetime.strptime(fecha_hora_salida, "%Y-%m-%d %H:%M:%S")
                    duracion = (tiempo_salida - tiempo_entrada).total_seconds() / 60
                    del vehiculos_ingresados[vehiculo]
                else:
                    print(f"No se encontró la placa '{placa_salida}' en el registro.")
                    continue
        elif opcion == "2":
            print("Regresando al menú principal...")

            continue    
            
        else:
            print("Opción no válida. Por favor, ingrese '1' o '2'.")
            continue
    elif opcion == '5':
        print("Saliendo del sistema. ¡Gracias por usar el gestor de parqueadero!")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")
        

    