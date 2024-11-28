# Actividad: Hundir la Flota Multijugador

**ID actividad:** PROG-2425-U3-001

**Agrupamiento de la actividad**: Individual/Parejas

---

### 1. Descripción

La actividad consiste en implementar un juego de "Hundir la Flota" en Python para dos jugadores, utilizando archivos JSON para compartir información entre turnos, y la configuración inicial del juego. Los jugadores deben alternar turnos, registrar movimientos, atacar al oponente, y cumplir las reglas del juego. Se trabaja con estructuras de datos complejas y gestión de archivos JSON.

**Objetivo:**
1. Desarrollar habilidades en programación estructurada, utilizando funciones y estructuras de datos avanzadas como listas, conjuntos y diccionarios.
2. Trabajar con archivos JSON para persistir y compartir datos entre jugadores.
3. Aplicar conceptos de lógica y control de flujo en un proyecto práctico.

**Trabajo a realizar:**

1. Crear un programa en Python que implemente el juego **Hundir la Flota**.
2. Diseñar y gestionar tres ficheros JSON: uno común para los dos jugadores que contiene la configuración y estado global del juego, y dos más, uno por cada jugador que contenga la información de la partida relativa al jugador: Configuración de tablero, estado, e información de los movimientos de ataque.
3. Implementar funciones para colocar tablero inicial, realizar ataques, registrar movimientos, gestionar turnos, verificar el estado de los barcos y mostrar información por consola.
4. Garantizar que el flujo del juego se respete y que los datos se actualicen correctamente tras cada turno.
5. Implementar el sistema para que sincronice los turnos y asegure que cada jugador interactúe correctamente con los datos compartidos.

Ver el ejemplo con la descripción completa en el punto 5. 

### 2. Recursos

- **Temario trabajado en clase:** Programación con Python, manipulación de estructuras de datos y uso de bibliotecas estándar para manejo de archivos: Listas y tuplas, Diccionarios, Conjuntos y JSON.
- **Recursos vistos en clase:** Ejemplos de JSON, manejo de bucles, estructuras condicionales y funciones.


### 3. Evaluación y Calificación

**Rúbrica:**
# TODO:


### 4. Condiciones de Entrega

> **La entrega tiene que cumplir las condiciones de entrega para poder ser calificada. En caso de no cumplirlas podría calificarse como no entregada.**

1. Cumple la fecha y hora de entrega.
2. **Entrega de código mediante repositorio GitHub:**
    - El contenido se entregará en un repositorio GitHub, y el documento principal será el **README.md** ubicado en el raíz del repositorio.
    - El juego debe compilar y ejecutarse correctamente.
    - Asegúrate de que el profesor tenga permisos de acceso. Si no se puede acceder al repositorio, se considerará como no entregado.
    - El README.md debe incluir:
        - Instrucciones para compilar y ejecutar el código.
        - Descripción de la aplicación y cómo funciona.
        - Autoría y referencias utilizadas.


### 5. Descripción detallada del ejercicio

#### 5.1. Inicio y estructura de archivos

Al inicio de la partida, el juego preguntará por:
1. Las carpeta utilizadas para compartir la información entre los jugadores.
2. El nombre de la partida. 

Un ejemplo de los mensajes iniciales durante la interacción con el juego, podemos verlo a continuación:

```text
Iniciando el juego Hundir la Flota Multijugador.
____________________________________________________

Introduce la carpeta de la partida: /partidas/hundir_la_flota
Introduce el nombre de la partida: MiPartida
```

Esto indicará que el juego utilizará la carpeta `/partidas/hundir_la_flota/MiPartida` para almacenar los archivos JSON de la partida `MiPartida`.

La estructura de directorios solicitada será:

```
/partidas
└── /hundir_la_flota
    └── /MiPartida
        ├── MiPartida.json
        ├── MiPartida.j1.json
        └── MiPartida.j2.json
```

En donde:
- **`/partidas/hundir_la_flota`**: Carpeta específica para el juego "Hundir la Flota".
- **`/MiPartida`**: Carpeta para una partida específica llamada "MiPartida".
   - **`MiPartida.json`**: Archivo de configuración general de la partida.
   - **`MiPartida.j1.json`**: Archivo con los datos específicos del Jugador 1.
   - **`MiPartida.j2.json`**: Archivo con los datos específicos del Jugador 2.

