# U2.2 - Sentencias Iterativas

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son las sentencias iterativas?

* Permiten repetir bloques de código múltiples veces
* También llamadas bucles o loops
* Fundamentales para procesar colecciones de datos
* Evitan la repetición manual de código

Note: Las sentencias iterativas son estructuras que permiten ejecutar un bloque de código repetidamente. Son esenciales porque los ordenadores destacan en tareas repetitivas. Sin bucles, tendríamos que escribir el mismo código cientos o miles de veces.


### Tipos de bucles en Python

* **while**: Repite mientras una condición sea verdadera
* **for**: Repite sobre elementos de una secuencia
* **Bucles anidados**: Bucles dentro de otros bucles
* Sentencias de control: break, continue, pass

Note: Python proporciona dos tipos principales de bucles. While es más general y se usa cuando no sabemos cuántas iteraciones necesitamos. For es ideal cuando iteramos sobre colecciones. Otros lenguajes como C o Java también tienen do-while, pero Python no.


### Conceptos previos importantes

* **Iteración**: Una ejecución del cuerpo del bucle
* **Variable de iteración**: Variable que controla el bucle
* **Bucle infinito**: Bucle que nunca termina
* **Inicialización y actualización**: Preparar y modificar variables

Note: Antes de profundizar en bucles, es crucial entender estos conceptos. Una iteración es cada "vuelta" del bucle. La variable de iteración cambia en cada vuelta y eventualmente hace que el bucle termine. Si no actualizamos esta variable correctamente, obtenemos un bucle infinito.

---

## Actualización de Variables


### Concepto de actualización

* Modificar el valor de una variable basándose en su valor actual
* Patrón muy común en programación
* Esencial para controlar bucles

```python
x = x + 1  # Incrementar
y = y - 1  # Decrementar
z = z * 2  # Duplicar
```

Note: La actualización de variables puede parecer extraña matemáticamente (¿x puede ser igual a x + 1?), pero en programación es fundamental. El lado derecho se evalúa primero con el valor actual, luego se asigna a la variable.


### Inicialización obligatoria

* Una variable debe existir antes de actualizarla
* Python requiere inicialización explícita
* Error común: actualizar variable no inicializada

```python
# Error: variable no inicializada
>>> x = x + 1
NameError: name 'x' is not defined

# Correcto: inicializar primero
>>> x = 0
>>> x = x + 1
>>> print(x)
1
```

Note: A diferencia de algunos lenguajes que inicializan automáticamente a 0, Python requiere que declares e inicialices explícitamente. Esto previene errores sutiles pero puede confundir a principiantes.


### Incrementar y decrementar

* **Incrementar**: Añadir 1 (o cualquier valor)
* **Decrementar**: Restar 1 (o cualquier valor)
* Operaciones muy comunes en bucles

```python
contador = 0
contador = contador + 1  # Incrementar
print(contador)  # 1

contador = contador - 1  # Decrementar
print(contador)  # 0

# Forma abreviada
contador += 1  # Equivalente a contador = contador + 1
contador -= 1  # Equivalente a contador = contador - 1
```

Note: Los operadores += y -= son atajos convenientes. Python no tiene los operadores ++ y -- que existen en C o Java. Siempre usa += 1 o -= 1.


### Operadores de asignación compuestos

* Atajos para operaciones comunes
* Más concisos y a veces más eficientes
* Funcionan con todos los operadores aritméticos

```python
x = 10
x += 5   # x = x + 5    → 15
x -= 3   # x = x - 3    → 12
x *= 2   # x = x * 2    → 24
x /= 4   # x = x / 4    → 6.0
x //= 2  # x = x // 2   → 3.0
x %= 2   # x = x % 2    → 1.0
x **= 3  # x = x ** 3   → 1.0
```

Note: Estos operadores hacen el código más conciso y expresivo. Son especialmente útiles en bucles donde frecuentemente actualizamos contadores y acumuladores. La eficiencia es similar, pero la legibilidad mejora.


### Acumuladores

* Variable que acumula un resultado
* Patrón fundamental en programación
* Común en sumas, productos, concatenaciones

```python
# Acumular suma
total = 0
total += 10  # total = 10
total += 20  # total = 30
total += 30  # total = 60

# Acumular producto
producto = 1
producto *= 5   # producto = 5
producto *= 3   # producto = 15

# Acumular cadenas
mensaje = ""
mensaje += "Hola "
mensaje += "Mundo"
print(mensaje)  # "Hola Mundo"
```

Note: Los acumuladores son variables que "acumulan" resultados a través de múltiples operaciones. Para sumas, inicializa a 0. Para productos, inicializa a 1. Para cadenas, inicializa a cadena vacía. Este patrón aparecerá constantemente en bucles.

---

## Bucle WHILE


### Estructura básica del while

* Repite mientras la condición sea True
* Verifica la condición antes de cada iteración
* Puede ejecutarse cero veces si la condición inicial es False

