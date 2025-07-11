from datetime import datetime

# Cupos máximos por tipo de vehículo
cupos_normal = 5
cupos_pesado = 3
cupos_motocicleta = 6

# Cupos ocupados por tipo de vehículo
ocupados_normal = 0
ocupados_pesado = 0
ocupados_motocicleta = 0

vehiculos_ingresados = []
placas_ingresadas = []

print("--- ¡Bienvenido al Sistema de Gestión de Parqueadero! ---")

while True:
    print("\n--- Menú Principal ---")
    print("1. Registrar ingreso de un vehículo")
    print("2. Mostrar estado actual de los cupos")
    print("3. Ver vehículos que han ingresado")
    print("4. Salir del sistema")

    opcion = input("Por favor, seleccione una opción (1-4): ")

    if opcion == '1':
        print("\nTipos de vehículos que puede ingresar: normal, pesado, motocicleta")
        entrada_vehiculo = input("Ingrese el tipo de vehículo (ej: normal, pesado, motocicleta): ").lower()

        if entrada_vehiculo == "normal":
            if ocupados_normal < cupos_normal:
                placa_vehiculo = input("Ahora, ingrese el serial de la placa del vehículo: ").upper()
                if placa_vehiculo in placas_ingresadas:
                    print(f"¡Atención! La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue
                ocupados_normal += 1
                placas_ingresadas.append(placa_vehiculo)
                fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                registro_vehiculo = {
                    "tipo": entrada_vehiculo,
                    "placa": placa_vehiculo,
                    "fecha_hora_entrada": fecha_hora_actual
                }
                vehiculos_ingresados.append(registro_vehiculo)
                print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (normal) registrado.")
                print(f"Cupos ocupados para 'normal': {ocupados_normal}/{cupos_normal}")
            else:
                print("Lo sentimos, no hay cupos disponibles para vehículos de tipo 'normal'.")
        elif entrada_vehiculo == "pesado":
            if ocupados_pesado < cupos_pesado:
                placa_vehiculo = input("Ahora, ingrese el serial de la placa del vehículo: ").upper()
                if placa_vehiculo in placas_ingresadas:
                    print(f"¡Atención! La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue
                ocupados_pesado += 1
                placas_ingresadas.append(placa_vehiculo)
                fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                registro_vehiculo = {
                    "tipo": entrada_vehiculo,
                    "placa": placa_vehiculo,
                    "fecha_hora_entrada": fecha_hora_actual
                }
                vehiculos_ingresados.append(registro_vehiculo)
                print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (pesado) registrado.")
                print(f"Cupos ocupados para 'pesado': {ocupados_pesado}/{cupos_pesado}")
            else:
                print("Lo sentimos, no hay cupos disponibles para vehículos de tipo 'pesado'.")
        elif entrada_vehiculo == "motocicleta":
            if ocupados_motocicleta < cupos_motocicleta:
                placa_vehiculo = input("Ahora, ingrese el serial de la placa del vehículo: ").upper()
                if placa_vehiculo in placas_ingresadas:
                    print(f"¡Atención! La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue
                ocupados_motocicleta += 1
                placas_ingresadas.append(placa_vehiculo)
                fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                registro_vehiculo = {
                    "tipo": entrada_vehiculo,
                    "placa": placa_vehiculo,
                    "fecha_hora_entrada": fecha_hora_actual
                }
                vehiculos_ingresados.append(registro_vehiculo)
                print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (motocicleta) registrado.")
                print(f"Cupos ocupados para 'motocicleta': {ocupados_motocicleta}/{cupos_motocicleta}")
            else:
                print("Lo sentimos, no hay cupos disponibles para vehículos de tipo 'motocicleta'.")
        else:
            print("Error: El tipo de vehículo ingresado no es válido. Por favor, elija entre: normal, pesado, motocicleta.")

    elif opcion == '2':
        print("\n--- Estado Actual de Cupos ---")
        print(f"Tipo: Normal | Ocupados: {ocupados_normal}/{cupos_normal} | Disponibles: {cupos_normal - ocupados_normal}")
        print(f"Tipo: Pesado | Ocupados: {ocupados_pesado}/{cupos_pesado} | Disponibles: {cupos_pesado - ocupados_pesado}")
        print(f"Tipo: Motocicleta | Ocupados: {ocupados_motocicleta}/{cupos_motocicleta} | Disponibles: {cupos_motocicleta - ocupados_motocicleta}")

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