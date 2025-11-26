# U2.1 - Sentencias Condicionales

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son las sentencias condicionales?

* Permiten tomar decisiones en el código
* Ejecutan diferentes bloques según condiciones
* Fundamentales en cualquier lenguaje de programación
* Controlan el flujo de ejecución del programa

Note: Las sentencias condicionales son estructuras de control que permiten que un programa tome decisiones basadas en condiciones. Son esenciales para crear programas que respondan de manera diferente según las circunstancias. Sin ellas, los programas solo ejecutarían secuencias lineales de instrucciones.


### Palabras clave en Python

* **if**: Primera evaluación de condición
* **elif**: Condiciones alternativas (else if)
* **else**: Caso por defecto (cuando ninguna se cumple)
* Similar en la mayoría de lenguajes de programación

Note: Aunque la sintaxis puede variar entre lenguajes, el concepto de condicionales es universal. Python utiliza palabras clave en inglés muy intuitivas. En otros lenguajes como Java, Kotlin o C, encontraremos estructuras similares aunque con sintaxis diferente (llaves en lugar de indentación).

---

## Expresiones Booleanas


### Valores booleanos

* Solo dos valores posibles: `True` o `False`
* Resultado de comparaciones y evaluaciones lógicas
* Tipo de dato fundamental en programación

```python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

Note: Los valores booleanos son nombrados en honor a George Boole, matemático que desarrolló el álgebra booleana. En Python, True y False son palabras reservadas y deben escribirse con la primera letra en mayúscula. Son objetos de la clase bool.


### Operador de igualdad

* Compara si dos valores son iguales
* Símbolo: `==` (doble igual)
* Devuelve True o False

```python
>>> 5 == 5
True
>>> 5 == 6
False
>>> "hola" == "hola"
True
```

Note: Es muy importante distinguir entre = (asignación) y == (comparación). El error más común en principiantes es usar = cuando se quiere comparar. El operador == compara valores, no identidad de objetos.


### Operadores de comparación

* `!=` : Diferente de
* `>` : Mayor que
* `<` : Menor que
* `>=` : Mayor o igual que
* `<=` : Menor o igual que

```python
>>> x = 10
>>> x != 5
True
>>> x > 8
True
>>> x <= 10
True
```

Note: Estos operadores funcionan con números, cadenas y otros tipos comparables. Con cadenas, la comparación es lexicográfica (alfabética). Es importante recordar que no existe =< ni =>, el signo igual siempre va después del símbolo de comparación.


### Operadores especiales: is

* `is` : Compara identidad de objetos (misma referencia)
* `is not` : Objetos con diferente identidad

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b  # Mismo contenido
True
>>> a is b  # Diferente objeto en memoria
False
>>> c = a
>>> c is a  # Misma referencia
True
```

Note: La diferencia entre == e is es crucial. El operador == compara valores mientras que is compara si dos variables apuntan exactamente al mismo objeto en memoria. Esto es especialmente importante cuando trabajamos con None, donde siempre debemos usar "is None" en lugar de "== None".

---

## Operadores Lógicos


### Operador AND

* Ambas condiciones deben ser verdaderas
* Símbolo: `and`
* Devuelve True solo si ambas son True

```python
>>> x = 5
>>> x > 0 and x < 10
True
>>> x > 0 and x < 3
False
```

Note: El operador and realiza una evaluación en cortocircuito: si la primera condición es False, no evalúa la segunda porque ya sabe que el resultado será False. Esto es útil para evitar errores, como se verá más adelante con el patrón guardián.


### Operador OR

* Al menos una condición debe ser verdadera
* Símbolo: `or`
* Devuelve True si cualquiera es True

```python
>>> n = 15
>>> n % 2 == 0 or n % 3 == 0
True
>>> n % 2 == 0 or n % 5 == 0
True
```

Note: El operador or también usa evaluación en cortocircuito: si la primera condición es True, no evalúa la segunda. Esto mejora la eficiencia y permite escribir código más seguro.


### Operador NOT

* Niega una expresión booleana
* Símbolo: `not`
* Invierte el valor True/False

```python
>>> x = 5
>>> not (x > 10)
True
>>> activo = True
>>> not activo
False
```

Note: El operador not tiene la mayor precedencia entre los operadores lógicos, seguido de and y luego or. Los paréntesis pueden usarse para controlar el orden de evaluación y mejorar la legibilidad.


### Combinando operadores lógicos

* Se pueden combinar múltiples operadores
* Usar paréntesis para claridad
* Precedencia: not > and > or

