# U3.0 - Cadenas de Texto

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son las cadenas?

* Secuencia ordenada de caracteres
* Tipo de dato fundamental en programación
* En Python se crean con comillas simples o dobles
* Son objetos inmutables
* Tienen muchos métodos útiles incorporados

Note: Las cadenas (strings) son uno de los tipos de datos más usados en programación. Representan texto: nombres, mensajes, datos, etc. En Python son objetos de la clase str y tienen características especiales que las hacen muy potentes.


### Crear cadenas en Python

```python
# Con comillas simples
nombre = 'Ana'

# Con comillas dobles
apellido = "García"

# Con comillas triples (multilínea)
parrafo = '''Este es un texto
que ocupa varias
líneas'''

# Cadena vacía
vacia = ''
```

Note: Python es flexible con las comillas. Usa simples o dobles indistintamente. Las comillas triples permiten cadenas de múltiples líneas, útiles para documentación o textos largos. La cadena vacía es válida y tiene longitud 0.


### Caracteres especiales

```python
# Salto de línea
texto = 'Primera línea\nSegunda línea'

# Tabulación
columnas = 'Nombre\tEdad\tCiudad'

# Comillas dentro de cadenas
dialogo = "Ella dijo: 'Hola'"
alternativa = 'El libro "Python" es bueno'

# Barra invertida literal
ruta = 'C:\\Users\\Ana\\Documents'
```

Note: \n inserta salto de línea, \t inserta tabulación. Para incluir comillas dentro de una cadena, usa el otro tipo de comillas o escápala con \. La barra invertida se escapa como \\.

---

## Acceso a Caracteres


### Indexación básica

* Los índices comienzan en 0
* Cada carácter tiene una posición
* Acceso con corchetes []
* Índices fuera de rango causan error

```python
palabra = 'Python'
print(palabra[0])   # 'P' - primer carácter
print(palabra[1])   # 'y' - segundo carácter
print(palabra[5])   # 'n' - sexto carácter
# palabra[6]  # IndexError: fuera de rango
```

Note: La indexación comienza en 0, no en 1. Es la convención en la mayoría de lenguajes de programación. El primer carácter está en índice 0, el segundo en 1, etc. Intentar acceder a un índice que no existe lanza IndexError.


### Índices negativos

* -1 es el último carácter
* -2 es el penúltimo
* Útil para acceder desde el final

```python
palabra = 'Python'
print(palabra[-1])   # 'n' - último
print(palabra[-2])   # 'o' - penúltimo
print(palabra[-6])   # 'P' - primer carácter (desde final)

# Equivalencias:
# palabra[0] == palabra[-6]
# palabra[5] == palabra[-1]
```

Note: Los índices negativos son muy convenientes cuando quieres acceder a caracteres desde el final sin saber la longitud exacta. -1 siempre es el último carácter, -2 el penúltimo, etc.


### Rebanado (Slicing) I

* Extrae subcadenas
* Sintaxis: [inicio:fin]
* Incluye inicio, excluye fin
* Índices opcionales

```python
texto = 'Python es genial'

print(texto[0:6])    # 'Python' (índices 0-5)
print(texto[7:9])    # 'es' (índices 7-8)
print(texto[10:16])  # 'genial' (índices 10-15)
```

Note: El slicing extrae una porción de la cadena. La sintaxis [inicio:fin] incluye el carácter en inicio pero excluye el de fin. Si quieres caracteres 0-5, usa [0:6]. Esto es consistente con range().


### Rebanado (Slicing) II

```python
palabra = 'Programación'

# Desde inicio hasta posición
print(palabra[:7])      # 'Progra' (índices 0-6)

# Desde posición hasta final
print(palabra[7:])      # 'mación' (índice 7 hasta el final)

# Toda la cadena (copia)
print(palabra[:])       # 'Programación'

# Con negativos
print(palabra[-6:])     # 'mación' (últimos 6 caracteres)
print(palabra[:-6])     # 'Progra' (excepto últimos 6)
```

Note: Si omites inicio, se asume 0. Si omites fin, se asume hasta el final. palabra[:] crea una copia de la cadena completa. Los índices negativos también funcionan en slicing.


