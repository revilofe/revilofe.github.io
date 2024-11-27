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
2. Diseñar y gestionar tres ficheros JSON: uno común para la configuración y estado global del juego, y uno para cada jugador que contenga la información de la partida relativa al jugador: Configuración de tablero, estado, e información de ataque.
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

El archivo `MiPartida.json` contendrá la configuración general de la partida:

**`MiPartida.json`:**
```json
{
    "nombre_partida": "MiPartida",
    "dimensiones_tablero": 10,
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
- **`nombre_partida`**: Nombre de la partida. En este caso, "MiPartida". Si no coincide con el nombre indicado al inicio, se mostrará un mensaje de error y terminará el juego.
- **`dimensiones_tablero`**: Tamaño del tablero cuadrado. En este caso, 10x10.
- **`tiempo_refresco`**: Tiempo de espera antes de volver a consultar la información de estado de tablero. Este tiempo se utilizará para mostrar el tablero actualizado.
- **`tiempo_ataque`**: Tiempo de espera entre turnos. Si pasado este tiempo no se realiza un ataque, se considerará un ataque fallido.
- **`configuracion_barcos`**: Contenrá la configuración de los barcos. Cada barco, tendrá el siguiente formato `{"NombreBarco": {"tamaño": N, "numero": M}}`.    

    - `"tamaño"`: Tamaño del barco.
    - `"numero"`: Número de barcos de ese tipo.

- **`turnos_jugados`**: Número de turnos jugados. Iniciará en 0, y se irá incrementando en cada ataque ejecutado, es decir, puede incrementarse el turno_jugado sin cambiar el turno_actual, siempre y cuando el jugador ataque y acierte.
- **`turno_actual`**: Jugador que tiene el turno actualmente {j1, j2}
- Otros datos relevantes que consideréis necesarios.

Los archivos `MiPartida.j1.json` y `MiPartida.j2.json` contendrán la información específica de cada jugador, incluyendo su tablero, barcos y movimientos realizados:

**`MiPartida.j1.json`:**
```json
{
    "nombre": "j1",
    "tablero": [
        ["B", "~", "H", "~", "B"],
        ["B", "B", "B", "B", "T"],
        ["~", "~", "~", "~", "~"],
        ["H", "~", "T", "B", "~"],
        ["H", "O", "~", "~", "O"]
    ],
    "barcos": {
        "Portaaviones": {
            "coordenadas": [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
            "estado": {"[1, 1]": "I", "[1, 2]": "T", "[1, 3]": "I", "[1, 4]": "I", "[1, 5]": "I"}
        }
    },
    "movimientos": [
        {"coordenada": [3, 4], "resultado": "A"},
        {"coordenada": [1, 2], "resultado": "T"}
    ]
}
```
En donde:
- **`nombre`**: Nombre del jugador. En este caso, "j1".
- **`tablero`**: Tablero de juego del jugador. Cada casilla puede tomar los siguientes valores:    

    - `"~"` (agua), 
    - `"B"` (barco), 
    - `"T"` (barco atacado), 
    - `"O"` (agua atacada), 
    - `"H"` (barco hundido).
- **`barcos`**: Diccionario con los barcos del jugador y su estado. Cada barco se representa con un diccionario que contiene las **coordenadas** que ocupa cada parte del barco y el **estado** de estas. Por tanto:    

    - `coordenadas`: será la lista de pares `[fila, columna]`. 
    - `estado`: tomará los siguientes valores `"I"` - intacto, `"T"` - Tocado o `"H"` - Hundido. Este último valor se asignará cuando todas las coordenadas del barco estén en estado `"T"`.
- **`movimientos`**: Lista de movimientos realizados por el jugador. En donde cada movimiento estarán representados por los siguientes datos:
    - `coordenada`: Coordenada del ataque en formato `[fila, columna]`.
    - `resultado`: Resultado del ataque (`"A"` - Agua, `"T"` - Tocado, `"H"` - Hundido). Este último valor se asignará cuando todas las coordenadas del barco del jugador atacado estén en estado `"T"`. 
- Otros datos relevantes que consideréis necesarios.


---

#### **Interacción**

**Inicio del Turno:**
```
Turno del Jugador 1.
Tu tablero de ataques:
~ ~ ~ ~ ~
~ ~ X ~ ~
~ ~ ~ ~ ~
~ ~ ~ O ~
~ ~ ~ ~ ~

Introduce coordenadas para atacar (fila, columna): 3, 4
Resultado del ataque: Agua
```

**Actualización de JSON:**
- El tablero de `Jugador 2` se actualiza para reflejar el ataque.
- El archivo global `MiPartida.json` se actualiza:
    - `"turnos_jugados": 1`
    - `"turno_actual": "Jugador 2"`

---

¿Especificamos más ejemplos de implementación o flujo detallado? 😊


#############################




### **Ejercicio: Hundir la Flota Multijugador en Python**

Este ejercicio propone desarrollar un juego de "Hundir la Flota" en Python, enfocado en el uso de estructuras de datos avanzadas y archivos JSON para gestionar la configuración y el intercambio de información entre dos jugadores. A continuación, se describe el juego, las especificaciones, las estructuras de datos requeridas, los ficheros necesarios y los aspectos clave a implementar.

---

### **Descripción del Bucle Principal del Juego**

El juego se desarrolla en un **bucle principal** que organiza la lógica de turnos y permite que los jugadores alternen para atacar el tablero del oponente. A continuación, se describe el flujo en lenguaje natural:

1. **Inicio del Juego:**
    - El archivo de configuración general se lee para obtener las dimensiones del tablero, la configuración de los barcos y el jugador que comienza.
    - Cada jugador dispone de su propio archivo JSON con su tablero, barcos, y registro de movimientos.

2. **Turnos Alternos:**
    - **Comprobación de Turno:** El programa consulta el archivo global (`nombre_de_la_partida.json`) para verificar quién tiene el turno.
    - **Tablero de Ataques:** Se construye dinámicamente un tablero basado en el registro de movimientos del jugador activo.
    - **Ataque:** El jugador introduce una coordenada (fila, columna) para atacar.
        - Si la coordenada coincide con un barco del oponente, el ataque se registra como "tocado" o "hundido".
        - Si no, se registra como "agua".
    - **Registro del Movimiento:** El ataque se añade al registro de movimientos del jugador activo.
    - **Actualización del Tablero del Oponente:** El tablero del oponente se actualiza con el resultado del ataque.
    - **Cambio de Turno:** El archivo global se actualiza para pasar el turno al siguiente jugador.

3. **Fin del Juego:**
    - Después de cada turno, se verifica si todos los barcos de un jugador han sido hundidos.
    - Si un jugador pierde todos sus barcos, se declara al ganador y el juego termina.

---

### **Estructura de Datos**

#### **1. Tablero**
El tablero de cada jugador es una lista de listas (`N x N`) que representa las casillas:
- `"~"`: Agua.
- `"B"`: Barco.
- `"X"`: Barco atacado.
- `"O"`: Agua atacada.

**Ejemplo de Tablero Inicial (Jugador 1):**
```python
tablero = [
    ["~", "~", "~", "~", "~"],
    ["~", "B", "B", "B", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "B", "B", "~"],
    ["~", "~", "~", "~", "~"]
]
```

---

#### **2. Barcos**
Cada barco es un diccionario que contiene:
- `coordenadas`: Lista de tuplas con las posiciones ocupadas por el barco.
- `estado`: Diccionario que indica si cada coordenada está `"intacto"` o `"tocado"`.

**Ejemplo de un Barco:**
```python
barco = {
    "coordenadas": [(1, 1), (1, 2), (1, 3)],
    "estado": {
        "(1, 1)": "intacto",
        "(1, 2)": "intacto",
        "(1, 3)": "tocado"
    }
}
```

---

#### **3. Registro de Movimientos**
El registro de movimientos realizados por cada jugador se almacena en un **conjunto** de tuplas, donde cada tupla contiene:
- La coordenada del ataque.
- El resultado del ataque (`"agua"`, `"tocado"`, `"hundido"`).

**Ejemplo de Registro de Movimientos:**
```python
movimientos = {
    ((1, 2), "tocado"),
    ((3, 4), "agua"),
    ((2, 1), "hundido")
}
```

---

#### **4. Jugador**
Cada jugador tiene:
- `nombre`: Nombre del jugador.
- `tablero`: Su tablero de juego.
- `barcos`: Un diccionario que almacena los barcos y su estado.
- `movimientos`: Conjunto que almacena los ataques realizados.

**Ejemplo de un Jugador:**
```python
jugador = {
    "nombre": "Jugador 1",
    "tablero": [["~", "~", "~", "~", "~"], ["~", "B", "B", "B", "~"], ...],
    "barcos": {
        "Portaaviones": {
            "coordenadas": [(1, 1), (1, 2), (1, 3)],
            "estado": {
                "(1, 1)": "intacto",
                "(1, 2)": "intacto",
                "(1, 3)": "tocado"
            }
        }
    },
    "movimientos": {
        ((1, 2), "tocado"),
        ((3, 4), "agua")
    }
}
```

---

### **Ficheros de Configuración JSON**

#### **1. Archivo General**
Contiene información fija sobre la partida y el estado actual del juego.

**Ejemplo:**
```json
{
    "nombre_partida": "MiPartida",
    "dimensiones_tablero": 10,
    "tiempo_refresco": 2,
    "configuracion_barcos": {
        "Portaaviones": {"tamaño": 5, "numero": 1},
        "Destructor": {"tamaño": 2, "numero": 4}
    },
    "turnos_jugados": 0,
    "turno_actual": "Jugador 1"
}
```

---

#### **2. Archivos de Jugadores**
Cada jugador tiene su propio archivo JSON con:
- Su tablero.
- La configuración de sus barcos.
- El registro de movimientos realizados.

**Ejemplo (Jugador 1):**
```json
{
    "nombre": "Jugador 1",
    "tablero": [
        ["~", "~", "~", "~", "~"],
        ["~", "B", "B", "B", "~"],
        ["~", "~", "~", "~", "~"],
        ["~", "~", "B", "B", "~"],
        ["~", "~", "~", "~", "~"]
    ],
    "barcos": {
        "Portaaviones": {
            "coordenadas": [[1, 1], [1, 2], [1, 3]],
            "estado": {"[1, 1]": "intacto", "[1, 2]": "intacto", "[1, 3]": "tocado"}
        }
    },
    "movimientos": [
        [[1, 2], "tocado"],
        [[3, 4], "agua"]
    ]
}
```

---

### **Especificaciones de las Funciones**

1. **Crear Tablero:**
   ```python
   def crear_tablero(n: int) -> list:
       """
       Crea un tablero vacío de tamaño N x N.
       """
   ```

2. **Colocar Barco:**
   ```python
   def colocar_barco(jugador: dict, tipo_barco: str, coordenadas: list[tuple]) -> bool:
       """
       Coloca un barco en el tablero del jugador.
       """
   ```

3. **Realizar Ataque:**
   ```python
   def realizar_ataque(jugador_oponente: dict, coordenada: tuple) -> str:
       """
       Realiza un ataque en el tablero del oponente.
       """
   ```

4. **Registrar Movimiento:**
   ```python
   def registrar_movimiento(jugador: dict, coordenada: tuple, resultado: str) -> None:
       """
       Registra un ataque realizado por el jugador.
       """
   ```

5. **Actualizar Turno:**
   ```python
   def actualizar_turno(nombre_archivo: str, siguiente_jugador: str) -> None:
       """
       Cambia el turno al siguiente jugador en el archivo global.
       """
   ```

---

### **Volcado de Datos a Consola**

1. **Inicio del Turno:**
   ```
   Turno del Jugador 1.
   Tu tablero de ataques:
   ~ ~ ~ ~ ~
   ~ ~ X ~ ~
   ~ ~ ~ ~ ~
   ~ ~ ~ O ~
   ~ ~ ~ ~ ~
   ```

2. **Después del Ataque:**
   ```
   Ataque a la coordenada (3, 4): Agua
   ```

---

### **Intercambio de Información entre Ataques**

1. **Información Registrada por el Atacante:**
    - Coordenada del ataque.
    - Resultado del ataque (`"agua"`, `"tocado"`, `"hundido"`).

2. **Actualización en el Archivo del Oponente:**
    - Estado del tablero.
    - Estado de los barcos afectados.

3. **Cambio de Turno:**
    - Actualización en el archivo global (`turno_actual`).

---

### **Sincronización y Turnos**

1. **Lectura de Turno:** Cada jugador lee el archivo global para saber si es su turno.
2. **Espera Activa:** Si no es su turno, el jugador espera (según `tiempo_refresco`).
3. **Cambio de Turno:** Después de cada ataque, el archivo global se actualiza para pasar el turno al siguiente jugador.

--- 

Este esquema detalla todos los

aspectos necesarios para que los alumnos comprendan la lógica del juego y las herramientas a utilizar. ¿Te gustaría algún diagrama para complementar? 😊