---
title: Separa responsabilidades.

description: Separa responsabilidades.

authors:
    - Eduardo Fernandez.

date: 2024-10-08

tags:
  - python
  - test
  - SRP
  - Buenas prácticas
---

# Principio de responsabilidad única (SRP) en un programa sencillo.

## 1. Concepto: Separación de responsabilidades
En un programa bien estructurado, es importante dividirlo en **tres fases principales** para que sea fácil de entender, probar y mantener. Estas fases son:

1. **Entrada y validación de datos**: Esta fase se encarga de capturar los datos necesarios para resolver el problema y validar que cumplan con los requisitos (por ejemplo, asegurarse de que sean números y no letras, que los números sean positivos, etc.).

2. **Procesamiento (lógica de negocio)**: Es la fase en la que realmente se resuelve el problema utilizando los datos que ya han sido validados. Es importante que la lógica del problema esté separada de la entrada y de la salida para que se pueda probar de forma independiente.

3. **Salida o presentación de resultados**: Después de calcular el resultado, este se presenta al usuario de forma comprensible. Esto podría ser un mensaje en consola o cualquier otro formato de salida.

## 2. Analogía: Un restaurante
Para que entiendan mejor este concepto, usaremos una analogía con un restaurante:

- **Entrada y validación de datos (Tomar la orden)**: Imagina que un cliente llega al restaurante y el camarero toma su orden. El camarero no acepta cualquier cosa; verifica que el cliente haya pedido algo que esté en el menú. Si el cliente pide algo que no existe, el camarero le pide que elija otra cosa. Esta fase es la **validación de la entrada**.

- **Procesamiento o lógica de negocio (Preparación de la comida)**: Una vez que el camarero tiene una orden válida, se la lleva al cocinero. El cocinero no se preocupa por cómo se tomó la orden o quién la pidió. Su responsabilidad es **preparar la comida** basada en la orden recibida.

- **Salida o presentación de resultados (Servir la comida)**: Cuando la comida está lista, el camarero se la lleva al cliente y se la presenta en la mesa. Aquí no se hace ningún cálculo ni verificación, simplemente se entrega el resultado.

De la misma manera, en un programa bien organizado, cada fase debe estar separada y tener una única responsabilidad.

## 3. Ejemplo práctico: Calcular el área de un rectángulo

Vamos a usar el ejemplo de calcular el área de un rectángulo:

#### 3.1. Código inicial (todo junto en una sola función):

```python
def calcular_area_rectangulo():
    # Entrada de datos
    ancho = float(input("Introduce el ancho del rectángulo: "))
    alto = float(input("Introduce el alto del rectángulo: "))

    # Proceso de cálculo
    area = ancho * alto

    # Salida
    print(f"El área del rectángulo es: {area}")
```

Este código mezcla la entrada, el procesamiento y la salida en una sola función, lo cual dificulta su prueba y mantenimiento. Vamos a separarlo en tres funciones distintas.

#### 3.2. Fase 1: **Entrada y validación de datos**

```python
def obtener_datos_rectangulo():
    """Obtiene y valida los datos de entrada del rectángulo."""
    ancho = None
    alto = None

    # Validar que el ancho y el alto sean números positivos
    while ancho is None:
        try:
            ancho = float(input("Introduce el ancho del rectángulo (positivo): "))
            if ancho <= 0:
                print("El valor debe ser positivo.")
                ancho = None
        except ValueError:
            print("Por favor, introduce un número válido.")

    while alto is None:
        try:
            alto = float(input("Introduce el alto del rectángulo (positivo): "))
            if alto <= 0:
                print("El valor debe ser positivo.")
                alto = None
        except ValueError:
            print("Por favor, introduce un número válido.")

    return ancho, alto
```

- **Qué hace esta función**: Toma la entrada del usuario y valida que sean números positivos. Si el usuario introduce un valor inválido, le pide que vuelva a intentarlo.

#### 3.3. Fase 2: **Procesamiento (lógica de negocio)**

```python
def calcular_area(ancho, alto):
    """Calcula el área de un rectángulo dado su ancho y alto."""
    return ancho * alto
```

- **Qué hace esta función**: Toma dos números (ancho y alto) y calcula el área del rectángulo. No tiene idea de cómo se obtuvieron estos números ni de cómo se va a mostrar el resultado. Esto es lo que se conoce como **lógica de negocio**.

