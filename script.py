from datetime import datetime

# Cupos máximos por cada de vehículo
limete_cupos_normal = 5
limite_cupos_pesado = 3
limete_cupo_motocicleta = 6

# Cupos ocupados por cada de vehículo
vehiculos_ocupados_normal = 0
vehiculos_ocupados_pesados = 0
vehiculos_ocupados_motocicleta = 0

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
    print("4. Salir del sistema")

    opcion = input("Selecciona el número de una de las opciones: ")

# Codigo de la opción 1
    if opcion == "1":
        print("\nTipos de vehículos permitidos: normal, pesado, motocicleta")
        entrada_vehiculo = input("Ingrese el tipo de vehículo: ").lower()

        if entrada_vehiculo == "normal":
            if vehiculos_ocupados_normal < limete_cupos_normal:
                placa_vehiculo = input("Ahora, ingrese el número de la placa del vehículo: ").upper()
                # Verificar si la placa ya está registrada
                if placa_vehiculo in placas_ingresadas:
                    print(f"La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue #Vuelve a solicitar la placa
                else:
                    vehiculos_ocupados_normal += 1
                    placas_ingresadas.append(placa_vehiculo)
                    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    registro_vehiculo = {
                        "tipo": entrada_vehiculo,
                        "placa": placa_vehiculo,
                        "fecha_hora_entrada": fecha_hora_actual
                    }
                    vehiculos_ingresados.append(registro_vehiculo)
                    print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (normal) registrado.")
                    print(f"Cupos ocupados para 'normal': {vehiculos_ocupados_normal}/{limete_cupos_normal}")
            else:
                print("Lo sentimos, ya no hay cupos disponibles para vehículos de tipo 'normal'. :(")
                continue

        elif entrada_vehiculo == "pesado":
            if vehiculos_ocupados_pesados < limite_cupos_pesado:
                placa_vehiculo = input("Ahora, ingrese el serial de la placa del vehículo: ").upper()
               # Verificar si la placa ya está registrada
                if placa_vehiculo in placas_ingresadas:
                    print(f"La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue # Vuelve a solicitar la placa
                else:
                    vehiculos_ocupados_pesados += 1
                    placas_ingresadas.append(placa_vehiculo)
                    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    registro_vehiculo = {
                        "tipo": entrada_vehiculo,
                        "placa": placa_vehiculo,
                        "fecha_hora_entrada": fecha_hora_actual
                    }
                    vehiculos_ingresados.append(registro_vehiculo)
                    print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (pesado) registrado.")
                    print(f"Cupos ocupados para 'pesado': {vehiculos_ocupados_pesados}/{limite_cupos_pesado}")
            else:
                print("Lo sentimos, no hay cupos disponibles para vehículos de tipo 'pesado'.")
                continue

        elif entrada_vehiculo == "motocicleta":
            if vehiculos_ocupados_motocicleta < limete_cupo_motocicleta:
                placa_vehiculo = input("Ahora, ingrese el serial de la placa del vehículo: ").upper()
                # Verificar si la placa ya está registrada
                if placa_vehiculo in placas_ingresadas:
                    print(f"La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue # Vuelve a solicitar la placa
                else:
                    vehiculos_ocupados_motocicleta += 1
                    placas_ingresadas.append(placa_vehiculo)
                    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    registro_vehiculo = {
                        "tipo": entrada_vehiculo,
                        "placa": placa_vehiculo,
                        "fecha_hora_entrada": fecha_hora_actual
                    }
                    vehiculos_ingresados.append(registro_vehiculo)
                    print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (motocicleta) registrado.")
                    print(f"Cupos ocupados para 'motocicleta': {vehiculos_ocupados_motocicleta}/{limete_cupo_motocicleta}")
            else:
                print("Lo sentimos, no hay cupos disponibles para vehículos de tipo 'motocicleta'.")
                continue

        else:
            print("Error: El tipo de vehículo ingresado no es válido. Por favor, elija entre: normal, pesado, motocicleta.")

    elif opcion == '2':
        print("\n--- Estado Actual de Cupos ---")
        print(f"Tipo: Normal | Ocupados: {vehiculos_ocupados_normal}/{limete_cupos_normal} | Disponibles: {limete_cupos_normal - vehiculos_ocupados_normal}")
        print(f"Tipo: Pesado | Ocupados: {vehiculos_ocupados_pesados}/{limite_cupos_pesado} | Disponibles: {limite_cupos_pesado - vehiculos_ocupados_pesados}")
        print(f"Tipo: Motocicleta | Ocupados: {vehiculos_ocupados_motocicleta}/{limete_cupo_motocicleta} | Disponibles: {limete_cupo_motocicleta - vehiculos_ocupados_motocicleta}")

    elif opcion == '3':
        if vehiculos_ingresados:
            print("\n--- Listado de Vehículos Ingresados ---")
            for i, vehiculo in enumerate(vehiculos_ingresados, 1):
                print(f"{i}. Tipo: {vehiculo['tipo'].capitalize()}, Placa: {vehiculo['placa']}, Entrada: {vehiculo['fecha_hora_entrada']}")
        else:
            print("Aún no se ha registrado ningún vehículo en el sistema.")

    elif opcion == '4':
        print("Saliendo del sistema. ¡Gracias por usar el gestor de parqueadero!")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")