### Rebanado con paso

* Tercer parámetro: paso
* Sintaxis: [inicio:fin:paso]
* Paso por defecto es 1
* Paso negativo invierte

```python
numeros = '0123456789'

print(numeros[::2])     # '02468' (de 2 en 2)
print(numeros[1::2])    # '13579' (impares)
print(numeros[::3])     # '0369' (de 3 en 3)

# Invertir cadena
print(numeros[::-1])    # '9876543210'
palabra = 'Python'
print(palabra[::-1])    # 'nohtyP'
```

Note: El tercer parámetro es el paso o salto. [::2] toma cada segundo carácter. El truco [::-1] invierte la cadena porque recorre de atrás hacia adelante con paso -1. Es un idioma muy pythónico.

---

## Inmutabilidad


### Las cadenas son inmutables

* No se pueden modificar después de creadas
* Intentar cambiar un carácter causa error
* Debes crear una nueva cadena para "modificar"

```python
nombre = 'Ana'

# Esto causa error:
# nombre[0] = 'J'  # TypeError: 'str' object does not support item assignment

# Solución: crear nueva cadena
nuevo_nombre = 'J' + nombre[1:]
print(nuevo_nombre)  # 'Jna'
```

Note: La inmutabilidad significa que una vez creada una cadena, no puedes cambiar sus caracteres. Esto puede parecer limitante pero tiene ventajas: seguridad, eficiencia, y permite usar cadenas como claves de diccionarios. Para "modificar", creas una nueva.


### Consecuencias de la inmutabilidad

```python
# Cada operación crea una nueva cadena
saludo = 'Hola'
saludo = saludo + ' mundo'  # Nueva cadena
saludo = saludo.upper()      # Nueva cadena
saludo = saludo.replace('O', 'o')  # Nueva cadena

# Las variables apuntan a diferentes objetos
a = 'Python'
b = a
b = 'Java'
print(a)  # 'Python' (a no cambió)
```

Note: Cada operación que "modifica" una cadena realmente crea una nueva. La variable original puede quedarse con la cadena vieja o puede reasignarse a la nueva. Esto es importante entenderlo para optimización: concatenar muchas cadenas en un bucle es ineficiente.

---

## Operaciones con Cadenas


### Concatenación (+)

* Unir cadenas con el operador +
* Crea una nueva cadena
* No añade espacios automáticamente

```python
nombre = 'Ana'
apellido = 'García'

# Concatenación básica
nombre_completo = nombre + apellido
print(nombre_completo)  # 'AnaGarcía' (sin espacio)

# Con espacio
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)  # 'Ana García'

# Múltiples concatenaciones
mensaje = 'Hola, ' + 'mi ' + 'nombre ' + 'es ' + nombre
```

Note: El operador + une cadenas. No añade espacios ni separadores automáticamente, debes añadirlos explícitamente. Puedes concatenar cuantas cadenas quieras, pero recuerda que cada + crea una nueva cadena.


### Repetición (*)

* Repetir cadenas con el operador *
* Útil para patrones y separadores

```python
# Repetir caracteres
linea = '-' * 40
print(linea)  # '----------------------------------------'

# Repetir palabras
eco = 'Hola ' * 3
print(eco)  # 'Hola Hola Hola '

# Casos especiales
print('Python' * 0)   # '' (cadena vacía)
print('Python' * 1)   # 'Python'
# 'Python' * -1  # '' (negativos dan cadena vacía)
```

Note: El operador * repite una cadena n veces. Es útil para crear separadores, líneas decorativas, o patrones repetitivos. Multiplicar por 0 o negativo da cadena vacía. Multiplicar por 1 da la misma cadena.


### Longitud (len)

* Función len() devuelve número de caracteres
* Incluye espacios y caracteres especiales
* Útil para validaciones y bucles

```python
nombre = 'Ana'
print(len(nombre))  # 3

mensaje = 'Hola mundo'
print(len(mensaje))  # 10 (incluye el espacio)

vacia = ''
print(len(vacia))  # 0

# Con caracteres especiales
texto = 'Primera\nSegunda'
print(len(texto))  # 15 (\n cuenta como 1)
```