```python
>>> x = 8
>>> (x > 5 and x < 10) or (x > 15 and x < 20)
True
>>> not (x < 0 or x > 100)
True
```

Note: Aunque Python tiene reglas de precedencia definidas, siempre es mejor usar paréntesis para hacer el código más legible y explícito. Esto ayuda tanto a quien escribe el código como a quien lo lee posteriormente.


### Flexibilidad de Python con valores

* Python acepta números como booleanos
* 0 se interpreta como False
* Cualquier número distinto de 0 es True

```python
>>> 17 and True
True
>>> 0 and True
0
>>> 5 or False
5
```

Note: Aunque esta flexibilidad existe, es recomendable para principiantes usar expresiones booleanas explícitas. La conversión automática puede llevar a confusión. En Python, también las cadenas vacías, listas vacías y None se evalúan como False.

---

## Sentencia IF Simple


### Estructura básica del if

* Sintaxis: `if condicion:`
* El bloque se indenta (tabulación o espacios)
* Se ejecuta solo si la condición es True

```python
x = 10
if x > 0:
    print('x es positivo')
```

Note: En Python, la indentación no es opcional, es parte de la sintaxis. La convención es usar 4 espacios (nunca mezclar espacios y tabulaciones). Los dos puntos al final de la línea if son obligatorios.


### La condición

* Debe ser una expresión booleana
* Va seguida de dos puntos (:)
* No requiere paréntesis (pero se pueden usar)

```python
edad = 18
if edad >= 18:
    print('Eres mayor de edad')

# También válido con paréntesis
if (edad >= 18):
    print('Eres mayor de edad')
```

Note: Aunque los paréntesis no son necesarios en Python (a diferencia de C, Java o Kotlin), pueden usarse para mejorar la legibilidad en condiciones complejas. La consistencia en el estilo es importante en un proyecto.


### Bloque indentado

* Todas las líneas del bloque deben tener la misma indentación
* Pueden ser múltiples sentencias
* El bloque termina cuando termina la indentación

```python
x = 15
if x > 10:
    print('x es mayor que 10')
    print('Esta línea también se ejecuta')
    print('Y esta también')
print('Esta línea siempre se ejecuta')
```

Note: La indentación define el alcance del bloque if. Todo lo que esté al mismo nivel de indentación forma parte del bloque. Python generalmente usa 4 espacios, aunque técnicamente cualquier número consistente funciona.


### La sentencia pass

* No hace nada
* Útil como marcador de posición
* Necesaria cuando se requiere un bloque pero aún no está implementado

```python
x = -5
if x < 0:
    pass  # TODO: gestionar valores negativos
```

Note: La sentencia pass es útil durante el desarrollo cuando queremos definir la estructura del código pero aún no implementar la lógica. Python requiere al menos una sentencia en cada bloque, por eso pass es necesario en bloques vacíos.


### Ejemplo completo: Verificar edad

```python
edad = int(input('Introduce tu edad: '))

if edad >= 18:
    print('Puedes votar')
    print('Tienes plenos derechos')
    
if edad < 18:
    print('Aún no puedes votar')
    print('Eres menor de edad')
```

Note: En este ejemplo vemos dos sentencias if independientes. Aunque funciona, no es la forma más eficiente. Más adelante veremos cómo usar if-else para este tipo de situaciones donde las condiciones son mutuamente excluyentes.

---

## Ejecución Alternativa (if-else)


### Estructura if-else

* Dos posibilidades mutuamente excluyentes
* Se ejecuta una u otra, nunca ambas
* Sintaxis: `if ... else:`

```python
x = 7
if x % 2 == 0:
    print('x es par')
else:
    print('x es impar')
```

Note: La estructura if-else garantiza que exactamente uno de los dos bloques se ejecutará. Es más eficiente que usar dos ifs independientes porque una vez que se evalúa la primera condición como verdadera, no necesita evaluar más.


### Las ramas

* Cada bloque (if y else) es una rama
* Solo se ejecuta una rama
* No se puede ejecutar ninguna de las dos

```python
temperatura = 25
if temperatura > 30:
    print('Hace calor')
    print('Bebe agua')
else:
    print('Temperatura agradable')
    print('Disfruta el día')
```

Note: El concepto de "rama" viene de los diagramas de flujo, donde el programa "se bifurca" en diferentes caminos. Es importante entender que las ramas son mutuamente excluyentes en la estructura if-else.


### Ejemplo: Validar contraseña

```python
password = input('Introduce la contraseña: ')
correcta = 'python123'

if password == correcta:
    print('Acceso concedido')
    print('Bienvenido al sistema')
else:
    print('Contraseña incorrecta')
    print('Acceso denegado')
```