#### 5.2. Archivo de configuración y estado de la partida

La partida se gestionará a través de un archivo JSON que contendrá la configuración general y el estado actual de la partida. Este archivo se utilizará para determinar el turno actual, el estado de los barcos, el tablero, y otros datos relevantes.

##### 5.2.1 Archivo de configuración 

El archivo `MiPartida.json` contendrá la configuración general de la partida:

**`MiPartida.json`:**
```json
{
    "nombre_partida": "MiPartida",
    "dimensiones_tablero": 5,
    "tiempo_refresco": 2,
    "tiempo_ataque": 30,
    "configuracion_barcos": {
        "Portaaviones": {"tamaño": 5, "numero": 1},
        "Submarino": {"tamaño": 2, "numero": 2},
        "Destructor": {"tamaño": 1, "numero": 3}
    },
    "turnos_jugados": 0,
    "turno_actual": "j1"
}
```

En donde:
- **`nombre_partida`**: Información estática. Nombre de la partida. En este caso, "MiPartida". Si no coincide con el nombre indicado al inicio, se mostrará un mensaje de error y terminará el juego.
- **`dimensiones_tablero`**: Información estática. Tamaño del tablero cuadrado. En este caso, 10x10.
- **`tiempo_refresco`**: Tiempo de espera antes de volver a consultar la información de estado de tablero. Este tiempo se utilizará para mostrar el tablero actualizado.
- **`tiempo_ataque`**: Información estática. Tiempo de espera entre turnos. Si pasado este tiempo no se realiza un ataque, se considerará un ataque fallido.
- **`configuracion_barcos`**: Información estática. Contendrá la configuración de los barcos. Cada barco, tendrá el siguiente formato `{"NombreBarco": {"tamaño": N, "numero": M}}`.    

    - `"tamaño"`: Tamaño del barco.
    - `"numero"`: Número de barcos de ese tipo.

- **`turnos_jugados`**: Información cambiante. Número de turnos jugados. Iniciará en 0, y se irá incrementando en cada ataque ejecutado, es decir, puede incrementarse el turno_jugado sin cambiar el turno_actual, siempre y cuando el jugador ataque y acierte.
- **`turno_actual`**: Información cambiante. Jugador que tiene el turno actualmente {"j1", "j2"}. Se alternará entre los jugadores en cada turno cada vez que se realice un ataque y sea fallido.

Este archivo tendrá la información global de la partida y se utilizará para determinar la información de los barcos, los datos de refresco y el turno actual. 

#####  5.2.2 Archivo de configuración

Los archivos `MiPartida.j1.json` y `MiPartida.j2.json` contendrán la información específica de cada jugador, incluyendo su tablero, barcos y movimientos realizados:

**`MiPartida.j1.json`:**
```json
{
    "nombre": "j1",
    "tablero": [
        ["B", "~", "H", "~", "B"],
        ["B", "T", "B", "B", "B"],
        ["~", "~", "~", "~", "~"],
        ["H", "~", "T", "B", "A"],
        ["H", "A", "~", "~", "A"]
    ],
    "barcos": {
        "Portaaviones1": {
            "coordenadas": [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4]],
            "estado": {"[1, 0]": "B", "[1, 1]": "T", "[1, 2]": "B", "[1, 3]": "B", "[1, 4]": "B"}
        },
        "submarino1": {
            "coordenadas": [[3, 0], [4, 0]],
            "estado": {"[3, 0]": "H", "[4, 0]": "H"}
        },
        "submarino2": {
            "coordenadas": [[3, 2], [3, 3]],
            "estado": {"[3, 2]": "T", "[3, 3]": "B"}
        },
        "Destructor1": {
            "coordenadas": [[0, 2]],
            "estado": {"[0, 2]": "H"}
        },
        "Destructor2": {
            "coordenadas": [[0, 0]],
            "estado": {"[0, 0]": "B"}
        },
        "Destructor3": {
            "coordenadas": [[0, 4]],
            "estado": {"[0, 4]": "B"}
        }
    },
    "movimientos": [
      {"coordenada": [0, 0], "resultado": "A"},
      {"coordenada": [4, 0], "resultado": "A"},
      {"coordenada": [4, 1], "resultado": "T"}
    ]
}
```
En donde:
- **`nombre`**: Nombre del jugador. En este caso, "j1".
- **`tablero`**: Tablero de juego del jugador. Cada casilla puede tomar los siguientes valores:    

    - `"~"` (agua), 
    - `"B"` (Barco), 
    - `"T"` (barco Tocado), 
    - `"A"` (Agua atacada), 
    - `"H"` (barco Hundido). Este último valor se asignará cuando todas las coordenadas del barco estén en estado `"T"`.
  
