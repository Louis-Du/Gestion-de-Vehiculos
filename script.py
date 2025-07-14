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

print("--- ¡Bienvenido al Sistema de Gestión de Parqueadero! ---")

def entradas_vehiculos(tipo_vehiculo):
    global vehiculos_ocupados_normal, vehiculos_ocupados_pesados, vehiculos_ocupados_motocicleta
    if tipo_vehiculo == "normal":
        if vehiculos_ocupados_normal < limete_cupos_normal:
            while True:
                placa_vehiculo = input("Ahora, ingrese el número de la placa del vehículo: ").upper()
                if placa_vehiculo in placas_ingresadas:
                    print(f"La placa '{placa_vehiculo}' ya se encuentra registrada en el parqueadero.")
                    continue
                else:
                    vehiculos_ocupados_normal += 1
                    placas_ingresadas.append(placa_vehiculo)
                    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    registro_vehiculo = {
                        "tipo": tipo_vehiculo,
                        "placa": placa_vehiculo,
                        "fecha_hora_entrada": fecha_hora_actual
                    }
                    vehiculos_ingresados.append(registro_vehiculo)
                    print(f"¡Éxito! Vehículo con placa '{placa_vehiculo}' (tipo: {tipo_vehiculo}) registrado.")
                    print(f"Cupos ocupados para 'normal': {vehiculos_ocupados_normal}/{limete_cupos_normal}")
                    break
        else:
            print("Lo sentimos, ya no hay cupos disponibles para vehículos de tipo 'normal'.")
    elif tipo_vehiculo == "pesado":
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
    elif tipo_vehiculo == "motocicleta":
        if vehiculos_ocupados_motocicleta < limete_cupo_motocicleta:
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
                    print(f"Cupos ocupados para 'motocicleta': {vehiculos_ocupados_motocicleta}/{limete_cupo_motocicleta}")
                    break
        else:
            print("Lo sentimos, ya no hay cupos disponibles para vehículos de tipo 'motocicleta'.")
    else:
        print("Error: El tipo de vehículo ingresado no es válido. Por favor, elija entre: normal, pesado, motocicleta.")

while True:
    try:
        print("\n--- Menú Principal ---")
        print("1. Registrar ingreso de un vehículo")
        print("2. Mostrar estado actual de los cupos")
        print("3. Ver vehículos que han ingresado")
        print("4. Registrar salida de vehículo y calcular tarifa")
        print("5. Salir del sistema")

        opcion = input("Selecciona el número de una de las opciones: ")

        if opcion == "1":
            print("\n--- Registro de Ingreso de Vehículo ---")
            print("Seleccione la opción")
            print("1. Registrar un vehículo")
            print("2. Regresar al menú principal")
            subopcion = input("Selecciona el número de una de las opciones: ")
            if subopcion == "1":
                print("\nTipos de vehículos permitidos: normal, pesado, motocicleta")
                entrada_vehiculo = input("Ingrese el tipo de vehículo: ").lower()
                entradas_vehiculos(entrada_vehiculo)
            elif subopcion == "2":
                print("Regresando al menú principal...")
                continue
            else:
                print("Opción no válida. Por favor, ingrese '1' o '2'.")
                continue

        elif opcion == "2":
            print("\n--- Estado Actual de Cupos ---")
            print(f"Tipo: Normal | Ocupados: {vehiculos_ocupados_normal}/{limete_cupos_normal} | Disponibles: {limete_cupos_normal - vehiculos_ocupados_normal}")
            print(f"Tipo: Pesado | Ocupados: {vehiculos_ocupados_pesados}/{limite_cupos_pesado} | Disponibles: {limite_cupos_pesado - vehiculos_ocupados_pesados}")
            print(f"Tipo: Motocicleta | Ocupados: {vehiculos_ocupados_motocicleta}/{limete_cupo_motocicleta} | Disponibles: {limete_cupo_motocicleta - vehiculos_ocupados_motocicleta}")

        elif opcion == "3":
            print("\n--- Listado de Vehículos Ingresados ---")
            if vehiculos_ingresados:
                for lista, vehiculo in enumerate(vehiculos_ingresados, 1):
                    print(f"{lista}. Tipo: {vehiculo['tipo'].capitalize()}, Placa: {vehiculo['placa']}, Entrada: {vehiculo['fecha_hora_entrada']}")
            else:
                print("Aún no se ha registrado ningún vehículo en el sistema.")
                continue

        elif opcion == "4":
           
                print("\n--- Registro de Salida de Vehículo ---")
                print("1. Seleccione el tipo de vehículo para calcular la tarifa:")
                print("2. Regresar al menú principal:")
                subopcion = input("Ingrese el número de la opción: ")
                try:
                    if subopcion == "1":
                        try:
                            placa_salida = input("Ingrese la placa del vehículo que desea registrar su salida: ").upper()
                            encontrado = False
                            for i, vehiculo in enumerate(vehiculos_ingresados):
                                if vehiculo['placa'] == placa_salida:
                                    fecha_hora_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    tiempo_entrada = datetime.strptime(vehiculo['fecha_hora_entrada'], "%Y-%m-%d %H:%M:%S")
                                    tiempo_salida = datetime.strptime(fecha_hora_salida, "%Y-%m-%d %H:%M:%S")
                                    duracion = (tiempo_salida - tiempo_entrada).total_seconds() / 60
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
                                        total = int(duracion) * tarifa
                                        print(f"Vehículo con placa '{placa_salida}' salió del parqueadero.")
                                        print(f"Tiempo de estadía: {int(duracion)} minutos.")
                                        print(f"Tarifa por minuto: {tarifa}")
                                        print(f"Total a pagar: {total}")
                                        del vehiculos_ingresados[i]
                                        placas_ingresadas.remove(placa_salida)
                                        encontrado = True
                                        break
                                if not encontrado:
                                    print(f"No se encontró la placa '{placa_salida}' en el registro.")
                        except ValueError:
                            print("Error al procesar la salida del vehículo.")
                    elif subopcion == "2":
                        print("Regresando al menú principal...")
                        continue
                except ValueError: 
                    print("Opción no válida. Por favor, ingrese '1' o '2'.")
                    continue

        elif opcion == "5":
            print("Saliendo del sistema. ¡Gracias por usar el gestor de parqueadero!")
            break
        
    except ValueError:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
        continue