Note: Este es un ejemplo educativo muy simplificado. En aplicaciones reales, nunca se deben almacenar contraseñas en texto plano ni compararlas directamente. Se deben usar técnicas de hashing y salting.


### Ejemplo: Determinar mayor de dos números

```python
a = int(input('Primer número: '))
b = int(input('Segundo número: '))

if a > b:
    print(f'{a} es mayor que {b}')
else:
    print(f'{b} es mayor o igual que {a}')
```

Note: Observa que la segunda rama cubre dos casos: cuando b es mayor y cuando son iguales. Si necesitáramos distinguir estos tres casos, deberíamos usar if-elif-else, que veremos a continuación.


### Diferencia con dos ifs independientes

```python
# Menos eficiente
if x > 0:
    print('Positivo')
if x <= 0:
    print('No positivo')

# Más eficiente
if x > 0:
    print('Positivo')
else:
    print('No positivo')
```

Note: Usar if-else es más eficiente porque solo evalúa una condición. Con dos ifs independientes, Python evalúa ambas condiciones incluso cuando la primera es True. Además, if-else hace explícito que las condiciones son mutuamente excluyentes.

---

## Condicionales Encadenados (elif)


### Estructura if-elif-else

* Múltiples condiciones a evaluar
* Se evalúan en orden
* Se ejecuta el primer bloque cuya condición sea True

```python
x = 5
y = 7

if x < y:
    print('x es menor que y')
elif x > y:
    print('x es mayor que y')
else:
    print('x e y son iguales')
```

Note: La palabra elif es una contracción de "else if". La estructura if-elif-else permite manejar múltiples casos de forma clara y eficiente. Solo se ejecuta el bloque del primer elif cuya condición sea True.


### Múltiples elif

* No hay límite en el número de elif
* Se evalúan secuencialmente
* La cláusula else es opcional

```python
nota = 7

if nota >= 9:
    print('Sobresaliente')
elif nota >= 7:
    print('Notable')
elif nota >= 5:
    print('Aprobado')
else:
    print('Suspenso')
```

Note: El orden de los elif es crucial. Python evalúa de arriba hacia abajo y ejecuta el primer bloque que encuentra verdadero. Si pusiéramos "nota >= 5" primero, un 9 se clasificaría como "Aprobado" porque nunca llegaría a verificar las otras condiciones.


### Sin else final

* El else es opcional
* Útil cuando no se requiere acción por defecto

```python
comando = 'salir'

if comando == 'iniciar':
    print('Iniciando sistema...')
elif comando == 'parar':
    print('Deteniendo sistema...')
elif comando == 'salir':
    print('Cerrando aplicación...')
# No hay else, otros comandos se ignoran
```

Note: Cuando no hay else y ninguna condición es verdadera, simplemente no se ejecuta ningún bloque. Esto es apropiado cuando no necesitamos manejar el caso por defecto.


### Ejemplo: Clasificar edad I

```python
edad = int(input('Introduce tu edad: '))

if edad < 0:
    print('Edad inválida')
elif edad < 13:
    print('Eres un niño')
elif edad < 18:
    print('Eres adolescente')
elif edad < 65:
    print('Eres adulto')
else:
    print('Eres adulto mayor')
```

Note: Este ejemplo muestra cómo manejar múltiples rangos de valores. Es importante validar primero los casos especiales (como edad negativa) antes de procesar los casos normales.


### Ejemplo: Clasificar edad II

```python
edad = int(input('Introduce tu edad: '))

if edad < 13:
    categoria = 'Niño'
elif edad < 18:
    categoria = 'Adolescente'
elif edad < 65:
    categoria = 'Adulto'
else:
    categoria = 'Adulto mayor'

print(f'Categoría: {categoria}')
```

Note: Esta versión es preferible porque separa la lógica de clasificación de la presentación del resultado. Esto hace el código más mantenible y reutilizable.


### Ejemplo: Calculadora simple

```python
operacion = input('Operación (+, -, *, /): ')
a = float(input('Primer número: '))
b = float(input('Segundo número: '))

if operacion == '+':
    resultado = a + b
elif operacion == '-':
    resultado = a - b
elif operacion == '*':
    resultado = a * b
elif operacion == '/':
    resultado = a / b
else:
    print('Operación no válida')
    resultado = None

if resultado is not None:
    print(f'Resultado: {resultado}')
```

Note: Este ejemplo muestra un uso práctico de elif para implementar diferentes operaciones. Observa cómo usamos una variable para almacenar el resultado y luego lo mostramos solo si la operación fue válida.