- **`barcos`**: Diccionario con los barcos del jugador y su estado. Cada barco se representa con un diccionario que contiene las **coordenadas** que ocupa cada parte del barco y el **estado** de estas. Por tanto:    

    - `coordenadas`: será la lista de pares `[fila, columna]`. 
    - `estado`: tomará los siguientes valores `"B"` - Barco intacto, `"T"` - Tocado o `"H"` - Hundido. Este último valor se asignará cuando todas las coordenadas del barco estén en estado `"T"`.
  
- **`movimientos`**: Lista de movimientos realizados por el jugador. En donde cada movimiento estarán representados por los siguientes datos:

    - `coordenada`: Coordenada del ataque en formato `[fila, columna]`.
    - `resultado`: Resultado del ataque (`"A"` - Agua, `"T"` - Tocado, `"H"` - Hundido). Este último valor se asignará cuando todas las coordenadas del barco del jugador atacado estén en estado `"T"`.   

Ten en cuenta, que en el fichero del j2, los movimientos tiene que ser coherentes con los datos del fichero del jugador 1. 

**`MiPartida.j2.json`:**
```json
{
    "nombre": "j2",
    "tablero": [...],
    "barcos": {...},
    "movimientos": [
      {"coordenada": [3, 0], "resultado": "H"},
      {"coordenada": [4, 0], "resultado": "H"},
      {"coordenada": [4, 1], "resultado": "A"},
      {"coordenada": [0, 2], "resultado": "H"},
      {"coordenada": [3, 4], "resultado": "A"},
      {"coordenada": [1, 1], "resultado": "T"},
      {"coordenada": [3, 2], "resultado": "T"},
      {"coordenada": [4, 4], "resultado": "A"}
    ]
}
```

#### 5.3. Flujo del Juego

El juego se desarrolla en un **bucle principal** que organiza la lógica de turnos y permite que los jugadores alternen para atacar el tablero del oponente. 

A continuación, se describe el flujo en lenguaje natural:   

1. Un jugador comienza el juego identificado la **carpeta de la partida** y el **nombre de la partida**. 
2. El archivo de configuración general **tiene que estar ya generado**. Se lee para obtener las dimensiones del tablero, la configuración de los barcos y el jugador que comienza. Chequea si el nombre de la partida coincide con el nombre del archivo, y chequea la demás información relevante.
3. El programa intentará crear el archivo del j1, si existe intentará crear el archivo del j2. Si existe, mostrará un mensaje de error y terminará el juego.
3. Cada jugador dispone de su propio archivo JSON con su tablero, barcos, y registro de movimientos. Al iniciar, se generará el tablero en base a la configuración de los barcos, preguntando por la posición de cada uno. Esta posición tiene que ser correcta y no puede superponerse con otro barco, ni estar fuera del tablero. 
4. Se selecciona el jugador que inicia el turno: el jugador activo. Siendo el otro, el jugador pasivo.
5. Se muestra los tableros actualizados: jugador activo "tablero de ataque", y jugador pasivo "tablero de estado". 
6. Se solicita al jugador activo que introduzca una coordenada para atacar. Tiene que cumplir el tiempo establecido, sino se dará el ataque por fallido.
7. En el JSON del jugador pasivo: Se chequea el ataque realizado y se registra el movimiento en el estado de los barcos y el tablero. 
8. En el JSON del jugador activo: Se registra el movimiento y su resultado. 
9. En consola, el "tablero de estado" del jugador pasivo se actualiza con el resultado del ataque. 
10. En consola, el "tablero de ataque" del jugador activo se muestra actualizado. 
11. Se actualiza el archivo global con el nuevo turno: Si es exitoso, se cambia el turno al siguiente jugador.
12. Volvemos al paso 4. 
13. Se declara al ganador y se finaliza el juego. 