Note: len() es una función incorporada que devuelve la longitud. Los espacios cuentan como caracteres. Los caracteres especiales como \n cuentan como un solo carácter aunque se escriban con dos. len() es O(1), muy eficiente.


### Operador in

* Verifica si una subcadena existe
* Devuelve True o False
* Sensible a mayúsculas/minúsculas

```python
frase = 'Python es genial'

print('Python' in frase)     # True
print('Java' in frase)       # False
print('ES' in frase)         # False (case-sensitive)
print('es' in frase)         # True

# También funciona not in
print('Ruby' not in frase)   # True
print('Python' not in frase) # False
```

Note: El operador in es muy útil para verificar si una cadena contiene una subcadena. Es case-sensitive (distingue mayúsculas/minúsculas). El operador not in es la negación, verifica que NO esté contenido.


### Comparación de cadenas

* Operadores: ==, !=, <, >, <=, >=
* Comparación lexicográfica (alfabética)
* Sensible a mayúsculas

```python
# Igualdad
print('Python' == 'Python')     # True
print('Python' == 'python')     # False

# Orden alfabético
print('A' < 'B')                # True
print('Python' < 'Ruby')        # True (P < R)
print('apple' < 'banana')       # True

# Mayúsculas vs minúsculas
print('A' < 'a')                # True (mayúsculas van antes)
```

Note: La comparación con == es exacta. Los operadores <, > comparan lexicográficamente (orden alfabético). Las mayúsculas vienen antes que minúsculas en el orden Unicode. Esto es útil para ordenar listas de cadenas.

---

## Métodos de Cadenas I


### Cambiar mayúsculas/minúsculas

```python
texto = 'Python Es Genial'

# Convertir a mayúsculas
print(texto.upper())      # 'PYTHON ES GENIAL'

# Convertir a minúsculas  
print(texto.lower())      # 'python es genial'

# Capitalizar (primera letra mayúscula)
print(texto.capitalize()) # 'Python es genial'

# Title case (primera de cada palabra)
print(texto.title())      # 'Python Es Genial'

# Invertir mayúsculas/minúsculas
print(texto.swapcase())   # 'pYTHON eS gENIAL'
```

Note: Estos métodos devuelven una nueva cadena, no modifican la original. upper() y lower() son útiles para comparaciones case-insensitive. capitalize() solo afecta la primera letra. title() capitaliza cada palabra.


### Buscar subcadenas

```python
frase = 'Python es un lenguaje de programación'

# Encontrar posición (devuelve índice)
print(frase.find('un'))           # 10
print(frase.find('Java'))         # -1 (no encontrado)

# Index (lanza excepción si no encuentra)
print(frase.index('Python'))      # 0
# frase.index('Java')  # ValueError

# Contar ocurrencias
print(frase.count('a'))           # 4
print(frase.count('Python'))      # 1
```

Note: find() devuelve el índice de la primera ocurrencia o -1 si no encuentra. index() hace lo mismo pero lanza ValueError si no encuentra. count() cuenta cuántas veces aparece una subcadena. Todos son case-sensitive.


### Verificar contenido

```python
# Verificar tipos de caracteres
print('Python'.isalpha())      # True (solo letras)
print('Python3'.isalpha())     # False (tiene número)
print('12345'.isdigit())       # True (solo dígitos)
print('Python3'.isalnum())     # True (letras y números)

# Verificar formato
print('PYTHON'.isupper())      # True
print('python'.islower())      # True
print('   '.isspace())         # True (solo espacios)
print('Python Es'.istitle())   # True
```

Note: Estos métodos booleanos verifican el contenido de la cadena. isalpha() verifica solo letras, isdigit() solo dígitos, isalnum() letras o dígitos. isupper/islower verifican mayúsculas/minúsculas. isspace() verifica espacios en blanco.

---

## Métodos de Cadenas II


### Reemplazar texto

```python
texto = 'Python es genial. Python es poderoso.'

# Reemplazar todas las ocurrencias
nuevo = texto.replace('Python', 'Java')
print(nuevo)  # 'Java es genial. Java es poderoso.'

# Reemplazar número limitado de veces
limitado = texto.replace('Python', 'Java', 1)
print(limitado)  # 'Java es genial. Python es poderoso.'

# Reemplazar varios caracteres
codigo = '1234567890'
print(codigo.replace('1', 'X').replace('0', 'O'))
```