```python
n = 5
while n > 0:
    print(n)
    n = n - 1
print('¡Despegue!')
```

Note: El bucle while es el más fundamental. Antes de cada iteración, evalúa la condición. Si es True, ejecuta el cuerpo. Si es False, sale del bucle. Es posible que nunca se ejecute si la condición inicial es False.


### Flujo de ejecución del while

1. Evaluar la condición (True o False)
2. Si es False, salir del bucle
3. Si es True, ejecutar el cuerpo
4. Volver al paso 1

```python
contador = 0
while contador < 3:
    print(f'Iteración {contador}')
    contador += 1

# Salida:
# Iteración 0
# Iteración 1
# Iteración 2
```

Note: Este flujo crea el "bucle". El programa vuelve repetidamente al principio del while hasta que la condición sea False. Es crucial entender que la condición se evalúa ANTES de cada iteración, no durante.


### Variable de iteración

* Controla cuándo termina el bucle
* Debe cambiar en cada iteración
* Si no cambia, bucle infinito

```python
# Bien: la variable cambia
i = 1
while i <= 5:
    print(i)
    i += 1  # Variable de iteración cambia

# Mal: bucle infinito
# i = 1
# while i <= 5:
#     print(i)
#     # ¡i nunca cambia!
```

Note: La variable de iteración es como un "cronómetro" para el bucle. Debe modificarse en cada vuelta para eventualmente hacer que la condición sea False. Olvidar actualizar esta variable es el error número uno que causa bucles infinitos.


### Ejemplo: Contador descendente

```python
# Cuenta regresiva desde 10
numero = 10

while numero >= 1:
    print(numero)
    numero -= 1
    
print('¡Feliz Año Nuevo!')

# Salida:
# 10
# 9
# 8
# ...
# 1
# ¡Feliz Año Nuevo!
```

Note: Este es un patrón común de cuenta regresiva. Iniciamos con un valor y lo decrementamos hasta llegar a una condición de parada. Observa que el bucle incluye el 1 porque usamos >= en lugar de >.


### Ejemplo: Suma de números I

```python
# Sumar números del 1 al 10
suma = 0
numero = 1

while numero <= 10:
    suma += numero
    numero += 1

print(f'La suma es: {suma}')  # 55
```

Note: Este ejemplo muestra el patrón acumulador. Suma es nuestro acumulador (comienza en 0). Numero es nuestra variable de iteración. En cada vuelta, añadimos el número actual a la suma y luego incrementamos el número.


### Ejemplo: Suma de números II

```python
# Sumar números hasta que el usuario diga 'fin'
suma = 0

while True:
    entrada = input('Introduce un número (fin para terminar): ')
    if entrada == 'fin':
        break
    numero = float(entrada)
    suma += numero

print(f'Total: {suma}')
```

Note: Este patrón usa un bucle infinito (while True) con break para salir. Es útil cuando no sabes de antemano cuántas iteraciones necesitas. El break sale inmediatamente del bucle. Sin embargo, es mejor evitar while True cuando sea posible.


### Bucles controlados por centinela

* Valor especial que indica fin de entrada
* Alternativa a break
* Más estructurado y legible

```python
suma = 0
entrada = input('Número (o "fin"): ')

while entrada != 'fin':
    suma += float(entrada)
    entrada = input('Número (o "fin"): ')

print(f'Total: {suma}')
```

Note: Un centinela es un valor especial que señala el final. Este patrón evita usar break y hace el bucle más predecible. Note que pedimos entrada antes del bucle y al final de cada iteración.

---

## Bucles Infinitos


### ¿Qué es un bucle infinito?

* Bucle cuya condición nunca se vuelve False
* El programa se "congela"
* Debe interrumpirse manualmente (Ctrl+C)

```python
# ¡CUIDADO! Bucle infinito
n = 10
while n > 0:
    print(n)
    # Olvidamos decrementar n
    # n nunca cambia, siempre es 10
```

Note: Los bucles infinitos son el error más común con while. El programa se queda atrapado ejecutando el bucle eternamente. En desarrollo, aprende a usar Ctrl+C para interrumpir programas. En servidores, pueden causar problemas serios.


### Causas comunes

* Olvidar actualizar la variable de iteración
* Actualización incorrecta (dirección equivocada)
* Condición que nunca se vuelve False
* Errores de lógica en la condición

```python
# Error 1: No actualizar
i = 0
while i < 5:
    print(i)
    # Falta: i += 1

# Error 2: Actualización incorrecta
i = 0
while i < 5:
    print(i)
    i -= 1  # ¡Decrementando en lugar de incrementar!
```

Note: Siempre verifica: (1) ¿Cambia la variable de iteración? (2) ¿Cambia en la dirección correcta? (3) ¿La condición eventualmente será False? Estos tres checks previenen la mayoría de bucles infinitos.


### Bucles infinitos intencionales

* A veces queremos un bucle infinito
* Servidores, juegos, sistemas de monitoreo
* Deben tener forma de salir (break, return)