##### 5.3.1. Interacción con el Juego

En una interacción típica con el juego, se mostrarán mensajes informativos y se solicitarán datos al usuario para realizar los ataques. A continuación, se muestra un ejemplo de interacción con el juego:

**Inicio del Turno: Jugador activo**
```
Turno del Jugador 1.
Tablero de ataque:
~ ~ H ~ ~
~ ~ ~ ~ T
~ ~ ~ ~ ~
H ~ T ~ ~
H A ~ ~ A
--- Tiempo de espera maximo: 30 segundos ---
Introduce coordenadas para atacar (fila, columna): 3, 4
```
Una vez se pulsa "Enter", se actualizarán los tableros y se mostrará el resultado del ataque:

```
Turno del Jugador 1.
Tablero de ataque: 
~ ~ H ~ ~
~ ~ ~ ~ T
~ ~ ~ ~ ~
H ~ T ~ A
H A ~ ~ A
Ataque 3, 4
Resultado del ataque: Agua
```

**Fin del Turno: Jugador activo - Actualización de JSON:**
- Se actualiza `MiPartida.j2.json`. Chequea el movimiento, obtiene el resultado. Deja reflejado el resultado en el tablero (Con X, para dejar constancia de que es el último movimiento) y en el estado de los barcos.
- Se actualiza `MiPartida.j1.json`, registra el movimiento con el resultado.
- El archivo global `MiPartida.json` se actualiza:
   - `"turnos_jugados": 6`
   - `"turno_actual": "j2"`

Si el jugador activo no realiza un ataque en el tiempo establecido, se considerará un ataque fallido y se pasará al siguiente jugador, en ese caso simplemente se incrementa el `turnos_jugados` y se cambia el `turno_actual` al siguiente jugador en el archivo global.

Tened en cuenta que en el tablero de ataque solo hay que mostrar los ataques realizados y sus resultados, pero no los barcos del jugador pasivo.

**Inicio de espera: Jugador pasivo**
```
Turno del Jugador 1.
Tablero de estado:
B ~ H ~ B
B B B B T
~ ~ ~ ~ ~
H ~ T B ~
H A ~ ~ A

Esperando ataque... 
```
El jugador pasivo queda esperando el ataque del jugador activo. Una vez el jugador activo ataca, muestra el resultado al jugador pasivo. 

```
Turno del Jugador 1.
Tablero de estado:
B ~ H ~ B
B B B B T
~ ~ ~ ~ ~
H ~ T B A
H A ~ ~ A

Ataque 3, 4
Resultado del ataque: Agua
```

**Fin de espera: Jugador pasivo - Actualización de JSON:**
- El tablero de `Jugador 2` se actualiza para reflejar el resultado del ataque. Busca X y lo sustituye por el resultado.



A continuación se describen de forma NO exhaustiva algunas de las funciones que se podrían implementar crear para desarrollar el juego **Hundir la Flota Multijugador**, detallando los argumentos que reciben, los valores que retornan, y su propósito. Como comentaba,la lista no pretende ser completa, ni obligatoria. Se intenta dar un ejemplo guía de algunas de las funciones en las que podría descomponerse el desarrollo.


#### 5.4. Funciones Relacionadas con la Configuración


##### 5.4.1. Crear Archivos de la Partida
```python
def crear_archivos_partida(carpeta: str, nombre_partida: str, dimensiones: int, configuracion_barcos: dict) -> None:
    """
    Crea los archivos necesarios para una nueva partida, incluyendo el archivo global y los archivos de los jugadores.
    
    Args:
        carpeta (str): Ruta a la carpeta donde se almacenarán los archivos de la partida.
        nombre_partida (str): Nombre de la partida.
        dimensiones (int): Dimensiones del tablero cuadrado (N x N).
        configuracion_barcos (dict): Configuración de los barcos en formato {"nombre": {"tamaño": int, "numero": int}}.
    
    Returns:
        None
    """
```