Note: replace() sustituye todas las ocurrencias de una subcadena por otra. El tercer parámetro opcional limita cuántas sustituciones hacer. Puedes encadenar múltiples replace() pero puede ser ineficiente. Para muchos reemplazos, considera usar expresiones regulares.


### Eliminar espacios

```python
texto = '   Python   '

# Eliminar espacios de ambos lados
print(texto.strip())        # 'Python'

# Solo de la izquierda
print(texto.lstrip())       # 'Python   '

# Solo de la derecha
print(texto.rstrip())       # '   Python'

# Eliminar otros caracteres
print('###Python###'.strip('#'))  # 'Python'
print('...texto...'.strip('.'))   # 'texto'
```

Note: strip() elimina espacios en blanco (y otros caracteres especificados) de los extremos. lstrip() solo izquierda, rstrip() solo derecha. Por defecto eliminan espacios, tabs, saltos de línea. Puedes especificar qué caracteres eliminar.


### Dividir cadenas (split)

```python
# Dividir por espacios (por defecto)
frase = 'Python es genial'
palabras = frase.split()
print(palabras)  # ['Python', 'es', 'genial']

# Dividir por otro separador
fecha = '25/10/2024'
partes = fecha.split('/')
print(partes)  # ['25', '10', '2024']

# Limitar divisiones
texto = 'uno:dos:tres:cuatro'
print(texto.split(':', 2))  # ['uno', 'dos', 'tres:cuatro']
```

Note: split() divide una cadena en una lista de subcadenas. Por defecto divide por espacios en blanco. Puedes especificar cualquier separador. El segundo parámetro limita cuántas divisiones hacer. Muy útil para procesar datos CSV, logs, etc.


### Unir cadenas (join)

```python
# Unir lista de cadenas
palabras = ['Python', 'es', 'genial']
frase = ' '.join(palabras)
print(frase)  # 'Python es genial'

# Unir con otros separadores
print('-'.join(palabras))    # 'Python-es-genial'
print(', '.join(palabras))   # 'Python, es, genial'

# Unir números (convertir primero)
numeros = [1, 2, 3]
# ','.join(numeros)  # TypeError: esperaba str
print(','.join(str(n) for n in numeros))  # '1,2,3'
```

Note: join() es el opuesto de split(). Une una lista de cadenas usando un separador. El separador va antes de .join(). Solo funciona con cadenas, debes convertir otros tipos primero. Es más eficiente que concatenar en bucle.


### Formato de cadenas

```python
# Justificar
print('Python'.center(20, '-'))  # '-------Python-------'
print('Python'.ljust(10))        # 'Python    '
print('Python'.rjust(10))        # '    Python'

# Rellenar con ceros
print('42'.zfill(5))             # '00042'
print('-42'.zfill(5))            # '-0042'

# Partir líneas
texto = 'Primera\nSegunda\nTercera'
lineas = texto.splitlines()
print(lineas)  # ['Primera', 'Segunda', 'Tercera']
```

Note: center(), ljust(), rjust() justifican texto. zfill() rellena con ceros a la izquierda, útil para formatear números. splitlines() divide por saltos de línea, útil para procesar archivos de texto línea por línea.

---

## F-Strings y Formato


### F-strings (Python 3.6+)

* Forma moderna y legible de formatear
* Expresiones dentro de {}
* Pueden contener cualquier expresión Python

```python
nombre = 'Ana'
edad = 25

# Formato básico
mensaje = f'Me llamo {nombre} y tengo {edad} años'
print(mensaje)

# Con expresiones
print(f'En 5 años tendré {edad + 5} años')
print(f'{nombre.upper()} tiene {len(nombre)} letras')

# Llamadas a funciones
print(f'Ahora son las {datetime.now()}')
```

Note: F-strings son la forma recomendada de formatear cadenas en Python moderno. Son más legibles que % o format(). Puedes poner cualquier expresión Python dentro de {}. Se evalúan en tiempo de ejecución.