#### 3.4. Fase 3: **Salida o presentación de resultados**

```python
def mostrar_resultado(area):
    """Muestra el resultado del área en la salida estándar."""
    print(f"El área del rectángulo es: {area}")
```

- **Qué hace esta función**: Muestra el resultado en la consola. No realiza cálculos ni toma datos de entrada.

#### 3.5. Función principal que une las tres fases

```python
def main():
    ancho, alto = obtener_datos_rectangulo()  # Entrada y validación de datos
    area = calcular_area(ancho, alto)         # Procesamiento o lógica de negocio
    mostrar_resultado(area)                   # Presentación de resultados

if __name__ == "__main__":
    main()
```

- **Qué hace esta función**: Conecta las tres fases en un solo flujo. Primero, obtiene y valida los datos, luego calcula el área y finalmente muestra el resultado.

#### 3.6. Probar la lógica de negocio
Aunque todas las fases se pueden probar, en esta etapa nos vamos a centrar en la **lógica de negocio** (`calcular_area`). Esto es importante porque queremos asegurarnos de que la función resuelve correctamente el problema sin preocuparnos por cómo se obtuvieron los datos ni cómo se muestra el resultado.

##### 3.6.1. Pruebas de la lógica de negocio (calcular_area)
Podemos probar la función `calcular_area` con un archivo de pruebas que no dependa de la entrada y salida:

```python
# test_calcular_area.py

# Importar la función calcular_area desde el archivo donde la definiste
from main import calcular_area  # Ajusta el nombre del archivo si es necesario

def test_area_positiva():
    assert calcular_area(5, 10) == 50, "Error: el área de 5x10 debería ser 50"

def test_area_cero():
    assert calcular_area(0, 10) == 0, "Error: el área de 0x10 debería ser 0"

def test_area_valores_negativos():
    # Dependiendo de la lógica de negocio, puedes decidir si aceptar o no valores negativos
    assert calcular_area(-5, 10) == -50, "Error: el área de -5x10 debería ser -50"
```

##### 3.6.2. Explicación del propósito de estas pruebas
Al probar la lógica de negocio, no tenemos que preocuparnos por si el usuario introduce letras en lugar de números o si el resultado se muestra correctamente. Nos centramos en verificar que, si se pasan datos válidos a la función `calcular_area`, esta devuelve el resultado correcto. Una vez que esta fase funcione bien, podemos estar seguros de que la parte central del programa está correcta.

## 4. Aplicación en desarrollo web
Es importante que los alumnos comprendan que esta separación de fases se aplica a aplicaciones más grandes, como las aplicaciones web:

1. **Entrada y validación de datos**: Se realiza en el **frontend** (por ejemplo, en el navegador), validando que los datos sean correctos antes de enviarlos al servidor. Esto es similar a la fase de entrada y validación de datos en nuestro ejemplo.

2. **Procesamiento o lógica de negocio**: El **backend** (servidor) recibe los datos validados y realiza el procesamiento necesario (por ejemplo, calcular valores, interactuar con bases de datos, etc.). Esto es análogo a la fase de cálculo de área en nuestro ejemplo.

3. **Salida o presentación de resultados**: Los resultados se devuelven al **frontend** para ser presentados al usuario de manera adecuada. El frontend solo se encarga de mostrar los resultados, no de realizar cálculos ni validaciones complejas.

¡Exacto! Lo que estás describiendo está relacionado directamente con el **Principio de Responsabilidad Única** (Single Responsibility Principle, SRP), que es uno de los principios fundamentales en el desarrollo de software.

## 5. Principio de Responsabilidad Única (SRP)
El SRP establece que **cada módulo, clase o función debe tener una única responsabilidad** y, por lo tanto, debe hacer solo **una cosa**. En otras palabras, cada componente de un programa debe tener una **única razón para cambiar**. Si un módulo o función se modifica por múltiples motivos, significa que está asumiendo más de una responsabilidad, lo cual lo hace más complejo de entender y mantener.

Aplicar este principio tiene varias ventajas:

1. **Facilita la lectura y comprensión**: Cada función tiene un propósito claro, por lo que es más fácil para otros (o para ti mismo en el futuro) entender lo que hace cada parte del código.

