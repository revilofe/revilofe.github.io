<!-- Con # se ponen los títulos -->

## U3.5

## Funciones

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Indice

---

### Funciones en Python

* Las funciones son estructuras esenciales de código.
* Unidades lógicas del programa.
* Dividen y organizan el código para mayor legibilidad y reutilización.
* Agrupan instrucciones para resolver un problema concreto.
* Objetivos:
  * Dividir y organizar el código.
  * Encapsular código repetitivo.

Note: Las funciones predefinidas en Python facilitan el trabajo, pero puedes definir las tuyas propias.

---

### Cómo definir una función en Python

* Utiliza la palabra reservada `def`.
* Nombre de la función seguido de paréntesis y lista de parámetros (opcional).
* Cabecera termina con dos puntos.
* Cuerpo de la función con sangrado mayor.
* Opcional: instrucción `return` para devolver un resultado.
* docstring se utiliza para documentar la función.

Note: El primer string de una función se llama docstring y se usa para documentar la función.

---

### Cómo usar una función en Python

* Para invocarla, escribe su nombre como una instrucción.
* Pasa los argumentos según los parámetros definidos.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">def multiplica_por_5(numero):
    print(f'{numero} * 5 = {numero * 5}')  # 7 * 5 = 35

multiplica_por_5(7)
</code></div></div></pre>

Note: El flujo de ejecución se desplaza a la función cuando es llamada.

---

## Parámetros y argumentos


### Diferencia entre parámetro y argumento

* Parámetro: definido en la función.
* Argumento: valor pasado a la función al ser invocada.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">def multiplica_por_5(numero):  # 'numero' es un parámetro
    print(f'{numero} * 5 = {numero * 5}')

multiplica_por_5(7)  # '7' es un argumento
</code></div></div></pre>

Note: Es importante distinguir entre ambos conceptos.


### Parámetros

* Paso por valor: copia el valor de las variables.
* Paso por referencia: copia la dirección de memoria.

Note: En Python, se pasa por valor la referencia del objeto.

---

## Retorno de valores


### Sentencia return

* El retorno de valores es opcional, puede devolver o no un valor.
* Termina la ejecución de la función y continúa el programa.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">def cuadrado_de_par(numero):
    if not numero % 2 == 0:
        return
    else:
        print(numero ** 2)  # 64

cuadrado_de_par(8)
</code></div></div></pre>

Note: `return` puede usarse para finalizar una función y/o devolver un valor. Ten en cuenta que los ejemplos no muestras buenas prácticas de uso, sino que son para ilustrar el concepto.


### Devolver más de un valor

* En Python, se puede devolver más de un valor con `return`.
* En tal caso, por defecto, se devuelve una tupla de valores.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">def cuadrado_y_cubo(numero):
    return numero ** 2, numero ** 3

cuad, cubo = cuadrado_y_cubo(4)
cuad  # 16
cubo  # 64
</code></div></div></pre>

Note: `return` permite devolver múltiples valores en una función.


### Devolver resultados en una lista

* Se pueden devolver diferentes resultados en una lista.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">def tabla_del(numero):
    resultados = []
    for i in range(11):
        resultados.append(numero * i)
    return resultados

res = tabla_del(3)
res  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
</code></div></div></pre>

Note: `return` puede utilizarse para devolver listas de resultados.


### Python siempre devuelve un valor

* A diferencia de otros lenguajes, Python no tiene procedimientos.
* Si no hay `return`, se devuelve automáticamente `None`.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">def saludo(nombre):
    print(f'Hola {nombre}')

print(saludo('j2logo'))  # Hola j2logo \n None
</code></div></div></pre>

Note: Python siempre devuelve un valor, incluso si no hay `return`. Por defecto, `None`

---

## Variables y ámbito


### Ámbito y ciclo de vida de las variables

* Local: dentro de una función, no accesible fuera.
* Global: definidas fuera de funciones, visibles dentro.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">
def muestra_x():
    x = 10
    print(f'x vale {x}')  # x vale 10

x = 20
muestra_x()
print(x)  # 20
</code></div></div></pre>

Note: Las variables tienen ámbitos locales o globales y ciclos de vida definidos.


### Ámbito y ciclo de vida de las variables

* Ámbito local: dentro de una función.
* Variables desaparecen al finalizar la función.

Note: Las variables definidas dentro de una función tienen un ámbito local y desaparecen al finalizar la función.


### Variables globales

* Ámbito global: fuera de funciones.
* Pueden ser consultadas dentro de funciones.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">
y = 20
def muestra_x():
    global x
    x += 1
    print(f'x vale {x}')
    print(f'y vale {y}')
</code></div></div></pre>

Note: Para modificar una variable global dentro de una función, se usa la palabra clave `global`.

---

### Funciones Lambda en Python

* Funciones anónimas y pequeñas.
* No requieren definición con `def`.
* Sintaxis: `lambda argumentos: expresion`.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">doble = lambda x: x * 2
</code></div></div></pre>

Note: Las funciones lambda son útiles para casos simples y breves.

---

### Resumen

* Funciones en Python son unidades lógicas de código.
* Dividen y organizan el código, facilitando la reutilización.
* Se definen con `def`, seguido del nombre y parámetros (opcional).
* Se invocan escribiendo el nombre y pasando argumentos.
* `return` opcional para devolver resultados.
* Ámbito de las variables: local y global.
* Las funciones lamda son utiles para casos simples y breves.

Note: ¡Enhorabuena! Has aprendido los conceptos fundamentales sobre funciones en Python.

---

## ¡Gracias por su atención!

Note: ¿Alguna pregunta sobre funciones en Python?