### Formato numérico con f-strings

```python
# Decimales
pi = 3.14159265359
print(f'Pi es aproximadamente {pi:.2f}')  # 3.14
print(f'Pi con 4 decimales: {pi:.4f}')    # 3.1416

# Porcentajes
tasa = 0.1547
print(f'Tasa: {tasa:.2%}')                # 15.47%

# Formato de miles
grande = 1000000
print(f'{grande:,}')                      # 1,000,000

# Notación científica
print(f'{grande:.2e}')                    # 1.00e+06
```

Note: Después de : especificas el formato. .2f significa float con 2 decimales. % multiplica por 100 y añade signo de porcentaje. , añade separadores de miles. e es notación científica.


### Alineación con f-strings

```python
# Alineación
nombre = 'Python'
print(f'{nombre:<10}')   # 'Python    ' (izquierda)
print(f'{nombre:>10}')   # '    Python' (derecha)
print(f'{nombre:^10}')   # '  Python  ' (centro)

# Con carácter de relleno
print(f'{nombre:*^10}')  # '**Python**'

# Tablas formateadas
print(f'{"Nombre":<10} {"Edad":>5}')
print(f'{"Ana":<10} {25:>5}')
print(f'{"Roberto":<10} {30:>5}')
```

Note: < alinea izquierda, > derecha, ^ centro. El número indica el ancho total. Puedes especificar carácter de relleno antes del símbolo de alineación. Útil para crear tablas formateadas en consola.


### Método format() (alternativa)

```python
# Formato básico
texto = 'Me llamo {} y tengo {} años'.format('Ana', 25)

# Con índices
texto = '{0} estudia {1} y {0} practica {1}'.format('Ana', 'Python')

# Con nombres
texto = '{nombre} tiene {edad} años'.format(nombre='Ana', edad=25)

# Aunque format() funciona, f-strings son más legibles
```

Note: format() es el método antiguo de formateo. Todavía funciona y lo verás en código antiguo, pero f-strings son preferibles por legibilidad. format() es útil cuando la plantilla y los datos están separados.

---

## Caracteres Unicode


### Unicode en Python

* Python 3 usa Unicode por defecto
* Soporta caracteres de todos los idiomas
* Emojis y símbolos especiales

```python
# Caracteres internacionales
print('Español: ñ, á, é, í, ó, ú')
print('Francés: à, è, ù, ç')
print('Griego: α, β, γ, δ')
print('Chino: 你好')
print('Árabe: مرحبا')

# Emojis
print('Python 🐍')
print('Feliz 😊')
```

Note: Python 3 maneja Unicode nativamente. Puedes usar cualquier carácter Unicode en tus cadenas sin configuración especial. Esto incluye letras acentuadas, alfabetos no latinos, emojis, y símbolos matemáticos.


### Secuencias de escape Unicode

```python
# Por código Unicode
print('\u0041')        # 'A'
print('\u03B1')        # 'α' (alpha griega)
print('\u4E2D')        # '中' (chino)

# Por nombre Unicode
print('\N{GREEK SMALL LETTER ALPHA}')  # 'α'
print('\N{SNAKE}')                     # '🐍'

# Obtener código de un carácter
print(ord('A'))        # 65
print(ord('α'))        # 945
print(chr(65))         # 'A'
```

Note: \u permite insertar caracteres por su código Unicode hexadecimal. \N permite usar el nombre Unicode oficial. ord() obtiene el código numérico de un carácter, chr() hace lo opuesto. Útil para trabajar con caracteres especiales programáticamente.

---

## Cadenas Crudas (Raw Strings)


### Raw strings con r

* Prefijo r antes de la cadena
* Ignora secuencias de escape
* Útil para rutas y expresiones regulares

```python
# Sin r - procesa escapes
print('C:\nombre\texto')      # Error: \n, \t son escapes

# Con r - literal
print(r'C:\nombre\texto')     # 'C:\nombre\texto'

# Rutas de Windows
ruta = r'C:\Users\Ana\Documents\file.txt'

# Expresiones regulares (veremos más adelante)
patron = r'\d{3}-\d{2}-\d{4}'  # Patrón de SSN
```