2. **Mejora la mantenibilidad**: Si hay un error o se necesita realizar un cambio, solo se modifica la función responsable de esa tarea específica, lo que minimiza el riesgo de introducir nuevos errores en otras partes del código.

3. **Facilita las pruebas**: Al tener funciones más pequeñas y específicas, se pueden crear pruebas unitarias más simples y precisas para verificar el comportamiento de cada función de manera independiente.

### 5.1. Relación del SRP con la separación de fases

En el ejemplo de separar las fases de un programa (entrada, procesamiento y salida), estamos aplicando este principio:

1. La función `obtener_datos_rectangulo` **solo** se encarga de **recoger y validar la entrada de datos**. No realiza cálculos ni muestra resultados.

2. La función `calcular_area` **solo** se encarga de **realizar el cálculo** del área. No se preocupa por cómo se obtuvieron los datos ni cómo se mostrará el resultado.

3. La función `mostrar_resultado` **solo** se encarga de **mostrar el resultado** al usuario. No recoge datos ni realiza cálculos.

Cada una de estas funciones tiene una **única responsabilidad**, y cada una tendría **una sola razón para cambiar**. Por ejemplo:

- Si cambia la forma en la que se muestran los resultados (por ejemplo, de consola a una ventana gráfica), **solo** se modificaría la función `mostrar_resultado`.
- Si se cambia la lógica para calcular el área (por ejemplo, calcular el área de otro tipo de figura), **solo** se modificaría la función `calcular_area`.
- Si se quiere cambiar la forma de capturar los datos (por ejemplo, de entrada en consola a un formulario en una aplicación web), **solo** se modificaría la función `obtener_datos_rectangulo`.

### 5.2. Analogía con el SRP en la cocina (Restaurante)
Volviendo a la analogía del restaurante:

1. **El camarero** tiene la responsabilidad de **tomar la orden** y verificar que el cliente haya elegido algo del menú. Si se cambia el menú (por ejemplo, se agrega un nuevo platillo), solo el camarero tiene que conocer estos cambios y su forma de tomar la orden.

2. **El cocinero** se encarga de **preparar la comida** basándose en la orden recibida. No le importa cómo se tomó la orden ni cómo se va a presentar. Si se cambia la receta de un platillo, solo el cocinero se ve afectado, pero el camarero y el proceso de servir no cambian.

3. **El camarero que sirve** tiene la responsabilidad de **llevar la comida a la mesa**. No le importa cómo se preparó la comida ni quién la pidió. Si cambian la forma de servir (por ejemplo, de bandejas a platos individuales), solo este camarero tendría que cambiar su manera de trabajar.

Cada rol tiene una **única responsabilidad**, lo que se traduce en que cada uno tiene **una única razón para cambiar**. Esto facilita que, si se produce un cambio en una parte, las otras no se vean afectadas. Podria cambiar el camaremo que toma nota, el cocinero o el camarero que sirve, pero no afecta a los otros.

### 5.3. Cómo relacionar el SRP con aplicaciones reales
El SRP se aplica no solo en programas pequeños, sino en proyectos más grandes y complejos como:

1. **Aplicaciones web**:
     - El **frontend** (cliente) tiene la responsabilidad de capturar y validar datos (similar a `obtener_datos_rectangulo`).
     - El **backend** (servidor) tiene la responsabilidad de procesar esos datos y devolver una respuesta (similar a `calcular_area`).
     - El **frontend** presenta los resultados al usuario de manera comprensible (similar a `mostrar_resultado`).

2. **Aplicaciones con diferentes módulos**:
     - Cada módulo tiene una responsabilidad específica, como gestionar la base de datos, realizar cálculos o manejar la interfaz de usuario.


## 6. Conclusión
Es importante separar las fases de un programa desde el principio, ya que esto nos preparará para escribir código modular y profesional. Aunque todas las fases se pueden probar, en este momento es recomendable centrarse en probar la lógica de negocio (`calcular_area`) para entender cómo se pueden realizar pruebas unitarias efectivas.

Separar las responsabilidades en funciones independientes y pequeñas sigue el principio de responsabilidad única, lo que nos ayuda a escribir un código más limpio, mantenible y fácil de probar. Es importante acostumbrarse a esta práctica, ya que en aplicaciones más complejas, esta organización será crucial para gestionar el código de manera eficiente.