---

## Condicionales Anidados


### Concepto de anidamiento

* Un condicional dentro de otro
* Cada nivel tiene su propia indentación
* Puede dificultar la lectura si se abusa

```python
x = 10
y = 5

if x == y:
    print('x e y son iguales')
else:
    if x < y:
        print('x es menor que y')
    else:
        print('x es mayor que y')
```

Note: Los condicionales anidados son necesarios a veces, pero hacen el código más difícil de leer. Cada nivel de anidamiento añade complejidad cognitiva. Siempre que sea posible, es mejor usar elif o simplificar con operadores lógicos.


### Múltiples niveles de anidación

```python
num = int(input('Introduce un número: '))

if num >= 0:
    if num == 0:
        print('El número es cero')
    else:
        if num % 2 == 0:
            print('Número positivo par')
        else:
            print('Número positivo impar')
else:
    print('Número negativo')
```

Note: Este ejemplo muestra tres niveles de anidación. Aunque funcional, puede ser confuso. Veremos cómo simplificarlo usando operadores lógicos y estructuras más planas.


### Simplificar con operadores lógicos I

```python
# Anidado (más complejo)
if 0 < x:
    if x < 10:
        print('x es un número positivo de un dígito')

# Simplificado con and (mejor)
if 0 < x and x < 10:
    print('x es un número positivo de un dígito')
```

Note: El operador and permite combinar condiciones que antes requerían anidamiento. Esto hace el código más legible y reduce la indentación. Python incluso permite escribir "0 < x < 10" que es aún más intuitivo.


### Simplificar con operadores lógicos II

```python
# Forma más pythonica
if 0 < x < 10:
    print('x es un número positivo de un dígito')

# También funciona con múltiples comparaciones
if 0 <= edad < 150:
    print('Edad válida')
```

Note: Esta notación encadenada es única de Python y muy intuitiva porque se lee como matemáticas. No todos los lenguajes la soportan. En Java o C++ tendrías que escribir "x > 0 && x < 10".


### Ejemplo: Validación de datos I

```python
usuario = input('Usuario: ')
password = input('Contraseña: ')

if len(usuario) >= 5:
    if len(password) >= 8:
        if '@' in usuario or '.' in usuario:
            print('Registro válido')
        else:
            print('Usuario debe contener @ o .')
    else:
        print('Contraseña muy corta')
else:
    print('Usuario muy corto')
```

Note: Este código funciona pero tiene tres niveles de anidación. Cada nivel hace más difícil seguir la lógica. Veamos cómo mejorarlo.


### Ejemplo: Validación de datos II

```python
usuario = input('Usuario: ')
password = input('Contraseña: ')

if len(usuario) < 5:
    print('Usuario muy corto')
elif len(password) < 8:
    print('Contraseña muy corta')
elif '@' not in usuario and '.' not in usuario:
    print('Usuario debe contener @ o .')
else:
    print('Registro válido')
```

Note: Esta versión usa elif y "retornos tempranos" para las condiciones de error. Es más fácil de leer porque reduce la anidación y agrupa los casos de error al principio.


### Cuándo usar anidamiento

* Cuando las condiciones internas dependen de las externas
* Cuando no se puede simplificar con operadores lógicos
* Con moderación para mantener legibilidad

```python
if tiene_permiso:
    if esta_en_horario:
        if hay_disponibilidad:
            print('Acceso concedido')
        else:
            print('No hay disponibilidad')
    else:
        print('Fuera de horario')
else:
    print('Sin permiso')
```

Note: En este caso, el anidamiento tiene sentido porque cada nivel proporciona un mensaje de error específico. Sin embargo, también podría simplificarse usando and y manejando los mensajes de error de otra forma.

---

## Evaluación en Cortocircuito


### ¿Qué es el cortocircuito?

* Python evalúa expresiones de izquierda a derecha
* Detiene evaluación cuando conoce el resultado
* Mejora eficiencia y previene errores

```python
x = 5
# Si x >= 2 es False, no evalúa (x/y) > 2
resultado = x >= 2 and (x/y) > 2
```

Note: El cortocircuito es una optimización importante que Python (y la mayoría de lenguajes) implementa. No solo mejora el rendimiento sino que también es crucial para escribir código seguro.


### Cortocircuito con AND

* Si el primer operando es False, devuelve False
* No evalúa el segundo operando
* Útil para prevenir errores

```python
x = 1
y = 0
# No genera error porque no evalúa (x/y)
resultado = x >= 2 and (x/y) > 2
print(resultado)  # False
```