```python
# Bucle de un servidor simple
while True:
    comando = input('> ')
    
    if comando == 'salir':
        break
    elif comando == 'ayuda':
        print('Comandos: ayuda, salir')
    else:
        print(f'Ejecutando: {comando}')
```

Note: Los bucles infinitos intencionales son comunes en programación de sistemas. Un servidor web, por ejemplo, corre en un bucle infinito esperando peticiones. La clave es tener una condición de salida clara y manejada.


### Usando break

* Sale inmediatamente del bucle más interno
* Útil para condiciones de salida complejas
* Mejor cuando la condición se cumple en medio del bucle

```python
# Buscar un valor en una lista
numeros = [3, 7, 2, 9, 5]
buscar = 9
encontrado = False
i = 0

while i < len(numeros):
    if numeros[i] == buscar:
        encontrado = True
        break
    i += 1

if encontrado:
    print(f'Encontrado en posición {i}')
```

Note: Break es útil pero debe usarse con moderación. A veces indica que la condición del while podría ser mejor. En este curso preferimos evitar break cuando sea posible para acostumbrarnos a pensar bien las condiciones.


### Evitar while True cuando sea posible

* Hace el código más predecible
* La condición documenta cuándo termina
* Más fácil de entender y mantener

```python
# Menos claro
while True:
    x = input('Número: ')
    if x == 'fin':
        break
    print(float(x) * 2)

# Más claro
x = input('Número: ')
while x != 'fin':
    print(float(x) * 2)
    x = input('Número: ')
```

Note: While True oculta la condición de salida dentro del bucle. Es mejor hacer la condición explícita en la línea del while. Esto hace que cualquiera que lea el código vea inmediatamente cuándo termina el bucle.

---

## Sentencia Continue


### ¿Qué hace continue?

* Salta al inicio del bucle inmediatamente
* Salta las instrucciones restantes de esa iteración
* No sale del bucle, solo de la iteración actual

```python
# Imprimir solo números impares del 1 al 10
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:  # Si es par
        continue         # Saltar a la siguiente iteración
    print(numero)
```

Note: Continue es como un "saltar adelante" dentro del bucle. Cuando se ejecuta, el resto del cuerpo del bucle se omite y vuelve a evaluar la condición. Es útil para evitar anidamiento excesivo de ifs.


### Ejemplo: Filtrar entrada

```python
# Procesar líneas ignorando comentarios
linea_num = 0
while linea_num < 5:
    entrada = input('Línea: ')
    linea_num += 1
    
    # Ignorar líneas que empiezan con #
    if entrada.startswith('#'):
        continue
    
    # Procesar línea normal
    print(f'Procesando: {entrada}')
```

Note: Este patrón es común al procesar archivos o entrada del usuario. Las líneas especiales (comentarios, líneas vacías) se saltan con continue. El código de procesamiento normal no necesita estar anidado en un else.


### Continue vs if-else

* Continue reduce anidamiento
* Hace el código más plano y legible
* Pero puede dificultar seguir el flujo

```python
# Con if-else (anidado)
while condicion:
    entrada = obtener_entrada()
    if entrada_valida(entrada):
        procesar(entrada)
    # else implícito: no hacer nada

# Con continue (plano)
while condicion:
    entrada = obtener_entrada()
    if not entrada_valida(entrada):
        continue
    procesar(entrada)
```

Note: Continue es una herramienta más, no siempre la mejor opción. Para casos simples, un if puede ser más claro. Continue brilla cuando evitas múltiples niveles de anidamiento. En este curso, aprende ambos patrones.


### Cuándo evitar continue

* En bucles simples puede complicar más que ayudar
* Múltiples continues son confusos
* Si la lógica es simple, usa if normal

```python
# Innecesariamente complicado
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# Más simple
while i < 10:
    i += 1
    if i % 2 != 0:
        print(i)
```

Note: Como regla general: si el cuerpo del bucle después del continue es pequeño (1-2 líneas), probablemente no necesites continue. Usa continue cuando evite anidar múltiples niveles o cuando hace el flujo más claro.

---

## Bucle FOR


### Estructura básica del for

* Itera sobre elementos de una secuencia
* Más conciso que while para recorrer colecciones
* Automáticamente maneja la variable de iteración

```python
# Iterar sobre una lista
frutas = ['manzana', 'banana', 'cereza']

for fruta in frutas:
    print(fruta)

# Salida:
# manzana
# banana
# cereza
```

Note: El bucle for es más "pythónico" que while para recorrer colecciones. Automáticamente toma cada elemento sin que gestiones un índice. La sintaxis se lee casi como inglés: "para cada fruta en frutas".


### Variable de iteración en for

* Toma el valor de cada elemento automáticamente
* Cambia en cada iteración
* Scope limitado al bucle

