# **Práctica: Gestión de operaciones financieras**

## **Descripción:**

En esta práctica, desarrollarás un programa que permita gestionar una serie de operaciones financieras como compras y ventas, llevar el saldo actualizado, y consultar o restablecer las transacciones realizadas. El programa se ejecutará en un bucle donde el usuario puede ingresar comandos para realizar las distintas operaciones y recibir retroalimentación sobre el saldo actual.

## **Objetivo del ejercicio:**

Implementar un programa que gestione un conjunto de comandos básicos de compra, venta, consulta de saldo, restablecimiento de datos y finalización del programa. El objetivo es que los estudiantes desarrollen habilidades de gestión de entradas de usuario, validación de datos y manejo de flujos de control en Python.

## **Estructura del programa:**

Debes implementar las siguientes funciones y completar la lógica para que el programa funcione correctamente. Se proporciona la documentación inicial de cada función, y deberás implementar el código dentro de cada una para que el programa funcione según lo especificado.

---

## **Funciones a desarrollar:**

### 1. `comprobar_importe`

```python
def comprobar_importe(valor: str) -> bool:
    """
    Verifica si el importe proporcionado es un número válido.

    Args:
        valor (str): Cadena que representa el importe a verificar.

    Returns:
        bool: True si el valor es un número válido (positivo, negativo o con punto decimal), False en caso contrario.
    """
    pass
```

### 2. `comprobar_comando`

```python
def comprobar_comando(comando: str) -> bool:
    """
    Verifica si el comando está dentro de la lista de comandos válidos.

    Args:
        comando (str): Cadena que representa el comando ingresado por el usuario.

    Returns:
        bool: True si el comando está en la lista de comandos válidos, False en caso contrario.
    """
    pass
```

### 3. `mostrar_mensaje_error`

```python
def mostrar_mensaje_error():
    """
    Muestra el mensaje de error por entrada inválida.
    """
    pass
```

### 4. `procesar_compra`

```python
def procesar_compra(saldo: float, importe: float) -> float:
    """
    Procesa una operación de compra y actualiza el saldo restando el importe.

    Args:
        saldo (float): El saldo actual.
        importe (float): El importe a restar por la compra.

    Returns:
        float: El saldo actualizado después de realizar la compra.
    """
    pass
```

### 5. `procesar_venta`

```python
def procesar_venta(saldo: float, importe: float) -> float:
    """
    Procesa una operación de venta y actualiza el saldo sumando el importe.

    Args:
        saldo (float): El saldo actual.
        importe (float): El importe a sumar por la venta.

    Returns:
        float: El saldo actualizado después de realizar la venta.
    """
    pass
```

### 6. `mostrar_saldo`

```python
def mostrar_saldo(saldo: float, cont_compras: int, cont_ventas: int):
    """
    Muestra el saldo actual junto con el número de compras y ventas.

    Args:
        saldo (float): El saldo actual.
        cont_compras (int): Número total de compras realizadas.
        cont_ventas (int): Número total de ventas realizadas.
    """
    pass
```

### 7. `resetear_saldo`

```python
def resetear_saldo(saldo: float, cont_compras: int, cont_ventas: int) -> tuple[float, int, int]:
    """
    Resetea el saldo y las operaciones realizadas, mostrando antes el saldo anterior.

    Args:
        saldo (float): El saldo actual.
        cont_compras (int): Número total de compras realizadas.
        cont_ventas (int): Número total de ventas realizadas.

    Returns:
        tuple[float, int, int]: El nuevo saldo (0), número de compras (0) y número de ventas (0) después del reinicio.
    """
    pass
```

### 8. `recuperar_comando_e_importe`

```python
def recuperar_comando_e_importe(linea: str) -> tuple[str, str]:
    """
    Recupera el comando y, si lo hay, el importe de una línea de entrada.
    
    Args:
        linea (str): Línea de texto introducida por el usuario.

    Returns:
        tuple: El comando (str o  None) y el importe (str o None).
    
    Ejemplos:
        >>> recuperar_comando_e_importe("compra 100")
        ('compra', '100')
        
        >>> recuperar_comando_e_importe("saldo")
        ('saldo', None)

        >>> recuperar_comando_e_importe("")
        (None, None)        
    """
    pass
```

---

## **Detalles del ejercicio:**

1. **Operaciones válidas**: Los comandos válidos para el programa son:
   - **compra [importe]**: Resta el importe del saldo.
   - **venta [importe]**: Suma el importe al saldo.
   - **saldo**: Muestra el saldo actual junto con el número de compras y ventas realizadas.
   - **reset**: Restablece el saldo a cero y reinicia los contadores de compras y ventas.
   - **fin**: Finaliza el programa.

2. **Validación**: El programa debe validar tanto el comando como el importe proporcionado. Si no se ingresa un comando válido o si el importe es incorrecto, el programa debe mostrar el mensaje "*ERROR* Entrada inválida".

3. **Pistas para validar el importe**: El importe debe ser un número entero o decimal positivo o negativo. Utiliza la función `comprobar_importe()` para realizar la validación.

4. **Control del flujo**: El programa debe permitir al usuario introducir tantos comandos como quiera, hasta que introduzca el comando "fin" para finalizar el programa.

5. **Control de compras y ventas**: Cada vez que se realiza una operación de compra o venta, el saldo debe actualizarse correctamente, y los contadores de compras y ventas deben incrementarse.

---

## **Flujo del programa:**

1. El programa comienza mostrando un prompt `> ` para que el usuario ingrese un comando.
2. Tras introducir un comando, el programa valida si es correcto. Si el comando no es válido, muestra el mensaje "*ERROR* Entrada inválida".
3. Si el comando es "compra" o "venta", valida si el importe es correcto y ajusta el saldo.
4. Si el comando es "saldo", muestra el saldo actual junto con el número de compras y ventas realizadas.
5. Si el comando es "reset", muestra el saldo anterior y restablece el saldo y los contadores de compras y ventas a cero.
6. El comando "fin" termina el programa.
7. El programa debe seguir ejecutándose hasta que el usuario introduzca el comando "fin".

---

## **Ejemplo de salida del programa:**

```
> compra 100
> venta 50
> saldo
Saldo actual = -50.00 (1 compras y 1 ventas)
> venta 200
> reset
Saldo anterior = 150.00 (1 compras y 2 ventas)
> saldo
Saldo actual = 0.00 (0 compras y 0 ventas)
> fin
```

---

## **Pistas:**

1. Utiliza **tipos de datos apropiados** para manejar los valores de saldo e importe.
2. Asegúrate de **validar entradas** adecuadamente. Por ejemplo, si el usuario introduce un importe no numérico, debes manejar ese caso.
3. Utiliza **bucles y estructuras de control** para gestionar el flujo del programa.

---

## **Bonus:**
Si tienes tiempo adicional, intenta mejorar el programa añadiendo la opción de "deshacer" la última operación realizada, devolviendo el saldo y los contadores a su estado anterior.

### ** Ejemplo de salida para Bonus extra:**

```
> compra 21000
> saldo
Saldo actual = -21000.00 (1 compras y 0 ventas)
> deshacer
Última operación deshecha.
> saldo
Saldo actual = 0.00 (0 compras y 0 ventas)
> 
```