##### 5.4.2. Leer Archivo Global
```python
def leer_archivo_global(carpeta: str, nombre_partida: str) -> dict:
    """
    Lee el archivo global de configuración de la partida.
    
    Args:
        carpeta (str): Ruta a la carpeta donde se encuentra el archivo de la partida.
        nombre_partida (str): Nombre de la partida.
    
    Returns:
        dict: Contenido del archivo global en forma de diccionario.
    """
```


##### 5.4.3. Leer Archivo de un Jugador
```python
def leer_archivo_jugador(carpeta: str, nombre_partida: str, jugador: str) -> dict:
    """
    Lee el archivo JSON de un jugador específico.
    
    Args:
        carpeta (str): Ruta a la carpeta donde se encuentra el archivo de la partida.
        nombre_partida (str): Nombre de la partida.
        jugador (str): Identificador del jugador ("j1" o "j2").
    
    Returns:
        dict: Contenido del archivo del jugador en forma de diccionario.
    """
```


##### 5.4.4. Guardar Archivo Global
```python
def guardar_archivo_global(carpeta: str, nombre_partida: str, datos: dict) -> None:
    """
    Guarda los cambios en el archivo global de configuración de la partida.
    
    Args:
        carpeta (str): Ruta a la carpeta donde se encuentra el archivo de la partida.
        nombre_partida (str): Nombre de la partida.
        datos (dict): Contenido actualizado del archivo global.
    
    Returns:
        None
    """
```

##### 5.4.5. Guardar Archivo de un Jugador**
```python
def guardar_archivo_jugador(carpeta: str, nombre_partida: str, jugador: str, datos: dict) -> None:
    """
    Guarda los cambios en el archivo JSON de un jugador.
    
    Args:
        carpeta (str): Ruta a la carpeta donde se encuentra el archivo de la partida.
        nombre_partida (str): Nombre de la partida.
        jugador (str): Identificador del jugador ("j1" o "j2").
        datos (dict): Contenido actualizado del archivo del jugador.
    
    Returns:
        None
    """
```


#### 5.5. Funciones Relacionadas con el Tablero y los Barcos

##### 5.5.1. Crear Tablero
```python
def crear_tablero(dimensiones: int) -> list:
    """
    Crea un tablero vacío de dimensiones N x N.
    
    Args:
        dimensiones (int): Tamaño del tablero (N x N).
    
    Returns:
        list: Tablero vacío representado como una lista de listas.
    """
```

### 5.5.2. Colocar Barco
```python
def colocar_barco(tablero: list, barco: dict, coordenadas: list[tuple]) -> bool:
    """
    Coloca un barco en el tablero si las coordenadas son válidas.
    
    Args:
        tablero (list): Tablero del jugador.
        barco (dict): Diccionario que representa el barco.
        coordenadas (list[tuple]): Lista de coordenadas donde colocar el barco.
    
    Returns:
        bool: True si el barco se colocó correctamente, False si hubo un error.
    """
```

##### 5.5.3. Actualizar Tablero
```python
def actualizar_tablero(tablero: list, coordenada: tuple, resultado: str) -> None:
    """
    Actualiza el tablero con el resultado de un ataque.
    
    Args:
        tablero (list): Tablero del jugador.
        coordenada (tuple): Coordenada del ataque (fila, columna).
        resultado (str): Resultado del ataque ("A", "T", "H").
    
    Returns:
        None
    """
```


#### 5.6. Funciones Relacionadas con los Movimientos

##### 5.6.1. Registrar Movimiento
```python
def registrar_movimiento(movimientos: set, coordenada: tuple, resultado: str) -> None:
    """
    Registra un movimiento en el conjunto de movimientos del jugador.
    
    Args:
        movimientos (set): Conjunto de movimientos del jugador.
        coordenada (tuple): Coordenada del ataque (fila, columna).
        resultado (str): Resultado del ataque ("A", "T", "H").
    
    Returns:
        None
    """
```