```python
# La variable puede llamarse como quieras
nombres = ['Ana', 'Juan', 'María']

for nombre in nombres:
    print(f'Hola {nombre}')
    
# nombre aún existe después del bucle
print(f'Último nombre: {nombre}')  # María
```

Note: La variable de iteración (nombre en este caso) se crea automáticamente y toma cada valor de la secuencia. Aunque técnicamente existe después del bucle, no es buena práctica usarla fuera. Su propósito es solo dentro del for.


### Iterar sobre cadenas

* Las cadenas son secuencias de caracteres
* Podemos iterar carácter por carácter

```python
palabra = "Python"

for letra in palabra:
    print(letra)

# Salida:
# P
# y
# t
# h
# o
# n
```

Note: En Python, las cadenas son secuencias igual que las listas. Cada iteración nos da un carácter. Esto es muy útil para procesar texto carácter por carácter, buscar caracteres específicos, etc.


### Función range() I

* Genera secuencia de números
* `range(fin)`: de 0 a fin-1
* `range(inicio, fin)`: de inicio a fin-1
* `range(inicio, fin, paso)`: con incremento personalizado

```python
# range(5) genera: 0, 1, 2, 3, 4
for i in range(5):
    print(i)

# range(2, 6) genera: 2, 3, 4, 5
for i in range(2, 6):
    print(i)
```

Note: Range es fundamental en Python. No crea una lista en memoria, genera los números bajo demanda (es un generador). Esto lo hace muy eficiente incluso para rangos grandes. Recuerda: el fin nunca se incluye.


### Función range() II

* Con paso podemos contar de 2 en 2, etc.
* El paso puede ser negativo (contar hacia atrás)

```python
# Números pares del 0 al 10
for num in range(0, 11, 2):
    print(num)  # 0, 2, 4, 6, 8, 10

# Cuenta regresiva
for num in range(10, 0, -1):
    print(num)  # 10, 9, 8, ..., 1

# Números impares descendente
for num in range(9, 0, -2):
    print(num)  # 9, 7, 5, 3, 1
```

Note: El tercer parámetro (paso) es muy versátil. Con paso negativo, el inicio debe ser mayor que el fin. Un paso de 2 da números pares (si inicio es par) o impares (si inicio es impar). Puedes usar cualquier valor de paso.


### Ejemplo: Tabla de multiplicar

```python
numero = 7

print(f'Tabla del {numero}:')
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

# Salida:
# Tabla del 7:
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70
```

Note: Este es un ejemplo clásico perfecto para for. Necesitamos exactamente 10 iteraciones, los números del 1 al 10. For con range es ideal. En cada iteración, calculamos y mostramos el resultado.


### Ejemplo: Suma de una lista

```python
numeros = [10, 20, 30, 40, 50]
total = 0

for numero in numeros:
    total += numero

print(f'La suma total es: {total}')  # 150

# Python tiene una función sum() que hace esto:
print(sum(numeros))  # 150
```

Note: Este es el patrón acumulador aplicado a un for. Recorremos cada número y lo sumamos al total. Python tiene sum() incorporado, pero es importante entender cómo funciona por dentro. Este patrón se aplica a muchos otros cálculos.


### For vs While

* For: cuando sabes cuántas iteraciones o iteras colección
* While: cuando la condición de parada es compleja
* For es más conciso y menos propenso a errores

```python
# Imprimir del 1 al 5 con for (preferido)
for i in range(1, 6):
    print(i)

# Mismo resultado con while (más código)
i = 1
while i <= 5:
    print(i)
    i += 1
```

Note: Si puedes usar for, úsalo. Es más simple, más claro y menos propenso a errores (no puedes olvidar actualizar la variable de iteración). While es para cuando la condición de parada no está basada en un contador simple.

---

## Patrones de Bucles


### Patrón: Contador

* Contar elementos que cumplen una condición
* Inicializar contador a 0
* Incrementar cuando se cumple condición

```python
# Contar números pares en una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
contador = 0

for num in numeros:
    if num % 2 == 0:
        contador += 1

print(f'Hay {contador} números pares')  # 5
```

Note: El patrón contador es uno de los más básicos y útiles. Siempre inicializa a 0 antes del bucle. Incrementa solo cuando se cumple tu condición. Al final del bucle, tienes el total de elementos que cumplen la condición.


### Patrón: Acumulador (suma)

* Acumular un total sumando valores
* Inicializar acumulador a 0
* Añadir cada valor en el bucle

```python
# Calcular promedio de notas
notas = [8, 7, 9, 6, 8, 10]
suma = 0

for nota in notas:
    suma += nota

promedio = suma / len(notas)
print(f'Promedio: {promedio:.2f}')  # 8.00
```

Note: El acumulador de suma es crucial para calcular totales, promedios, etc. Siempre inicializa a 0. La diferencia con el contador es que añades el valor del elemento, no solo 1. Este patrón lo usarás constantemente.


### Patrón: Acumulador (producto)

* Acumular multiplicando valores
* Inicializar acumulador a 1 (no 0)
* Multiplicar cada valor