Note: Si Python evaluara siempre ambos lados del and, este código generaría un ZeroDivisionError. Gracias al cortocircuito, la segunda parte nunca se evalúa porque x >= 2 ya es False.


### Cortocircuito con OR

* Si el primer operando es True, devuelve True
* No evalúa el segundo operando

```python
x = 10
y = 0
# No genera error porque no evalúa (x/y) > 2
resultado = x < 5 or (x/y) > 2
print(resultado)  # False (evaluó solo x < 5)

resultado = x > 5 or (x/y) > 2
print(resultado)  # True (no evaluó x/y)
```

Note: Con or, si la primera condición es True, Python devuelve True inmediatamente sin evaluar el resto. Esto es útil para proporcionar valores por defecto o para operaciones costosas que queremos evitar cuando sea posible.


### Patrón Guardián

* Protege de errores usando cortocircuito
* Evalúa condiciones seguras primero
* Evita división por cero, índices inválidos, etc.

```python
y = 0
# El guardián y != 0 previene la división por cero
if y != 0 and (x/y) > 2:
    print('x es más del doble de y')
```

Note: El patrón guardián es una técnica fundamental en programación. Siempre colocamos las verificaciones de seguridad antes de las operaciones que podrían fallar. Es como poner un guardia que verifica condiciones antes de permitir el paso.


### Ejemplo: Validar división I

```python
x = 10
y = 0

# Mal: puede generar error
# if (x/y) > 2:
#     print('OK')

# Bien: el guardián previene el error
if y != 0 and (x/y) > 2:
    print('x es más del doble de y')
```

Note: Este patrón es tan común que debe convertirse en un hábito. Siempre que vayas a hacer una operación que podría fallar, coloca una verificación antes usando and.


### Ejemplo: Validar división II

```python
dividendo = float(input('Dividendo: '))
divisor = float(input('Divisor: '))

# Guardián protege contra división por cero
if divisor != 0 and dividendo / divisor > 10:
    print('El cociente es mayor que 10')
elif divisor != 0:
    print(f'El cociente es {dividendo / divisor}')
else:
    print('No se puede dividir por cero')
```

Note: En este ejemplo vemos cómo usar el patrón guardián en múltiples ramas. Cada vez que necesitamos usar el divisor, primero verificamos que no sea cero.


### Ejemplo: Validar índice de lista

```python
numeros = [1, 2, 3, 4, 5]
indice = 10

# Guardián verifica longitud antes de acceder
if indice < len(numeros) and numeros[indice] > 3:
    print('El elemento es mayor que 3')
else:
    print('Índice inválido o condición no cumplida')
```

Note: Este es otro uso común del patrón guardián: verificar que un índice esté dentro de los límites antes de acceder a una lista. Sin el guardián, obtendríamos un IndexError.

---

## Patrones Comunes


### Validación de entrada

* Verificar que los datos sean correctos
* Dar retroalimentación al usuario
* Común en aplicaciones interactivas

```python
edad = int(input('Edad: '))

if edad < 0:
    print('La edad no puede ser negativa')
elif edad > 120:
    print('Edad poco probable')
else:
    print(f'Edad registrada: {edad}')
```

Note: La validación de entrada es fundamental en cualquier aplicación. Nunca debemos confiar en que el usuario proporcionará datos válidos. Siempre debemos verificar y manejar casos extremos.


### Cálculo condicional

* Aplicar diferentes fórmulas según condiciones
* Común en aplicaciones matemáticas y científicas

```python
horas = 45
tarifa = 15

if horas <= 40:
    salario = horas * tarifa
else:
    # Horas extra se pagan al 150%
    regulares = 40 * tarifa
    extras = (horas - 40) * tarifa * 1.5
    salario = regulares + extras

print(f'Salario: {salario}€')
```

Note: Este patrón es muy común en cálculos que tienen diferentes reglas según rangos de valores. Las horas extra, los impuestos progresivos, los descuentos por volumen, todos siguen este patrón.


### Clasificación en categorías

* Asignar elementos a grupos según criterios
* Útil para análisis y reportes

```python
temperatura = 22

if temperatura < 0:
    clima = 'Helado'
elif temperatura < 10:
    clima = 'Frío'
elif temperatura < 20:
    clima = 'Templado'
elif temperatura < 30:
    clima = 'Cálido'
else:
    clima = 'Muy caliente'

print(f'El clima está {clima}')
```

