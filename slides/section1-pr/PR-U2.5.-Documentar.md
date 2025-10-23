# U2.5 - Documentación del Código

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Por qué documentar el código?

* El código se lee más veces de las que se escribe
* Ayuda a otros (y a tu yo futuro) a entender el código
* Facilita mantenimiento y colaboración
* Demuestra profesionalismo
* Hace el código auto-explicativo

Note: Guido van Rossum dijo "El código se lee más veces de las que se escribe". Documentar bien no es opcional, es parte esencial de escribir buen código. Tu yo dentro de 6 meses te lo agradecerá.


### Tipos de documentación

* **Comentarios**: Explicaciones breves en el código
* **Docstrings**: Documentación de funciones, clases, módulos
* **README**: Descripción general del proyecto
* **Documentación técnica**: Guías detalladas
* **Type hints**: Anotaciones de tipos

Note: La documentación viene en diferentes formas y niveles. Los comentarios son para desarrolladores que lean tu código. README para usuarios que usen tu proyecto. Docstrings son documentación formal para módulos, clases y funciones.


### Equilibrio: ni mucho ni poco

* **Poco**: Código difícil de entender
* **Mucho**: Ruido que distrae
* **Justo**: Clarifica intención sin redundancia
* El código debe ser auto-documentado cuando sea posible

Note: No documentes lo obvio. Si tu código es claro, no necesita comentarios explicando cada línea. Documenta el "por qué", no el "qué". El código ya dice qué hace, los comentarios deben explicar por qué lo hace así.

---

## Comentarios


### Comentarios de una línea

```python
# Calcular precio con descuento del 20%
precio_final = precio * 0.8

edad = 25  # Edad del usuario en años

# TODO: Añadir validación de entrada
# FIXME: Este cálculo falla con valores negativos
# HACK: Solución temporal hasta refactorizar
```

Note: Los comentarios de una línea empiezan con #. Úsalos para aclaraciones breves. Las etiquetas como TODO, FIXME, HACK ayudan a encontrar puntos que necesitan atención. Muchos IDEs las resaltan.


### Comentarios de varias líneas

```python
"""
Este es un comentario largo que explica
una sección compleja del código.

Puede abarcar múltiples líneas y proporcionar
contexto detallado sobre decisiones de diseño.
"""

# También puedes usar múltiples líneas con #
# pero es menos común y más difícil de mantener
# que las triple comillas.
```