```python
# Calcular factorial de 5 (5! = 5*4*3*2*1)
n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f'{n}! = {factorial}')  # 120
```

Note: Para productos, inicializa a 1 (no 0, porque cualquier cosa por 0 es 0). Este patrón se usa para factoriales, potencias iterativas, etc. Es menos común que la suma pero igual de importante.


### Patrón: Encontrar máximo

* Buscar el valor más grande
* Inicializar a None o al primer elemento
* Actualizar cuando encuentres uno mayor

```python
numeros = [3, 7, 2, 9, 4, 1]
maximo = None

for num in numeros:
    if maximo is None or num > maximo:
        maximo = num

print(f'El máximo es: {maximo}')  # 9

# Python tiene max() incorporado
print(max(numeros))  # 9
```

Note: El patrón de búsqueda de máximo mantiene el "mayor hasta ahora". None como valor inicial significa "aún no hemos visto ninguno". La primera comparación será True automáticamente. Python tiene max(), pero entender el patrón es importante.


### Patrón: Encontrar mínimo

* Buscar el valor más pequeño
* Similar al máximo pero con <

```python
numeros = [3, 7, 2, 9, 4, 1]
minimo = None

for num in numeros:
    if minimo is None or num < minimo:
        minimo = num

print(f'El mínimo es: {minimo}')  # 1

# Python tiene min() incorporado
print(min(numeros))  # 1
```

Note: El patrón de mínimo es idéntico al de máximo pero invirtiendo la comparación. Ambos patrones son fundamentales en análisis de datos, procesamiento de listas, etc. Entiende cómo funcionan aunque uses min() y max().


### Patrón: Búsqueda (encontrar elemento)

* Buscar si existe un elemento específico
* Usar bandera booleana
* Detener cuando se encuentra (opcional)

```python
numeros = [3, 7, 2, 9, 4, 1]
buscar = 9
encontrado = False

for num in numeros:
    if num == buscar:
        encontrado = True
        break  # Opcional: detener búsqueda

if encontrado:
    print(f'{buscar} está en la lista')
else:
    print(f'{buscar} no está en la lista')

# Python: usar 'in'
print(buscar in numeros)  # True
```

Note: Este patrón usa una bandera booleana. La inicializas a False y la cambias a True si encuentras el elemento. Break es opcional pero eficiente: ¿para qué seguir buscando si ya lo encontraste? Python tiene el operador 'in' pero este patrón es útil para búsquedas más complejas.


### Patrón: Filtrado

* Crear nueva colección con elementos que cumplen condición
* Inicializar lista vacía
* Añadir elementos que cumplen

```python
# Obtener solo números pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)

print(pares)  # [2, 4, 6, 8, 10]

# Python: list comprehension
pares = [num for num in numeros if num % 2 == 0]
```

Note: El patrón de filtrado es esencial para procesar datos. Creas una nueva lista vacía y añades solo los elementos que cumplen tu criterio. Python tiene list comprehensions que hacen esto más conciso, pero este patrón es la base.

---

## Bucles Anidados


### Concepto de anidamiento

* Un bucle dentro de otro bucle
* El bucle interno se ejecuta completamente en cada iteración del externo
* Potencia el número de iteraciones (multiplicativo)

```python
# Bucle anidado simple
for i in range(1, 4):        # Externo: 3 iteraciones
    for j in range(1, 3):    # Interno: 2 iteraciones
        print(f'i={i}, j={j}')

# Total de prints: 3 * 2 = 6
```

Note: Los bucles anidados multiplican el número de iteraciones. Si el externo hace 3 vueltas y el interno 2, tendrás 3×2=6 iteraciones totales. Esto crece rápidamente: dos bucles de 100 son 10,000 iteraciones.


### Ejemplo: Tabla de multiplicar completa

```python
# Tabla del 1 al 5
for i in range(1, 6):
    print(f'\nTabla del {i}:')
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')

# El bucle interno (j) se ejecuta completo
# para cada valor de i
```

Note: Este es un uso clásico de bucles anidados. Para cada número del bucle externo, mostramos su tabla completa (bucle interno). El bucle interno se ejecuta 10 veces para i=1, luego 10 veces para i=2, etc. Total: 5×10=50 líneas.


### Ejemplo: Matriz de caracteres I

```python
# Imprimir un cuadrado de 5x5
filas = 5
columnas = 5

for i in range(filas):
    for j in range(columnas):
        print('* ', end='')
    print()  # Nueva línea al final de cada fila

# Salida:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
```

Note: Este patrón es muy común para trabajar con estructuras 2D. El bucle externo controla las filas, el interno las columnas. El print sin argumentos al final de cada fila hace el salto de línea.


### Ejemplo: Matriz de caracteres II

```python
# Triángulo creciente
for i in range(1, 6):
    for j in range(i):
        print('* ', end='')
    print()

# Salida:
# *
# * *
# * * *
# * * * *
# * * * * *
```