##### 5.6.2. Verificar Movimiento Válido
```python
def verificar_movimiento(movimientos: set, coordenada: tuple) -> bool:
    """
    Verifica si un movimiento ya ha sido realizado en las coordenadas dadas.
    
    Args:
        movimientos (set): Conjunto de movimientos del jugador.
        coordenada (tuple): Coordenada a verificar (fila, columna).
    
    Returns:
        bool: True si el movimiento es válido, False si ya ha sido realizado.
    """
```

#### 5.7. Funciones Relacionadas con el Flujo del Juego

##### 5.7.1. Realizar Ataque
```python
def realizar_ataque(jugador_activo: dict, jugador_pasivo: dict, coordenada: tuple) -> str:
    """
    Realiza un ataque del jugador activo al jugador pasivo, registrando el resultado.
    
    Args:
        jugador_activo (dict): Diccionario con la información del jugador activo.
        jugador_pasivo (dict): Diccionario con la información del jugador pasivo.
        coordenada (tuple): Coordenada del ataque (fila, columna).
    
    Returns:
        str: Resultado del ataque ("A", "T", "H").
    """
```

##### 5.7.2. Cambiar Turno
```python
def cambiar_turno(archivo_global: str) -> str:
    """
    Cambia el turno al siguiente jugador en el archivo global.
    
    Args:
        archivo_global (str): Ruta al archivo global de la partida.
    
    Returns:
        str: Nuevo turno actual ("j1" o "j2").
    """
```

##### 5.7.3. Verificar Fin del Juego
```python
def verificar_fin_juego(jugador: dict) -> bool:
    """
    Verifica si todos los barcos de un jugador han sido hundidos.
    
    Args:
        jugador (dict): Diccionario con la información del jugador.
    
    Returns:
        bool: True si todos los barcos han sido hundidos, False en caso contrario.
    """
```

#### 5.8. Funciones Relacionadas con la Consola

##### 5.8.1. Mostrar Tablero
```python
def mostrar_tablero(tablero: list, modo: str = "ataque") -> None:
    """
    Muestra el tablero en consola. Si el modo es "ataque", oculta los barcos intactos.
    
    Args:
        tablero (list): Tablero del jugador.
        modo (str): Modo de visualización ("ataque" o "estado").
    
    Returns:
        None
    """
```


### 6. Consejos

A continuación, se presentan consejos prácticos para implementar el juego de **Hundir la Flota Multijugador**. Estos están diseñados para guiarte paso a paso en la resolución del ejercicio de manera estructurada.

#### 6.1. Comprender el Problema

Antes de comenzar a programar, asegúrate de comprender completamente el problema y los requerimientos:
1. Lee cuidadosamente la descripción del ejercicio.
2. Comprende el flujo del juego: inicialización, colocación de barcos, ataques, cambios de turno, y finalización.
3. Identifica qué datos se necesitan en cada etapa y cómo interactúan los jugadores con el sistema.

#### 6.2. Planificación y Diseño

1. Divide el problema en partes más pequeñas. Implementa primero funciones sencillas como la creación de tableros, y después pasa a funciones más complejas, como los ataques.
2. Usa pseudocódigo o diagramas para planificar la lógica del juego. Esto puede ayudarte a visualizar el flujo de datos entre funciones y archivos.
3. Diseña las funciones pensando en la modularidad. Cada función debe realizar una tarea específica.

#### 6.3. Modularidad y Funciones

1. Escribe una función para cada operación. Por ejemplo, crea funciones separadas para:   

    - Leer y guardar archivos JSON.  
    - Crear el tablero.
    - Registrar un movimiento.
    - Realizar un ataque.
   
2. Prueba cada función de manera independiente antes de integrarla en el programa principal.   
3. Evita escribir todo el código en un solo archivo. Si es posible, organiza las funciones en módulos según su propósito.

#### 6.4. Uso de Archivos JSON

1. Familiarízate con el formato JSON. Asegúrate de comprender cómo se representan listas, diccionarios, y estructuras anidadas.    
2. Valida los datos al leer un archivo JSON. Por ejemplo, comprueba que las dimensiones del tablero sean correctas y que los barcos estén definidos adecuadamente.  
3. Guarda los datos regularmente. Asegúrate de que los archivos de los jugadores y el archivo global reflejen siempre el estado más reciente de la partida.   

