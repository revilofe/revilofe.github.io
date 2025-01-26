
## **Guía de ayuda para realizar los apartados 5 al 13 del ejercicio 4.5 - Tiempo**

### **5. Método `incrementar(t:Tiempo):Boolean`**

1. **Propósito:**
    - Incrementar el tiempo del objeto actual con el tiempo que almacena `t`.
    - Si el resultado excede `23:59:59`, no modifica el tiempo y devuelve `false`.
    - Si todo ok, devuelve `true`.

2. **Pistas:**
    - Convertir el tiempo actual y `t` a segundos facilita la suma.
    - Validar si la suma excede los segundos equivalentes a `23:59:59` (86399 segundos).
    - Podéis crear la constante `MAX_SEGUNDOS` = 86399 en el companion object.
    - Si no excede, actualizar el tiempo usando una función que convierta los segundos totales de vuelta a horas, minutos y segundos.

3. **Lógica:**
    - Crea un nuevo método `obtenerSegundos` para calcular y retornar los segundos totales del objeto actual.
    - El método `obtenerSegundos` también podrás utilizarlo para el objeto `t` que se pasa como argumento.
    - Si la suma no excede el límite, actualiza el tiempo del objeto actual.
    - También podéis crear otro método, `actualizarTiempoConSegundos` para convertir los segundos en hora, min y seg y actualizar las propiedades del objeto. 

   /**
    * Convierte las horas, minutos y segundos del objeto actual en un total de segundos y lo retorna.
    *
    * @return El tiempo total en segundos.
    */
   private fun obtenerSegundos(): Int {
       //TODO: retornar el tiempo en segundos utilizando las propiedades hora, min y seg.
   }

   /**
    * Actualiza los valores de hora, minuto y segundo del objeto actual
    * con base en un total de segundos.
    *
    * @param totalSegundos El tiempo total en segundos.
    */
   private fun actualizarTiempoConSegundos(totalSegundos: Int) {
       //TODO: convertir segundos a hora, min y seg para actualizar las propiedades
   }

### **6. Método `decrementar(t:Tiempo):Boolean`**

1. **Propósito:**
    - Decrementar el tiempo del objeto actual con el tiempo que almacena `t`.
    - Si el resultado es menor que `00:00:00`, no modifica el tiempo y devuelve `false`.

2. **Pistas:**
    - Similar al método `incrementar`, pero en lugar de sumar los segundos, los resta.
    - Validar si el resultado es negativo antes de actualizar el tiempo.
    - Reutiliza la función auxiliar para actualizar el tiempo con los segundos restantes.

3. **Lógica:**
    - Calcula los segundos totales del objeto actual y de `t`.
    - Si la resta da un resultado negativo, devuelve `false`.
    - Si no es negativo, actualiza el tiempo.

### **7. Método `comparar(t:Tiempo):Int`**

1. **Propósito:**
    - Comparar el tiempo del objeto actual con el tiempo de `t`, devolviendo:
        - `-1` si el tiempo actual es menor.
        - `0` si son iguales.
        - `1` si el tiempo actual es mayor.

2. **Pistas:**
    - Usa los segundos totales para realizar la comparación.
    - Reutiliza el método `obtenerSegundos` para obtener los valores en segundos.
    - Usa un bloque `when` o `if` para devolver el resultado de la comparación.

3. **Lógica:**
    - Obtén los segundos totales de ambos objetos.
    - Compara los valores y devuelve el resultado.

### **8. Método `copiar():Tiempo`**

1. **Propósito:**
    - Crear y devolver un nuevo objeto `Tiempo` con los mismos valores que el objeto actual.

2. **Pistas:**
    - Reutiliza el constructor de la clase para crear un nuevo objeto.
    - Pasa las propiedades `hora`, `min` y `seg` del objeto actual al constructor.

3. **Lógica:**
    - Retorna un nuevo objeto `Tiempo` inicializado con los valores actuales.

### **9. Método `copiar(t:Tiempo):Tiempo`**

1. **Propósito:**
    - Copiar el tiempo del objeto `t` en el objeto actual.

2. **Pistas:**
    - Modifica directamente las propiedades `hora`, `min` y `seg` del objeto actual con los valores de `t`.
    - Este método devuelve el mismo objeto que recibe como argumento de entrada.

3. **Lógica:**
    - Asigna los valores de `t.hora`, `t.min` y `t.seg` al objeto actual.
    - Retorna el objeto que se le ha pasado como único parámetro del método.

### **10. Método `sumar(t:Tiempo):Tiempo?`**

1. **Propósito:**
    - Sumar el tiempo del objeto actual con el tiempo de `t`.
    - Devuelve un nuevo objeto `Tiempo` con el resultado, o `null` si el resultado excede `23:59:59`.

2. **Pistas:**
    - Usa el método `incrementar` para evitar duplicar la lógica.
    - Crea una copia del objeto actual antes de intentar la suma.
    - Si `incrementar` devuelve `true`, retorna la copia actualizada. De lo contrario, retorna `null`.

3. **Lógica:**
    - Usa `copiar` para crear una copia del objeto actual.
    - Aplica `incrementar` en la copia.
    - Retorna la copia si la operación es válida o `null` si no lo es.

### **11. Método `restar(t:Tiempo):Tiempo?`**

1. **Propósito:**
    - Restar el tiempo del objeto actual con el tiempo de `t`.
    - Devuelve un nuevo objeto `Tiempo` con el resultado, o `null` si el resultado es menor que `00:00:00`.

2. **Pistas:**
    - Similar al método `sumar`, pero usa `decrementar`.
    - Crea una copia del objeto actual antes de intentar la resta.
    - Si `decrementar` devuelve `true`, retorna la copia actualizada. De lo contrario, retorna `null`.

3. **Lógica:**
    - Usa `copiar` para crear una copia del objeto actual.
    - Aplica `decrementar` en la copia.
    - Retorna la copia si la operación es válida o `null` si no lo es.

### **12. Método `esMayorQue(t:Tiempo):Boolean`**

1. **Propósito:**
    - Determinar si el tiempo del objeto actual es mayor que el tiempo de `t`.

2. **Pistas:**
    - Compara los segundos totales del objeto actual y de `t`.
    - Reutiliza el método `obtenerSegundos`.

3. **Lógica:**
    - Retorna `true` si los segundos del objeto actual son mayores que los de `t`.

### **13. Método `esMenorQue(t:Tiempo):Boolean`**

1. **Propósito:**
    - Determinar si el tiempo del objeto actual es menor que el tiempo de `t`.

2. **Pistas:**
    - Similar a `esMayorQue`, pero verifica si los segundos totales son menores.

3. **Lógica:**
    - Retorna `true` si los segundos del objeto actual son menores que los de `t`.

## **Consejos Generales para Resolver el Ejercicio**

- **Reutilización de Métodos:**
    - Piensa en cómo los métodos existentes pueden ayudarte a implementar nuevos métodos sin duplicar lógica. Por ejemplo, `sumar` y `restar` reutilizan `incrementar` y `decrementar`.

- **Creación de los métodos `obtenerSegundos` y `actualizarTiempoConSegundos`:**
    - Estos métodos son clave para simplificar las operaciones de comparación, suma y resta de tiempos.

- **Pruebas Graduales:**
    - Implementa un método a la vez y verifica su funcionamiento con casos simples en el programa principal antes de pasar al siguiente.

- **Validaciones:**
    - Asegúrate de manejar los casos límite, como tiempos negativos o mayores que `23:59:59`.
