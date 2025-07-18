

# Sistema de Gestión para Parqueadero Multivehicular

Aplicación de consola para administrar un parqueadero no gratuito, con capacidad para carga pesada, automóviles y motocicletas.

## Objetivo

Desarrollar una app que gestione entradas, salidas y cobros para tres tipos de vehículos.

## Requisitos principales

- **Parametrización inicial:**  
  Configura tarifas por hora y cantidad de cupos por categoría al iniciar la aplicación.

- **Registro de entrada:**  
  Solicita placa, fecha y hora de ingreso. Valida cupos, unicidad de placa y fechas correctas.

- **Registro de salida:**  
  Solicita fecha y hora de salida. Calcula el tiempo y el cobro. Libera el cupo ocupado.

- **Control financiero:**  
  Acumula pagos y permite consultar el total recaudado en el día.

## Tecnologías

- Aplicación por consola (sin interfaz gráfica)
- Sin base de datos, almacenamiento en memoria
- Uso de excepciones y librerías para manejo de fecha y hora (`try`, `except`, `import datetime`, etc.)

## Participantes

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/eljavi0">
        <img src="https://github.com/eljavi0.png" width="80" /><br />
        <sub><b>eljavi0</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Louis-Du">
        <img src="https://github.com/Louis-Du.png" width="80" /><br />
        <sub><b>Louis-Du</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/lukasa133">
        <img src="https://github.com/lukasa133.png" width="80" /><br />
        <sub><b>lukasa133</b></sub>
      </a>
    </td>
  </tr>
</table>
