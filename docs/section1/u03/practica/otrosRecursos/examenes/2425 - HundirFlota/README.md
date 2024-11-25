# Actividad: Hundir la Flota Multijugador

**ID actividad:** PROG-001

**Agrupamiento de la actividad**: Individual

---

### 1. Descripción

La actividad consiste en implementar un juego de "Hundir la Flota" en Python para dos jugadores, utilizando archivos JSON para compartir información entre turnos. Los jugadores deben alternar turnos, registrar movimientos, atacar al oponente, y cumplir las reglas del juego. Se trabaja con estructuras de datos complejas y gestión de archivos JSON.

**Objetivo:**
1. Desarrollar habilidades en programación estructurada, utilizando funciones y estructuras de datos avanzadas como listas, conjuntos y diccionarios.
2. Trabajar con archivos JSON para persistir y compartir datos entre jugadores.
3. Aplicar conceptos de lógica y control de flujo en un proyecto práctico.

**Trabajo a realizar:**

1. Crear un programa en Python que implemente el juego **Hundir la Flota**.
2. Diseñar y gestionar tres ficheros JSON: uno común para la configuración y estado global del juego, y uno para cada jugador.
3. Implementar funciones para colocar tablero inicial, realizar ataques, registrar movimientos, gestionar turnos, verificar el estado de los barcos y mostrar información por consola.
4. Garantizar que el flujo del juego se respete y que los datos se actualicen correctamente tras cada turno.
5. Implementar el sistema para que sincronice los turnos y asegure que cada jugador interactúe correctamente con los datos compartidos.

Ver el ejemplo con la descripción completa en el punto 5. 

### 2. Recursos

- **Temario trabajado en clase:** Programación con Python, manipulación de estructuras de datos y uso de bibliotecas estándar para manejo de archivos.
- **Recursos vistos en clase:** Ejemplos de JSON, manejo de bucles, estructuras condicionales y funciones.


### 3. Evaluación y Calificación
# TODO:

**Rúbrica:**
Ver moodle.

### 4. Condiciones de Entrega

> **La entrega tiene que cumplir las condiciones de entrega para poder ser calificada. En caso de no cumplirlas podría calificarse como no entregada.**

1. Cumple la fecha y hora de entrega.
2. **Entrega de código mediante repositorio GitHub:**
    - El contenido se entregará en un repositorio GitHub, y el documento principal será el **README.md** ubicado en el raíz del repositorio.
    - Asegúrate de que el profesor tenga permisos de acceso. Si no se puede acceder al repositorio, se considerará como no entregado.
    - El README.md debe incluir:
        - Instrucciones para compilar y ejecutar el código.
        - Descripción de la aplicación y cómo funciona.
        - Autoría y referencias utilizadas.


### 5. Ejemplo del Ejercicio

#### **Ficheros JSON**

1. **`nombre_de_la_partida.json`:**
```json
{
    "nombre_partida": "MiPartida",
    "dimensiones_tablero": 10,
    "tiempo_refresco": 2,
    "configuracion_barcos": {
        "Portaaviones": {"tamaño": 5, "numero": 1},
        "Submarino": {"tamaño": 3, "numero": 2},
        "Destructor": {"tamaño": 2, "numero": 4}
    },
    "turnos_jugados": 0,
    "turno_actual": "Jugador 1"
}
```

2. **`MiPartida.jugador1.json`:**
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
            "coordenadas": [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
            "estado": {"[1, 1]": "intacto", "[1, 2]": "tocado", "[1, 3]": "intacto", "[1, 4]": "tocado", "[1, 5]": "intacto"}
        }
    },
    "movimientos": [
        {"coordenada": [3, 4], "resultado": "agua"},
        {"coordenada": [1, 2], "resultado": "tocado"}
    ]
}
```

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