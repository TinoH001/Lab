

# README - Laboratorio 1: 

## 1. Integrantes
* **Nombre:**  -  **RUT:** 

---

## 2. Especificación de los Algoritmos y Desarrollo
El programa ha sido desarrollado en Python 3.x bajo una estructura modular, implementando manualmente cada algoritmo de transformación para cumplir con la prohibición estricta de usar librerías de conversión automática.

Se implementaron diccionarios globales para optimizar la lógica de conversión y filtrado:
### Estructuras de Soporte (Diccionarios)
 * **Mapeo de Prefijos (`prefix_base`)**: Asocia los símbolos (`*`, `&`, `#`, `!`) con sus bases numéricas (2, 8, 10, 16) y viceversa. 
 * **Validación de Bases (`filter`)**: Define los caracteres permitidos para cada sistema, permitiendo que el programa detecte el fin de una secuencia y descarte el "ruido" automáticamente.
 * **Traducción Hexadecimal (`hexadecimal_numbers` y `numbers_hexadecimal`)**: Proporciona el mapeo bidireccional entre valores decimales (10-15) y caracteres (A-F), fundamental para la base 16 (Hexadecimal).

### Funciones Principales
* **`Read_file`**: Se encarga de la apertura y lectura del archivo de texto, asegurando que el flujo de datos sea procesado correctamente.
* **`Filter`**: Recorre el flujo de caracteres para identificar los valores numéricos mediante sus prefijos (*, &, #, !) e ignora el "ruido" o caracteres que no corresponden a la base detectada.
* **`BaseX_to_decimal_and_ASCII`**: Realiza la conversión manual a base 10 utilizando el método de potencias (dígito * base^exponente). Además, valida que el equivalente decimal esté en el rango 32-126 y utiliza la función `chr()` para convertir cada valor válido en su respectivo carácter ASCII, construyendo así el mensaje final.
* **`Decimal_to_BI_OCT_HEX`**: Implementa el algoritmo de divisiones sucesivas para transformar los valores decimales a la base de visualización (2, 8, 10 o 16) elegida por el usuario.
* **`Show_results`**: Genera la interfaz de salida que muestra la tabla de valores extraídos y el mensaje final decodificado segun dicta el laboratorio.
* **`Main`**: Orquestador principal que solicita la base de visualización, valida la entrada del usuario y dirige la ejecución de los módulos anteriores.

---

## 3. Supuestos Utilizados
* **Uso de Funciones Base**: Se emplea `int()` únicamente para el casteo de tipos (string a entero) y `chr()` para la obtención del carácter ASCII final. Se respeta estrictamente la prohibición de utilizar `int(x, base)` o cualquier función de conversión de base automatizada.
* **Continuidad de Datos**: Se asume que el archivo de entrada contiene una cadena continua de caracteres sin necesidad de espacios o saltos de línea para su procesamiento.
* **Rango de Filtrado**: Se asume que cualquier valor cuyo equivalente decimal sea menor a 32 o mayor a 126 es "ruido" y no formará parte del mensaje decodificado.
* **Prefijos Obligatorios**: Se asume que todo dato válido debe comenzar estrictamente con uno de los prefijos definidos (*, &, #, !) para ser identificado por el sistema.
* **Ruta de Lectura de Archivo**: Se asume que la estructura de directorios del evaluador coincide con la del entorno de desarrollo, existiendo una carpeta llamada `Encriptados` que contiene varios`Examples.txt`. De lo contrario, el evaluador deberá modificar manualmente la ruta que se le pasa a la función `Read_file` dentro del bloque `main`
---