Note: Aquí el número de iteraciones del bucle interno depende del valor de i del bucle externo. En la primera fila (i=1) se imprime 1 asterisco, en la segunda (i=2) se imprimen 2, etc. Esto crea el patrón triangular.


### Ejemplo: Combinaciones

```python
# Todas las combinaciones de dos listas
colores = ['rojo', 'verde', 'azul']
tamaños = ['S', 'M', 'L']

for color in colores:
    for tamaño in tamaños:
        print(f'Camiseta {color} talla {tamaño}')

# Salida: 9 combinaciones (3 colores × 3 tallas)
```

Note: Los bucles anidados son perfectos para generar todas las combinaciones de dos o más conjuntos. Cada color se combina con cada talla. En bases de datos o comercio electrónico, este patrón aparece constantemente.


### Ejemplo: Buscar en matriz

```python
# Buscar un valor en una matriz (lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

buscar = 5
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == buscar:
            print(f'Encontrado en [{i}][{j}]')
            encontrado = True
            break
    if encontrado:
        break
```

Note: Buscar en matrices requiere bucles anidados. Recorremos cada fila y dentro de cada fila, cada columna. El doble break sale de ambos bucles una vez encontrado el valor. Esto es común en procesamiento de imágenes, juegos de tablero, etc.


### Complejidad de bucles anidados

* Dos bucles de n: O(n²) - cuadrático
* Tres bucles de n: O(n³) - cúbico
* Crece rápidamente, cuidado con n grandes

```python
# Con n=100, este bucle hace 10,000 operaciones
n = 100
for i in range(n):
    for j in range(n):
        pass  # Alguna operación

# Con tres bucles: 1,000,000 de operaciones!
```

Note: La complejidad computacional es importante. Dos bucles de 10 son 100 operaciones. De 100 son 10,000. De 1000 son 1,000,000. Los bucles anidados pueden hacer que programas sean muy lentos si no tienes cuidado con el tamaño de los datos.

---

## Ejercicios Aplicados


### Ejercicio 1: Suma de números

Escribe un programa que sume todos los números del 1 al 100 usando un bucle while y luego verifica el resultado con for.

```python
# Tu código aquí con while

# Tu código aquí con for
```

Note: Este ejercicio practica ambos tipos de bucles para la misma tarea. También puedes verificar tu resultado con la fórmula n(n+1)/2. Para 100 números, debería dar 5050.


### Ejercicio 2: Números primos

Crea un programa que encuentre todos los números primos entre 1 y 50. Un número primo solo es divisible por 1 y por sí mismo.

```python
# Tu código aquí
```

Note: Este ejercicio combina bucles con condicionales. Para cada número, necesitas verificar si tiene divisores (bucle interno). Si un número es divisible por algo entre 2 y él-1, no es primo.


### Ejercicio 3: Factorial

Implementa una función que calcule el factorial de un número usando un bucle. El factorial de n (n!) es n × (n-1) × (n-2) × ... × 1.

```python
def factorial(n):
    # Tu código aquí
    pass

print(factorial(5))  # Debería dar 120
```

Note: Recuerda que el factorial requiere un acumulador inicializado a 1, no a 0. Multiplica los números del 1 hasta n. El factorial de 0 es 1 por definición. Piensa en cómo manejar números negativos (no tienen factorial).


### Ejercicio 4: Validación con reintento

Escribe un programa que pida un número entre 1 y 10 al usuario. Si introduce un valor inválido, debe volver a preguntar hasta que sea correcto.

```python
# Tu código aquí
```

Note: Este ejercicio practica validación de entrada con bucles. Necesitas un while que continúe hasta que la entrada sea válida. También necesitas try-except para manejar si el usuario introduce texto en lugar de número.


### Ejercicio 5: Pirámide de números

Crea un programa que imprima una pirámide de números como esta (hasta el número que el usuario elija):

```
1
12
123
1234
12345
```

```python
# Tu código aquí
```

Note: Este ejercicio usa bucles anidados. El bucle externo controla las filas, el interno imprime los números de cada fila. Necesitas imprimir los números sin espacios y sin salto de línea hasta terminar la fila.


### Ejercicio 6: Adivinar número

Implementa un juego donde el programa elige un número aleatorio entre 1 y 100, y el usuario debe adivinarlo. El programa indica si el número es mayor o menor.

```python
import random
# Tu código aquí
```

Note: Este ejercicio combina bucles, condicionales y aleatoriedad. Usa random.randint(1, 100) para generar el número. El bucle continúa hasta que el usuario adivine. Cuenta cuántos intentos tomó. Opcionalmente, limita los intentos máximos.

---

## Buenas Prácticas


### Elegir el bucle apropiado

* For: conoces el número de iteraciones o iteras colección
* While: condición de parada compleja o desconocida
* Preferir for cuando sea posible