Note: Este patrón de clasificación en rangos es muy útil para convertir valores numéricos en categorías comprensibles. Lo encontrarás en calificaciones, niveles de riesgo, categorías de edad, etc.


### Búsqueda de máximo/mínimo condicional

* Encontrar valores extremos que cumplan condiciones
* Combina comparación con condicionales

```python
numeros = [15, 22, 8, 35, 42, 18]
umbral = 20

# Buscar el mayor número menor que el umbral
maximo_valido = None

for num in numeros:
    if num < umbral:
        if maximo_valido is None or num > maximo_valido:
            maximo_valido = num

if maximo_valido is not None:
    print(f'Mayor número válido: {maximo_valido}')
else:
    print('No hay números válidos')
```

Note: Este patrón combina iteración con condicionales para encontrar valores que cumplan criterios específicos. Es más sofisticado que simplemente encontrar el máximo de toda la lista.


### Procesamiento de menús

* Presentar opciones y ejecutar acciones
* Base de interfaces de consola

```python
print('1. Nuevo')
print('2. Abrir')
print('3. Guardar')
print('4. Salir')

opcion = input('Selecciona opción: ')

if opcion == '1':
    print('Creando nuevo archivo...')
elif opcion == '2':
    print('Abriendo archivo...')
elif opcion == '3':
    print('Guardando archivo...')
elif opcion == '4':
    print('Saliendo...')
else:
    print('Opción no válida')
```

Note: Los menús son una aplicación práctica muy común de if-elif-else. En aplicaciones más grandes, cada opción llamaría a funciones específicas en lugar de solo imprimir mensajes.


### Validación múltiple con banderas

* Verificar múltiples condiciones
* Usar variables booleanas para claridad

```python
usuario = 'admin'
password = 'pass123'
tiene_permiso = True

credenciales_ok = (usuario == 'admin' and 
                   password == 'pass123')
puede_acceder = credenciales_ok and tiene_permiso

if puede_acceder:
    print('Acceso concedido')
else:
    if not credenciales_ok:
        print('Credenciales incorrectas')
    else:
        print('Sin permisos suficientes')
```

Note: Usar variables booleanas con nombres descriptivos hace el código mucho más legible. En lugar de condiciones complejas, tenemos expresiones que se leen como lenguaje natural.

---

## Buenas Prácticas


### Claridad sobre brevedad

* Priorizar código legible
* Usar nombres descriptivos
* Añadir espacios para separar lógica

```python
# Menos claro
if a>18and b<100:x=True

# Más claro
edad = 25
edad_maxima = 100
if edad > 18 and edad < edad_maxima:
    es_valido = True
```

Note: El código se lee muchas más veces de las que se escribe. Sacrificar un poco de brevedad por claridad siempre vale la pena. Los nombres descriptivos y el espaciado adecuado hacen el código auto-documentado.


### Evitar anidamiento excesivo

* Máximo 2-3 niveles de profundidad
* Usar elif cuando sea posible
* Extraer lógica compleja a funciones

```python
# Evitar
if a:
    if b:
        if c:
            if d:
                # Muy profundo

# Mejor
if not a:
    return
if not b:
    return
if not c:
    return
if d:
    # Lógica principal
```

Note: El código profundamente anidado es difícil de leer y mantener. La técnica de "retorno temprano" para condiciones de error hace el código más plano y fácil de seguir. También se conoce como "fail fast".


### Consistencia en comparaciones

* Orden consistente de comparaciones
* Usar el mismo estilo en todo el código

```python
# Inconsistente
if edad > 18:
    ...
if 65 < edad:
    ...

# Consistente
if edad > 18:
    ...
if edad > 65:
    ...
```

Note: La consistencia ayuda al cerebro a procesar el código más rápidamente. Si siempre pones la variable primero, los lectores no tienen que reinterpretar cada comparación.


### Condiciones positivas cuando sea posible

* Las afirmaciones positivas son más fáciles de entender
* Evitar dobles negaciones

```python
# Menos claro
if not no_es_valido:
    procesar()

# Más claro
if es_valido:
    procesar()
```

Note: El cerebro procesa afirmaciones positivas más fácilmente que negaciones. Las dobles negaciones son especialmente confusas. Siempre que puedas, formula las condiciones en términos positivos.


### Comentar la lógica compleja

* Explicar el "por qué", no el "qué"
* Documentar casos especiales
* Aclarar condiciones complejas

```python
# Verificar que el usuario tenga edad suficiente
# y que no haya superado el límite de intentos (3)
if edad >= 18 and intentos < 3:
    permitir_acceso()
```