Note: Las raw strings tratan las barras invertidas como caracteres literales, no como inicios de secuencias de escape. Son esenciales para rutas de Windows y expresiones regulares donde \ es común. El prefijo r puede usarse con comillas simples, dobles o triples.

---

## Ejercicios Propuestos


### Ejercicio 1: Validador de Email

Escribe una función que valide si una cadena es un email válido básico (contiene @ y un punto después del @).

```python
def es_email_valido(email):
    # Tu código aquí
    pass

# Pruebas
print(es_email_valido('usuario@ejemplo.com'))  # True
print(es_email_valido('invalido.com'))         # False
print(es_email_valido('sin@punto'))            # False
```

Note: Este ejercicio practica búsqueda en cadenas con find() o in. Necesitas verificar que @ exista y que haya un punto después de @. Es una validación muy básica, en producción se usan expresiones regulares.


### Ejercicio 2: Contador de Palabras

Crea una función que cuente cuántas palabras hay en un texto.

```python
def contar_palabras(texto):
    # Tu código aquí
    pass

# Pruebas
print(contar_palabras('Python es genial'))           # 3
print(contar_palabras('Hola mundo'))                 # 2
print(contar_palabras('Una  frase   con  espacios')) # 4
```

Note: Usa split() que maneja automáticamente múltiples espacios. Luego cuenta los elementos de la lista resultante con len(). Cuidado con cadenas vacías o solo espacios.


### Ejercicio 3: Invertir Palabras

Escribe una función que invierta el orden de las palabras en una frase.

```python
def invertir_palabras(frase):
    # Tu código aquí
    pass

# Pruebas
print(invertir_palabras('Python es genial'))
# 'genial es Python'
print(invertir_palabras('Hola mundo'))
# 'mundo Hola'
```

Note: Divide la frase con split(), invierte la lista con [::-1] o reversed(), y únel con join(). Practica la combinación de métodos de cadenas y listas.


### Ejercicio 4: Eliminar Duplicados

Crea una función que elimine letras duplicadas consecutivas de una cadena.

```python
def eliminar_duplicados(texto):
    # Tu código aquí
    pass

# Pruebas
print(eliminar_duplicados('Hoola'))      # 'Hola'
print(eliminar_duplicados('Programaaación'))  # 'Programación'
print(eliminar_duplicados('Pythonnn'))   # 'Python'
```

Note: Itera por la cadena comparando cada carácter con el anterior. Construye una nueva cadena solo con caracteres que no se repiten consecutivamente. Necesitas un bucle y una variable acumuladora.


### Ejercicio 5: Palíndromo

Escribe una función que verifique si una palabra es un palíndromo (se lee igual al derecho y al revés).

```python
def es_palindromo(palabra):
    # Tu código aquí
    pass

# Pruebas
print(es_palindromo('radar'))     # True
print(es_palindromo('python'))    # False
print(es_palindromo('anilina'))   # True
```

Note: Compara la palabra con su versión invertida usando [::-1]. Considera si quieres que sea case-insensitive (convierte a minúsculas primero). Considera si los espacios y acentos importan.


### Ejercicio 6: Censurar Palabras

Crea una función que reemplace palabras prohibidas con asteriscos.

```python
def censurar(texto, prohibidas):
    # Tu código aquí
    pass

# Pruebas
texto = 'Este es un texto con palabras malas'
prohibidas = ['malas', 'texto']
print(censurar(texto, prohibidas))
# 'Este es un ***** con palabras *****'
```

Note: Para cada palabra prohibida, usa replace() para cambiarla por asteriscos. Puedes hacer los asteriscos del mismo largo que la palabra original multiplicando '*' por len(palabra).

---

## Mejores Prácticas


### Usar f-strings para formato

```python
# Mal: concatenación
nombre = 'Ana'
edad = 25
mensaje = 'Me llamo ' + nombre + ' y tengo ' + str(edad) + ' años'

# Bien: f-string
mensaje = f'Me llamo {nombre} y tengo {edad} años'

# Mal: múltiples concatenaciones
resultado = str(a) + ' + ' + str(b) + ' = ' + str(a + b)

# Bien: f-string
resultado = f'{a} + {b} = {a + b}'
```