```python
# Bien: usar for para iterar lista
for nombre in nombres:
    print(nombre)

# Innecesario: usar while para esto
i = 0
while i < len(nombres):
    print(nombres[i])
    i += 1
```

Note: For es más "pythónico" y menos propenso a errores. Úsalo siempre que iteres una colección o sepas el número de iteraciones. While es para situaciones más complejas donde la condición de parada no es un simple contador.


### Nombres descriptivos para variables de iteración

* i, j, k: solo para índices simples
* Nombres descriptivos para elementos

```python
# Poco claro
for i in usuarios:
    procesar(i)

# Claro
for usuario in usuarios:
    procesar(usuario)

# Índices: i, j, k está bien
for i in range(10):
    for j in range(10):
        matriz[i][j] = 0
```

Note: Cuando iteras elementos, usa nombres que describan qué es cada elemento. Cuando usas índices numéricos, i, j, k son convencionalmente aceptados. La legibilidad es más importante que la brevedad.


### Evitar modificar la colección durante iteración

* Modificar la lista que estás iterando puede causar errores
* Crea una nueva lista o itera sobre una copia

```python
# Peligroso: modificar mientras iteras
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # ¡Problema!

# Seguro: iterar sobre copia
for num in numeros[:]:  # [:] crea copia
    if num % 2 == 0:
        numeros.remove(num)

# Mejor: crear nueva lista
numeros = [num for num in numeros if num % 2 != 0]
```

Note: Modificar una colección mientras la iteras puede saltarse elementos o causar errores. Si necesitas modificar, itera sobre una copia (lista[:]) o mejor aún, crea una nueva lista con los elementos que quieres mantener.


### Limitar profundidad de anidamiento

* Máximo 2-3 niveles
* Más niveles: extraer a funciones
* Usar continue/break para reducir anidamiento

```python
# Difícil de leer: muy anidado
for i in range(n):
    if condicion1:
        for j in range(m):
            if condicion2:
                for k in range(p):
                    if condicion3:
                        # Código muy adentro

# Mejor: extraer a función
def procesar_elemento(i):
    if not condicion1:
        return
    for j in range(m):
        procesar_fila(i, j)
```

Note: El anidamiento excesivo hace el código difícil de leer y mantener. Si necesitas más de 2-3 niveles, probablemente deberías extraer lógica a funciones separadas. Cada función debe hacer una cosa y hacerla bien.


### Comentar bucles complejos

* Explicar qué hace el bucle
* Documentar invariantes importantes
* Aclarar bucles anidados

```python
# Buscar todos los pares de números que suman el objetivo
objetivo = 10
numeros = [1, 5, 3, 7, 2, 8]

# Para cada número, buscar si existe su complemento
for i in range(len(numeros)):
    complemento = objetivo - numeros[i]
    for j in range(i+1, len(numeros)):
        if numeros[j] == complemento:
            print(f'{numeros[i]} + {numeros[j]} = {objetivo}')
```

Note: Los bucles simples no necesitan comentarios, pero los bucles con lógica compleja sí. Explica qué estás buscando o calculando, no cómo lo haces (eso ya lo muestra el código). Los invariantes (condiciones que se mantienen) son especialmente importantes de documentar.


### Optimización: evitar trabajo redundante

* Calcular fuera del bucle lo que no cambia
* Almacenar resultados que se reutilizan
* Romper bucles cuando hayas terminado

```python
# Ineficiente: calcula len() en cada iteración
for i in range(len(lista)):
    # usar lista[i]

# Eficiente: calcula len() una vez
n = len(lista)
for i in range(n):
    # usar lista[i]

# Mejor aún: iterar directamente
for elemento in lista:
    # usar elemento
```

Note: Los bucles se ejecutan muchas veces, así que pequeñas ineficiencias se multiplican. Saca del bucle cualquier cálculo que no cambie. Sin embargo, no optimices prematuramente: primero haz que funcione, luego hazlo rápido si es necesario.

---

## Depuración de Bucles


### Print para seguir iteraciones

* Imprimir valores de variables de iteración
* Ver cuántas veces se ejecuta
* Verificar que la condición cambie correctamente

```python
suma = 0
for i in range(1, 6):
    print(f'Iteración {i}: suma antes = {suma}')
    suma += i
    print(f'Iteración {i}: suma después = {suma}')

print(f'Suma final: {suma}')
```

Note: Prints estratégicos son tu primera herramienta de depuración. Muestra el valor de la variable de iteración y variables importantes al inicio y fin de cada iteración. Esto te ayuda a ver si el bucle hace lo que esperas.


### Verificar condiciones de terminación

* Asegurar que la condición eventualmente sea False
* Verificar que las variables cambien correctamente
* Comprobar casos límite

```python
# ¿Este bucle terminará?
i = 0
while i < 10:
    print(i)
    # ¿Olvidé i += 1?
    
# Agregar print para verificar
print(f'i vale {i} después del bucle')
```