Note: Para comentarios largos, usa triple comillas ("""). Aunque técnicamente son cadenas, Python las ignora si no están asignadas. Son más fáciles de leer y editar que múltiples líneas con #.


### Qué comentar: el "Por qué"

```python
# Mal: comenta lo obvio
x = x + 1  # Incrementar x en 1

# Bien: explica el por qué
x = x + 1  # Compensar por índice basado en 1 en la API

# Mal: redundante
usuarios = []  # Crear lista vacía

# Bien: explica la decisión
usuarios = []  # Caché de usuarios para evitar consultas repetidas
```

Note: No comentes lo que el código ya dice claramente. Comenta decisiones de diseño, workarounds, limitaciones conocidas, algoritmos no obvios, razones de negocio. Comenta el "por qué", no el "qué".


### Qué NO comentar

```python
# Evitar:
i = 0  # Asignar 0 a i
while i < 10:  # Bucle de 0 a 9
    print(i)  # Imprimir i
    i = i + 1  # Incrementar i

# Mejor (sin comentarios innecesarios):
for i in range(10):
    print(i)
```

Note: No comentes código obvio. Si necesitas muchos comentarios para explicar código simple, probablemente el código necesita ser más claro, no más comentarios. Usa nombres descriptivos en lugar de comentarios.


### Comentar código complejo

```python
# Algoritmo de ordenamiento quicksort
# Complejidad: O(n log n) promedio, O(n²) peor caso
# Elegido por mejor rendimiento promedio vs mergesort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    # Usar elemento medio como pivote para mejor distribución
    pivot = arr[len(arr) // 2]
    
    # Particionar en menores, iguales y mayores
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)
```

Note: Para algoritmos complejos, comenta la estrategia general, complejidad computacional, y razones de elección. Los pasos individuales pueden comentarse si no son obvios. Esto ayuda a quien mantiene el código en el futuro.

---

## Docstrings


### ¿Qué son los docstrings?

* Documentación formal de módulos, clases y funciones
* Se escriben con triple comillas """
* Accesibles vía atributo `__doc__`
* Mostrados por help()
* Procesables por herramientas de documentación

```python
def saludar(nombre):
    """Imprime un saludo personalizado."""
    print(f'Hola, {nombre}!')

print(saludar.__doc__)  # Imprime el docstring
help(saludar)           # Muestra documentación completa
```

Note: Los docstrings son la forma estándar de documentar Python. A diferencia de comentarios, son parte del objeto y accesibles programáticamente. Herramientas como Sphinx pueden generar documentación HTML desde docstrings.


### Docstrings de funciones - Formato básico

```python
def calcular_area_rectangulo(ancho, alto):
    """
    Calcula el área de un rectángulo.
    
    Args:
        ancho: Ancho del rectángulo en metros
        alto: Alto del rectángulo en metros
        
    Returns:
        Área del rectángulo en metros cuadrados
    """
    return ancho * alto
```

Note: El docstring de función debe estar inmediatamente después de la definición. Primera línea: resumen breve. Línea vacía. Luego detalles: parámetros, retorno, excepciones. Este formato es Google Style, uno de los más populares.


### Docstrings - Numpy Style

```python
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Parameters
    ----------
    numeros : list of float
        Lista de números para promediar
        
    Returns
    -------
    float
        Promedio de los números
        
    Raises
    ------
    ValueError
        Si la lista está vacía
    """
    if not numeros:
        raise ValueError('Lista vacía')
    return sum(numeros) / len(numeros)
```

Note: Numpy Style usa guiones para separar secciones. Es popular en comunidad científica. Más visual que Google Style. Ambos son válidos, elige uno y sé consistente en todo tu proyecto.


### Docstrings de clases

```python
class Rectangulo:
    """
    Representa un rectángulo con ancho y alto.
    
    Esta clase proporciona métodos para calcular
    área y perímetro de rectángulos.
    
    Attributes:
        ancho (float): Ancho del rectángulo
        alto (float): Alto del rectángulo
    """
    
    def __init__(self, ancho, alto):
        """
        Inicializa un nuevo rectángulo.
        
        Args:
            ancho: Ancho del rectángulo
            alto: Alto del rectángulo
        """
        self.ancho = ancho
        self.alto = alto
```

Note: El docstring de clase describe qué representa la clase y sus atributos principales. Los métodos tienen sus propios docstrings. El docstring del __init__ describe los parámetros del constructor.


### Docstrings de módulos

```python
"""
Módulo de utilidades geométricas.

Este módulo proporciona clases y funciones para
cálculos geométricos básicos con figuras 2D.

Clases:
    Rectangulo: Representa un rectángulo
    Circulo: Representa un círculo
    
Funciones:
    calcular_area_triangulo: Calcula área de triángulo
    
Ejemplo:
    >>> from geometria import Rectangulo
    >>> rect = Rectangulo(5, 3)
    >>> rect.calcular_area()
    15
"""

class Rectangulo:
    # ...
```

Note: El docstring de módulo va al principio del archivo, antes de imports. Describe el propósito del módulo, lista clases y funciones principales, y opcionalmente incluye ejemplos de uso.


### Ejemplos en docstrings

```python
def fibonacci(n):
    """
    Genera los primeros n números de Fibonacci.
    
    Args:
        n: Cantidad de números a generar
        
    Returns:
        Lista con los primeros n números de Fibonacci
        
    Examples:
        >>> fibonacci(5)
        [0, 1, 1, 2, 3]
        
        >>> fibonacci(1)
        [0]
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib
```

Note: Ejemplos en docstrings son muy valiosos. Muestran uso real de la función. Además, pueden ejecutarse como tests con doctest. Los ejemplos usan formato >>> como en el intérprete interactivo.

---

## Type Hints


### Introducción a Type Hints

* Anotaciones de tipos para parámetros y retornos
* Documentan qué tipos se esperan
* Verificables con mypy
* No afectan ejecución (solo documentación)

```python
def saludar(nombre: str) -> str:
    return f'Hola, {nombre}!'

def sumar(a: int, b: int) -> int:
    return a + b
```

Note: Type hints son una forma de documentación ejecutable. No cambian el comportamiento del código, pero herramientas como mypy pueden verificar que uses los tipos correctamente. Previene muchos bugs.


### Type Hints básicos

```python
# Tipos simples
edad: int = 25
nombre: str = 'Ana'
activo: bool = True
precio: float = 19.99

# Funciones
def calcular(x: int, y: int) -> int:
    return x + y

# None
def procesar(datos: str) -> None:
    print(datos)
```

Note: Los type hints más básicos son int, str, bool, float, None. Usa -> para indicar el tipo de retorno. None indica que la función no retorna nada (solo hace algo).


### Type Hints para colecciones

```python
from typing import List, Dict, Tuple, Set, Optional

def procesar_nombres(nombres: List[str]) -> int:
    return len(nombres)

def obtener_config() -> Dict[str, int]:
    return {'timeout': 30, 'reintentos': 3}

def obtener_coordenadas() -> Tuple[float, float]:
    return (40.4168, -3.7038)

def buscar_usuario(id: int) -> Optional[str]:
    # Puede retornar str o None
    return None if id < 0 else 'Usuario'
```

Note: Para colecciones, importa tipos de typing. List[str] es lista de strings. Dict[str, int] es diccionario con claves string y valores int. Optional[str] significa str o None.


### Type Hints avanzados

```python
from typing import Union, Callable, Any

# Union: puede ser uno de varios tipos
def formatear(valor: Union[int, float, str]) -> str:
    return str(valor)

# Callable: función como parámetro
def aplicar(func: Callable[[int], int], x: int) -> int:
    return func(x)

# Any: cualquier tipo (evitar si es posible)
def procesar(dato: Any) -> Any:
    return dato
```

Note: Union permite múltiples tipos posibles. Callable para funciones como parámetros. Any para "cualquier cosa" (evita Any cuando sea posible, es mejor ser específico).


### Combinación: Docstrings + Type Hints

```python
def calcular_descuento(
    precio: float,
    porcentaje: float,
    aplicar: bool = True
) -> float:
    """
    Calcula precio con descuento aplicado.
    
    Args:
        precio: Precio original del producto
        porcentaje: Porcentaje de descuento (0-100)
        aplicar: Si aplicar descuento o solo calcularlo
        
    Returns:
        Precio final después del descuento
        
    Raises:
        ValueError: Si porcentaje fuera de rango 0-100
    """
    if not 0 <= porcentaje <= 100:
        raise ValueError('Porcentaje debe estar entre 0 y 100')
    
    descuento = precio * (porcentaje / 100)
    return precio - descuento if aplicar else descuento
```

Note: Type hints y docstrings se complementan. Type hints documentan tipos de forma verificable. Docstrings documentan comportamiento, restricciones, y casos especiales. Juntos proporcionan documentación completa.

---

## Mejores Prácticas


### PEP 8 y PEP 257

* **PEP 8**: Guía de estilo para código Python
* **PEP 257**: Convenciones para docstrings
* Seguir estas guías hace tu código consistente con comunidad Python
* Herramientas como flake8 y pylint verifican PEP 8

```python
# PEP 8: nombres descriptivos, snake_case
def calcular_precio_final(precio_base, impuesto_porcentaje):
    """PEP 257: Docstring en línea después de definición."""
    return precio_base * (1 + impuesto_porcentaje / 100)
```

Note: PEP 8 es el estándar de estilo de Python. Cúbrelo en detalle más adelante, pero lo esencial: nombres descriptivos en snake_case, 4 espacios de indentación, líneas máximo 79 caracteres, docstrings para todo lo público.


### README del proyecto

```markdown
# Mi Proyecto

Descripción breve del proyecto.

## Instalación

```bash
pip install mi-proyecto
```

## Uso

```python
from mi_proyecto import funcion_principal
resultado = funcion_principal()
```

## Contribuir

1. Fork el proyecto
2. Crea una rama
3. Haz commits
4. Push y crea Pull Request

## Licencia

MIT License
```

Note: Todo proyecto debe tener README. Explica qué hace el proyecto, cómo instalarlo, cómo usarlo. GitHub automáticamente muestra el README.md en la página del proyecto. Es lo primero que ven los usuarios.


### Documentación es mantenimiento

* Actualizar documentación cuando cambies código
* Documentación obsoleta es peor que no documentación
* Incluir documentación en code reviews
* Tratar documentación como código

Note: La documentación obsoleta confunde y causa bugs. Cuando cambies código, actualiza la documentación. En code reviews, verifica que la documentación esté actualizada. Documentación es parte del código, no un afterthought.


### Herramientas de documentación

* **Sphinx**: Genera documentación HTML desde docstrings
* **MkDocs**: Documentación con Markdown
* **Read the Docs**: Hosting gratuito para documentación
* **Pdoc**: Documentación simple auto-generada

Note: Estas herramientas automatizan la generación de documentación web desde tus docstrings y archivos Markdown. Sphinx es el estándar en Python. Read the Docs es donde se aloja documentación de la mayoría de proyectos open source.


### Documentación para diferentes audiencias

* **Código**: Comentarios y docstrings para desarrolladores
* **API**: Referencia técnica de funciones y clases
* **Tutoriales**: Guías paso a paso para usuarios
* **README**: Vista general para nuevos usuarios

Note: Diferent audiencias necesitan diferente documentación. Desarrolladores leen código y docstrings. Usuarios finales leen tutoriales y README. No mezcles: mantén separada documentación técnica de guías de usuario.

---

## Ejemplos Completos


### Función bien documentada

```python
from typing import List

def encontrar_primos(limite: int) -> List[int]:
    """
    Encuentra todos los números primos hasta un límite.
    
    Utiliza el algoritmo de la Criba de Eratóstenes para
    eficiencia. Complejidad O(n log log n).
    
    Args:
        limite: Número máximo a considerar (inclusive)
        
    Returns:
        Lista ordenada de números primos hasta limite
        
    Raises:
        ValueError: Si limite es menor que 2
        
    Examples:
        >>> encontrar_primos(10)
        [2, 3, 5, 7]
        
        >>> encontrar_primos(2)
        [2]
    """
    if limite < 2:
        raise ValueError('Límite debe ser al menos 2')
    
    # Criba de Eratóstenes
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    
    # Marcar múltiplos de cada primo como no primos
    for i in range(2, int(limite**0.5) + 1):
        if es_primo[i]:
            # Optimización: empezar desde i²
            for j in range(i*i, limite + 1, i):
                es_primo[j] = False
    
    # Recolectar todos los números que quedaron como primos
    return [num for num in range(2, limite + 1) if es_primo[num]]
```

Note: Este ejemplo muestra documentación completa: type hints, docstring con todos los elementos, comentarios explicando algoritmo, ejemplos de uso. Es el estándar de calidad profesional.


### Clase bien documentada

```python
from typing import List, Optional

class CuentaBancaria:
    """
    Representa una cuenta bancaria con operaciones básicas.
    
    Esta clase mantiene el saldo de la cuenta y proporciona
    métodos para depósitos y retiros con validación.
    
    Attributes:
        titular (str): Nombre del titular de la cuenta
        saldo (float): Saldo actual de la cuenta
        numero (str): Número de cuenta único
        
    Example:
        >>> cuenta = CuentaBancaria('Ana', 1000.0, '12345')
        >>> cuenta.depositar(500)
        >>> cuenta.retirar(200)
        >>> cuenta.saldo
        1300.0
    """
    
    def __init__(self, titular: str, saldo_inicial: float, numero: str):
        """
        Inicializa una nueva cuenta bancaria.
        
        Args:
            titular: Nombre del titular
            saldo_inicial: Saldo inicial (debe ser >= 0)
            numero: Número de cuenta único
            
        Raises:
            ValueError: Si saldo_inicial es negativo
        """
        if saldo_inicial < 0:
            raise ValueError('Saldo inicial no puede ser negativo')
        
        self.titular = titular
        self.saldo = saldo_inicial
        self.numero = numero
    
    def depositar(self, cantidad: float) -> None:
        """
        Deposita dinero en la cuenta.
        
        Args:
            cantidad: Cantidad a depositar
            
        Raises:
            ValueError: Si cantidad es negativa o cero
        """
        if cantidad <= 0:
            raise ValueError('Cantidad debe ser positiva')
        self.saldo += cantidad
    
    def retirar(self, cantidad: float) -> bool:
        """
        Retira dinero de la cuenta.
        
        Args:
            cantidad: Cantidad a retirar
            
        Returns:
            True si el retiro fue exitoso, False si fondos insuficientes
            
        Raises:
            ValueError: Si cantidad es negativa o cero
        """
        if cantidad <= 0:
            raise ValueError('Cantidad debe ser positiva')
        
        if cantidad > self.saldo:
            return False
        
        self.saldo -= cantidad
        return True
    
    def __str__(self) -> str:
        """Retorna representación en string de la cuenta."""
        return f'Cuenta {self.numero} - {self.titular}: ${self.saldo:.2f}'
```

Note: Una clase profesional documenta la clase misma, todos sus métodos públicos, y proporciona ejemplos. Los atributos se documentan en el docstring de la clase. Cada método público tiene su documentación completa.

---

## Resumen


### Principios clave

* Documenta el "por qué", no el "qué"
* Usa docstrings para todo lo público
* Combina docstrings con type hints
* Mantén documentación actualizada
* Escribe para tu audiencia

Note: La documentación es inversión, no gasto. Tiempo documentando hoy ahorra mucho tiempo mañana. Código sin documentación es código legado desde el día uno.


### Herramientas recordadas

* Comentarios (#) para notas breves
* Docstrings (""") para documentación formal
* Type hints para tipos de datos
* README para descripción del proyecto
* Tools como Sphinx para documentación web

Note: Cada herramienta tiene su propósito. Domínalas todas y úsalas apropiadamente. La combinación de todas hace tu código profesional y mantenible.


### Próximos pasos

* Practicar escribir buenos docstrings
* Aprender a usar Sphinx
* Leer PEP 257 completo
* Contribuir a proyectos open source
* Escribir tu primer README completo

Note: La mejor forma de aprender es haciendo. Empieza documentando tus propios proyectos. Lee código de proyectos establecidos para ver cómo documentan los expertos. La práctica hace al maestro.

---

## ¿Preguntas?

Note: Documentar puede parecer tedioso pero es esencial. Anima a los estudiantes a documentar desde el principio, no después. Que entiendan que la documentación es para ellos mismos tanto como para otros.