Note: Los comentarios deben explicar decisiones de diseño, restricciones del dominio o lógica que no sea obvia. No comentes código obvio como "# incrementar x" antes de "x = x + 1".


### Orden de condiciones

* Casos más comunes primero (eficiencia)
* Casos especiales al principio (validación)
* Depende del contexto

```python
# Para validación: casos especiales primero
if edad < 0:
    return 'Error: edad inválida'
elif edad < 18:
    return 'Menor de edad'
elif edad < 65:
    return 'Adulto'
else:
    return 'Adulto mayor'
```

Note: El orden de las condiciones puede afectar tanto la eficiencia como la claridad. Para validaciones, pon los casos de error primero. Para el procesamiento normal, pon los casos más frecuentes primero.

---

## Depuración de Condicionales


### Errores comunes: Indentación

* Python es sensible a la indentación
* Cada nivel debe ser consistente
* Usar 4 espacios (convención PEP 8)

```python
# Error: indentación inconsistente
if edad > 18:
  print('Mayor de edad')
    print('Puede votar')  # Error!

# Correcto
if edad > 18:
    print('Mayor de edad')
    print('Puede votar')
```

Note: Los errores de indentación son muy comunes en principiantes. Configura tu editor para mostrar espacios y tabulaciones, y para convertir tabulaciones a espacios automáticamente.


### Errores comunes: Confundir = con ==

* `=` es asignación
* `==` es comparación
* Error muy frecuente en principiantes

```python
x = 5

# Error: asignación en lugar de comparación
if x = 5:  # SyntaxError
    print('x es 5')

# Correcto
if x == 5:
    print('x es 5')
```

Note: Este error es tan común que muchos lenguajes modernos lo detectan y dan advertencias. Python directamente no permite asignaciones en condiciones, generando un error de sintaxis.


### Errores comunes: Olvidar los dos puntos

* Todas las líneas de encabezado requieren `:`
* if, elif, else deben terminar con dos puntos

```python
# Error: faltan los dos puntos
if edad > 18
    print('Mayor')

# Correcto
if edad > 18:
    print('Mayor')
```

Note: Los dos puntos son obligatorios en Python para todas las estructuras de control. Son la señal de que viene un bloque indentado. Si los olvidas, obtendrás un SyntaxError.


### Depurar con print

* Insertar prints para ver valores
* Verificar qué rama se ejecuta
* Útil para entender flujo de ejecución

```python
x = 10
y = 20

print(f'Antes del if: x={x}, y={y}')

if x > y:
    print('Rama 1: x > y')
    resultado = 'x mayor'
elif x < y:
    print('Rama 2: x < y')
    resultado = 'y mayor'
else:
    print('Rama 3: x == y')
    resultado = 'iguales'

print(f'Resultado: {resultado}')
```

Note: Aunque existen depuradores más sofisticados, usar print es rápido y efectivo para problemas simples. Es especialmente útil cuando estás aprendiendo para ver qué camino toma el código.


### Usar el depurador

* Establecer breakpoints
* Ejecutar paso a paso
* Inspeccionar valores de variables
* VSCode y otros IDEs tienen depuradores integrados

Note: Aprender a usar un depurador es una habilidad esencial. Permite pausar la ejecución, examinar el estado del programa y avanzar línea por línea. Es mucho más potente que usar prints, especialmente para código complejo.


### Ejemplo: Depurar comparación

```python
edad_str = input('Edad: ')
# Olvidamos convertir a int

if edad_str > 18:  # Compara strings, no números!
    print('Mayor de edad')
else:
    print('Menor de edad')

# Correcto
edad = int(edad_str)
if edad > 18:
    print('Mayor de edad')
```

Note: Este es un error sutil pero común. La comparación de strings es lexicográfica: "9" > "18" es True porque "9" viene después de "1" alfabéticamente. Siempre convierte las entradas a los tipos apropiados.

---

## Ejercicios Propuestos


### Ejercicio 1: Número positivo/negativo

Escribe un programa que solicite un número al usuario y determine si es positivo, negativo o cero. Muestra un mensaje apropiado para cada caso.

```python
# Tu código aquí
```

Note: Este ejercicio refuerza el uso básico de if-elif-else. Recuerda manejar los tres casos: positivo, negativo y cero. No olvides convertir la entrada a número.


### Ejercicio 2: Mayor de tres números

Crea un programa que pida tres números al usuario y determine cuál es el mayor. Maneja el caso en que dos o más números sean iguales.

```python
# Tu código aquí
```

Note: Este ejercicio requiere múltiples comparaciones. Hay varias formas de resolverlo: comparando de dos en dos, o usando max(). Intenta hacerlo con condicionales primero para practicar.


