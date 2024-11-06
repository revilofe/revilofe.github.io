
# **Manual de uso - Calculadora Interactiva**

## **1. Inicio de la calculadora**
Cuando se inicia el programa, se muestra el nombre de la aplicación y se solicita una entrada o comando de operación:

```
### CALCULADORA ###
    -----------

Operación (RES => 0.00) >> 
```

### **2. Ver la lista de operaciones disponibles**
Escribe `lista` para ver todas las operaciones que puedes realizar con esta calculadora. El sistema mostrará la siguiente información:

```
Operación (RES => 0.00) >> lista

Operaciones disponibles:
    ce => Reiniciar resultado a 0
    decimales <n> => Establecer decimales en resultado
    cadena vacía + <ENTER> => Pregunta si desea salir
    calculo => Iniciar cálculo secuencial
        + => Suma
        - => Resta
        x o * => Multiplicación
        / o : => División
        ** exp => Potencia
        cancelar => volver sin actualizar resultado de la calculadora
        cadena vacía + <ENTER> => volver actualizando resultado de la calculadora

Presione ENTER para continuar...
```

### **3. Cambiar el número de decimales**
Para configurar el número de decimales que se mostrarán en el resultado, ingresa `decimales` seguido del número de decimales deseado. Ejemplo:

```
Operación (RES => 0.00) >> decimales 3
Decimales configurados a 3.

Presione ENTER para continuar...
```

después de pulsar ENTER, el resultado de formateará con tres decimales:

```
Operación (RES => 0.000) >>
```

Esta configuración de decimales también afectará a los resultados intermedios que se produzcan en los cálculos secuenciales *(dentro de la opción `calculo`)*

### **4. Reiniciar el resultado a cero**
Para restablecer el valor almacenado a 0, usa el comando `ce`:

```
Operación (RES => 18.24) >> ce
Resultado reiniciado a 0.

Presione ENTER para continuar...
```

Después de pulsar ENTER, el resultado almacenado de la calculadora será 0:

```
Operación (RES => 0.00) >>
```

### **5. Secuencia de cálculos con el comando `calculo`**
Para iniciar una secuencia de cálculos, escribe `calculo`:

```
Operación (RES => 1.00) >> calculo

## Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo ##

    (Cálculo = 0) >> 5
    (Cálculo = 5) >> +
    (Cálculo = 5) >> 3
    (Cálculo = 8) >> *
    (Cálculo = 8) >> resultado
    (Cálculo = 8) >> ** 2
    (Cálculo = 64) >> 
```

5.1. **Realizar operaciones secuenciales**: 
   - La calculadora permite realizar cálculos secuenciales con los operadores disponibles, como `+`, `-`, `x`, `*`, `/`, `:`, `**` o `exp`.
   - En el ejemplo anterior, se ingresan 5 y se suma 3, luego se multiplica el cálculo realizado por el valor almacenado en la calculadora (con `resultado`... observad que es 1... *Operación (RES => 1.00)*), y finalmente se eleva al cuadrado con `** 2`.

5.2. **Opciones para terminar o cancelar la secuencia**:
   - **Cancelar**: Para salir sin actualizar el resultado final, escribe `cancelar` y presiona <ENTER>.
   - **Actualizar resultado**: Deja la entrada en blanco y presiona <ENTER> para finalizar y actualizar el resultado en la calculadora.

5.3. **Ejemplo de salida al cancelar:**

Si escribimas `cancelar`:

```
Operación (RES => 1.00) >> calculo

## Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo ##

    (Cálculo = 0) >> 5
    (Cálculo = 5) >> +
    (Cálculo = 5) >> 3
    (Cálculo = 8) >> *
    (Cálculo = 8) >> resultado
    (Cálculo = 8) >> ** 2
    (Cálculo = 64) >> cancelar
Secuencia cancelada. Resultado almacenado sin cambios.

Presione ENTER para continuar...
```

Al pulsar ENTER y volver, el resultado de la calculadora no se debe haber actualizado:

```
Operación (RES => 1.00) >>
```

5.3. **Ejemplo de salida al terminar para actualizar el resultado:**

Si solo dejamos la entrada vacía y pulsamos ENTER:

```
Operación (RES => 1.00) >> calculo

## Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo ##

    (Cálculo = 0) >> 5
    (Cálculo = 5) >> +
    (Cálculo = 5) >> 3
    (Cálculo = 8) >> *
    (Cálculo = 8) >> resultado
    (Cálculo = 8) >> ** 2
    (Cálculo = 64) >> 

Presione ENTER para continuar...
```

Al pulsar ENTER y volver, el resultado de la calculadora se debe haber actualizado:

```
Operación (RES => 64.00) >>
```

### **6. Salir de la calculadora**
Para cerrar la aplicación, ingresa una entrada vacía y presiona `ENTER`. La calculadora preguntará si deseas salir:

```
Operación (RES => 64.00) >> 
¿Desea salir de la calculadora? (s/n) s
```

Después de contestar 's' y pulsar `ENTER`, se debe limpiar la consola y mostrar un mensaje de despedida, finalizando la aplicación:

```


Bye, bye...


```

Si contesta cualquier otra cosa, limpia la pregunta y vuelve al prompt a la espera de un comando:

```
Operación (RES => 64.00) >> 
¿Desea salir de la calculadora? (s/n) noooo
```

Después de contestar 'noooo' y pulsar `ENTER` vuelve al prompt:

```
Operación (RES => 64.00) >> 
```