Note: F-strings son más legibles, menos propensos a errores, y más eficientes que concatenación. Convierte tipos automáticamente. No necesitas str() explícito para números. Usa f-strings siempre que sea posible.


### Evitar concatenación en bucles

```python
# Mal: concatenación repetida (ineficiente)
resultado = ''
for palabra in palabras:
    resultado = resultado + palabra + ' '

# Bien: join (eficiente)
resultado = ' '.join(palabras)

# Si necesitas bucle, usa lista
partes = []
for palabra in palabras:
    partes.append(palabra.upper())
resultado = ' '.join(partes)
```

Note: Concatenar cadenas en bucles es muy ineficiente porque crea una nueva cadena en cada iteración. Usa join() o acumula en una lista y une al final. La diferencia de rendimiento es significativa con muchas iteraciones.


### Comparaciones case-insensitive

```python
# Mal: muchas comparaciones
if texto == 'python' or texto == 'Python' or texto == 'PYTHON':
    ...

# Bien: convertir a minúsculas
if texto.lower() == 'python':
    ...

# Para múltiples palabras
if texto.lower() in ['python', 'java', 'javascript']:
    ...
```

Note: Para comparaciones que no distinguen mayúsculas, convierte ambas cadenas a minúsculas (o mayúsculas). Es más simple y mantenible que listar todas las combinaciones posibles.


### Validación de entrada

```python
# Siempre valida entrada del usuario
email = input('Email: ')

# Verificar no vacío
if not email or not email.strip():
    print('Email no puede estar vacío')

# Verificar formato básico
if '@' not in email or '.' not in email:
    print('Email inválido')

# Limpiar espacios extras
email = email.strip().lower()
```

Note: Nunca confíes ciegamente en entrada del usuario. Valida que no esté vacía, que tenga el formato esperado, y limpia espacios extras. strip() elimina espacios al inicio/final que el usuario pudo escribir accidentalmente.


### Documentar cadenas complejas

```python
# Sin documentación
regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Con documentación
# Patrón de email:
# - Comienza con letras, números o ._%+-
# - Seguido de @
# - Dominio con letras, números, punto o guión
# - Punto y extensión de al menos 2 letras
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

Note: Patrones complejos (regex, SQL, etc.) en cadenas deben documentarse. Explica qué hace el patrón, no solo ponlo ahí. Tu yo futuro te lo agradecerá.

---

## Resumen


### Conceptos clave

* Cadenas son secuencias inmutables de caracteres
* Indexación con [] (comienza en 0)
* Slicing [inicio:fin:paso] para subcadenas
* Operadores: +, *, in, ==, <, >
* Muchos métodos útiles: upper, lower, split, join, replace
* F-strings para formato moderno

Note: Las cadenas son fundamentales en Python. Dominar su manipulación es esencial. La inmutabilidad puede parecer limitante pero proporciona seguridad y eficiencia. Los métodos de cadenas cubren casi cualquier necesidad.


### Métodos más importantes

* **Búsqueda**: find, index, count, in
* **Transformación**: upper, lower, capitalize, title
* **Limpieza**: strip, lstrip, rstrip
* **División/Unión**: split, join
* **Reemplazo**: replace
* **Validación**: isalpha, isdigit, isalnum

Note: No necesitas memorizar todos los métodos, solo conocer los principales. La documentación oficial es tu amiga. Con práctica, recordarás los más comunes. Lo importante es saber qué es posible hacer.


### Próximos pasos

* Practicar con ejercicios de manipulación de cadenas
* Aprender expresiones regulares para patrones complejos
* Estudiar listas (siguiente tema)
* Explorar módulos string y textwrap
* Trabajar con archivos de texto

Note: Las cadenas son la base para mucho en programación: procesar archivos, manejar APIs, validar entrada, formatear salida. Practica mucho. El próximo tema, listas, se complementa perfectamente con cadenas.

---

## ¿Preguntas?

Note: Las cadenas son omnipresentes en programación. Asegúrate de que los estudiantes entienden indexación, slicing, e inmutabilidad. Estos conceptos se aplican también a listas y tuplas. Anima a practicar con ejercicios variados.