#### 6.5. Trabajar con Tableros y Barcos

1. Representa el tablero como una lista de listas y actualízalo conforme ocurran ataques.
2. Asegúrate de que los barcos se coloquen en posiciones válidas:

    - Dentro de los límites del tablero.  
    - Sin superponer a otros barcos.  
   
3. Al realizar un ataque, actualiza tanto el tablero como el estado del barco atacado.

#### 6.6. Manejo de Movimientos

1. Usa un conjunto para registrar las coordenadas de los ataques realizados por cada jugador. Esto evita duplicados automáticamente.
2. Antes de realizar un ataque, verifica si la coordenada ya ha sido atacada.
3. Guarda el resultado del ataque (agua, tocado, hundido) junto con las coordenadas en los archivos correspondientes.

#### 6.7. Depuración y Validación

1. Asegúrate de que cada función se comporta como se espera antes de integrarla. Por ejemplo:   

    - Prueba si la función `crear_tablero` genera correctamente un tablero vacío.
    - Valida si los archivos JSON son leídos y escritos correctamente.
   
2. Utiliza mensajes de error claros para detectar problemas rápidamente. Por ejemplo:   

    - "Coordenada fuera de los límites del tablero."   
    - "El barco no cabe en la posición indicada."    

#### 6.8. Prueba Escenarios Simples

1. Antes de probar el juego completo, simula pequeñas partes del flujo. Por ejemplo:    

    - Coloca un barco y verifica su representación en el tablero.
    - Realiza un ataque y verifica si el resultado se registra correctamente.
2. Usa datos de prueba realistas, como un tablero parcialmente lleno y un archivo de configuración global válido.

#### 6.9. Interacción con el Usuario

1. Proporciona mensajes claros y detallados. Por ejemplo:    

    - "Es tu turno. Introduce una coordenada para atacar."
    - "Ataque exitoso: Has tocado un barco en (2, 3)."

2. Asegúrate de que el tablero mostrado en consola sea fácil de interpretar:   

    - Tablero del jugador activo: Muestra solo los ataques realizados y sus resultados.
    - Tablero del jugador pasivo: Muestra los barcos, incluyendo cuáles han sido tocados o hundidos.

#### 6.10. Control de Turnos

1. Lee el archivo global para determinar quién tiene el turno.
2. Asegúrate de que el turno se actualiza correctamente después de cada ataque.
3. Implementa un temporizador (si es requerido) para forzar el cambio de turno si el jugador activo no realiza un ataque dentro del tiempo límite.

#### 6.11. Documentación y Organización

1. Comenta tu código. Explica el propósito de cada función y cualquier lógica compleja.
2. Escribe un README que explique:    

    - Cómo ejecutar el programa.
    - Cómo están organizados los archivos JSON.
    - Las reglas del juego y las convenciones utilizadas en el código.   
   
3. Organiza el código en secciones lógicas. Por ejemplo:    

    - Funciones relacionadas con el tablero.
    - Funciones para manejar los archivos JSON.
    - Funciones para la interacción del usuario.

#### 6.12. Errores Comunes y Cómo Evitarlos

1. **Barcos superpuestos o fuera de los límites:**    

    - Valida las posiciones de los barcos antes de colocarlos en el tablero.   
   
2. **Ataques duplicados:**

    - Usa el conjunto de movimientos para evitar ataques repetidos en la misma coordenada.
   
3. **Turnos desincronizados:**

    - Asegúrate de que el archivo global refleje correctamente el turno actual.
   
4. **JSON malformado:**

    - Usa estructuras claras y validadas antes de guardar los datos.
   

#### 6.13. Prueba Completa

1. Antes de finalizar, prueba una partida completa:    

    - Configura un tablero inicial con barcos colocados.   
    - Realiza ataques alternados entre los jugadores.   
    - Verifica que los archivos JSON se actualicen correctamente después de cada turno.   
   
2. Asegúrate de que las condiciones de victoria se detecten correctamente y que el juego termine de manera adecuada.