Note: Si tu programa se "cuelga", probablemente sea un bucle infinito. Verifica que: (1) la variable de la condición cambie, (2) cambie en la dirección correcta, (3) eventualmente cumpla la condición de salida. Los casos límite (listas vacías, 0 iteraciones) son fuente común de bugs.


### Usar el depurador

* Establecer breakpoint en la línea del bucle
* Ejecutar iteración por iteración
* Inspeccionar variables en cada paso

Note: Un depurador gráfico es más potente que prints. Puedes pausar en cada iteración, inspeccionar todas las variables, y avanzar paso a paso. Aprende a usar el depurador de tu IDE (VSCode, PyCharm, etc.). Es una habilidad que te ahorrará horas de frustración.


### Errores comunes: Off-by-one

* Ejecutar una iteración de más o de menos
* Muy común con rangos e índices

```python
# Error: se salta el último elemento
lista = [1, 2, 3, 4, 5]
for i in range(len(lista) - 1):  # ¡Falta el último!
    print(lista[i])

# Correcto
for i in range(len(lista)):
    print(lista[i])

# Mejor aún
for elemento in lista:
    print(elemento)
```

Note: Los errores "off-by-one" son extremadamente comunes. Recuerda: range(n) va de 0 a n-1, no incluye n. Si tienes una lista de 5 elementos (índices 0-4), usa range(5) o range(len(lista)). Cuando sea posible, itera directamente sobre la colección en lugar de usar índices.


### Errores comunes: Confundir for y while

* Usar while cuando for sería más simple
* Olvidar actualizar contador en while

```python
# Complicado con while
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

# Simple con for
for elemento in lista:
    print(elemento)
```

Note: Si estás escribiendo un while con un contador que solo incrementas, probablemente deberías usar for. While es para condiciones más complejas. Este error es común en principiantes que vienen de lenguajes como C donde for es más complicado.


### Testing de bucles

* Probar con 0 iteraciones (lista vacía)
* Probar con 1 iteración
* Probar con muchas iteraciones

```python
def suma_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total

# Casos de prueba
assert suma_lista([]) == 0        # Lista vacía
assert suma_lista([5]) == 5       # Un elemento
assert suma_lista([1,2,3]) == 6   # Varios elementos
```

Note: Los casos límite revelan muchos bugs. Siempre prueba: (1) entrada vacía/cero iteraciones, (2) un solo elemento, (3) dos elementos, (4) muchos elementos. Muchos bugs aparecen solo en estos casos extremos.

---

## Resumen


### Conceptos fundamentales

* While: repite mientras condición sea True
* For: itera sobre secuencias
* Break: sale del bucle inmediatamente
* Continue: salta a la siguiente iteración
* Range(): genera secuencias de números

Note: Estos son los conceptos core de bucles en Python. Domínalos y podrás expresar cualquier patrón de repetición. While es el más fundamental, for es el más usado, break y continue son herramientas adicionales.


### Patrones esenciales

* Contador: contar elementos
* Acumulador: sumar/multiplicar valores
* Búsqueda: encontrar elementos
* Máximo/mínimo: valores extremos
* Filtrado: seleccionar elementos

Note: Estos patrones aparecen una y otra vez en programación. Memoriza sus estructuras básicas. La mayoría de problemas con bucles son variaciones de estos patrones. Una vez los reconozcas, programar será más fácil.


### Mejores prácticas recordadas

* Preferir for sobre while cuando sea posible
* Nombres descriptivos para variables de iteración
* Evitar anidamiento excesivo (máx 2-3 niveles)
* Comentar lógica compleja
* Probar casos límite (0, 1, muchos elementos)

Note: Las buenas prácticas hacen tu código más legible, mantenible y menos propenso a bugs. No son opcionales: son la diferencia entre código profesional y código amateur. Adóptalas desde el principio.


### Depuración

* Prints estratégicos para seguir el flujo
* Verificar que condiciones cambien correctamente
* Usar depurador para casos complejos
* Cuidado con bucles infinitos y off-by-one
* Probar con diferentes tamaños de entrada

Note: La depuración de bucles puede ser frustrante al principio. Desarrolla un proceso sistemático: verifica las condiciones, sigue las variables clave, prueba casos simples primero. Con práctica, encontrarás y arreglarás bugs más rápidamente.


### Próximos pasos

* Practicar con ejercicios variados
* Aprender list comprehensions (bucles más concisos)
* Combinar bucles con funciones
* Estudiar algoritmos de ordenamiento y búsqueda
* Trabajar con estructuras de datos más complejas

Note: Los bucles son fundamentales para todo lo que viene después. Practica hasta que se vuelvan naturales. Los próximos temas (excepciones, funciones, estructuras de datos) construyen sobre este conocimiento.

---

## ¿Preguntas?

Note: Los bucles son un tema extenso y con muchas sutilezas. Asegúrate de que todos los conceptos queden claros. Anima a los estudiantes a compartir sus dudas y errores comunes que hayan encontrado. Aprender de los errores de otros también es valioso.