### Ejercicio 3: Año bisiesto

Escribe un programa que determine si un año es bisiesto. Un año es bisiesto si es divisible por 4, excepto los años que son divisibles por 100, a menos que también sean divisibles por 400.

```python
# Tu código aquí
```

Note: Este ejercicio practica la lógica con operadores múltiples y el operador módulo. La regla completa: divisible por 4 AND (NO divisible por 100 OR divisible por 400).


### Ejercicio 4: Calculadora de IMC

Crea un programa que calcule el Índice de Masa Corporal (IMC = peso / altura²) y lo clasifique: bajo peso (< 18.5), normal (18.5-24.9), sobrepeso (25-29.9), obesidad (≥ 30).

```python
# Tu código aquí
```

Note: Este ejercicio combina cálculos con clasificación en rangos. Es similar al ejemplo del clima. Recuerda validar que peso y altura sean positivos.


### Ejercicio 5: Conversor de calificaciones

Escribe un programa que convierta calificaciones numéricas (0-100) a letras: A (90-100), B (80-89), C (70-79), D (60-69), F (<60). Valida que la entrada esté en el rango correcto.

```python
# Tu código aquí
```

Note: Este ejercicio practica la validación de entrada y la clasificación en rangos. Piensa en qué orden debes poner las condiciones para que funcione correctamente.


### Ejercicio 6: Validador de contraseña

Crea un programa que valide una contraseña según estos criterios: al menos 8 caracteres, contiene mayúsculas, minúsculas y números. Informa al usuario qué requisitos no cumple.

```python
# Tu código aquí
```

Note: Este ejercicio es más complejo y requiere múltiples verificaciones. Puedes usar métodos de string como isupper(), islower(), isdigit(). También puedes practicar dar feedback específico sobre qué falta.

---

## Recursos Adicionales


### Documentación oficial

* [Python.org - Control de Flujo](https://docs.python.org/es/3/tutorial/controlflow.html)
* [PEP 8 - Guía de Estilo](https://pep8.org/)
* Tutorial interactivo en Python.org

Note: La documentación oficial de Python es excelente y está disponible en español. PEP 8 es la guía de estilo oficial que todo programador de Python debería conocer.


### Libros recomendados

* "Python para todos" - Charles Severance
* "Aprende Python" - Andrés Marzal
* "Automate the Boring Stuff" - Al Sweigart

Note: Estos libros son excelentes para principiantes. "Python para todos" es gratuito online. "Automate the Boring Stuff" enseña Python a través de proyectos prácticos.


### Plataformas de práctica

* HackerRank
* LeetCode
* Exercism.io
* CodingBat (Python section)

Note: La práctica es esencial para dominar la programación. Estas plataformas ofrecen ejercicios graduados desde principiante hasta experto, con feedback automático.


### Consejos finales

* Practica escribiendo código todos los días
* Lee código de otros programadores
* Experimenta y comete errores
* Los errores son oportunidades de aprendizaje

Note: La programación se aprende programando. No tengas miedo de experimentar y cometer errores. Cada error es una oportunidad para entender mejor cómo funciona el lenguaje.

---

## Resumen


### Conceptos clave

* Expresiones booleanas y operadores de comparación
* Operadores lógicos: and, or, not
* Estructuras: if, if-else, if-elif-else
* Condicionales anidados y cuándo usarlos
* Evaluación en cortocircuito y patrón guardián

Note: Estos son los conceptos fundamentales que hemos cubierto. Asegúrate de entender cada uno antes de avanzar a temas más complejos.


### Mejores prácticas

* Escribir código claro y legible
* Evitar anidamiento excesivo
* Usar nombres descriptivos
* Validar entradas del usuario
* Aplicar el patrón guardián para prevenir errores

Note: Las buenas prácticas no son opcionales; son esenciales para escribir código que otros (y tú mismo en el futuro) puedan entender y mantener.


### Próximos pasos

* Practicar con ejercicios variados
* Combinar condicionales con bucles (siguiente tema)
* Aprender sobre excepciones y manejo de errores
* Estudiar estructuras de datos más complejas

Note: Las sentencias condicionales son fundamentales para todo lo que viene después. Asegúrate de dominarlas bien antes de continuar. En el próximo tema veremos bucles, que se combinan frecuentemente con condicionales.

---

## ¿Preguntas?

Note: Anima a los estudiantes a hacer preguntas. Las sentencias condicionales son fundamentales y es importante que todos los conceptos queden claros antes de avanzar.
