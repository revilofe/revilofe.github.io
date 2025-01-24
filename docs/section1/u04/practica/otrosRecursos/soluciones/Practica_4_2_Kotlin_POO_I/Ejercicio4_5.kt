package vtresvcuatro.u4
/**
### **Ejercicio 4.5**

1. Crear una clase `Tiempo`, que refleja las horas de un día, es decír, desde `00:00:00` hasta `23:59:59`,  con atributos `hora`, `minuto` y `segundo`, que pueda ser construida indicando los tres atributos, sólo hora y minuto o sólo la hora *(si no se indica, el valor de minuto o segundo será 0)*.

2. Crear el método `toString()` para mostrar el tiempo en formato: ***`XXh XXm XXs`***.

3. En el programa principal, debe solicitar por teclado hora, minuto y segundo de forma que se puedan omitir los segundos o los minutos *(y segundos, claro)* e instancie la clase `Tiempo` mostrando su valor.

4. A tener en cuenta:

 * Si segundos o minutos es mayor que 60, se tendrá que hacer las operaciones necesarios para incrementar la magnitud superior por el resultado del modulo de 60, quedándose en segundos o minutos con el resto. Es decir 65 segundos equivale a : 1 minuto y 5 segundos.
 * Hora siempre tendrá que ser menor que 24, si no, lanzará una excepción.

5. Añadir un nuevo método `incrementar(t:Tiempo):Boolean`, que incrementa en `t`, el total del tiempo que almacena el objeto que recibe el mensaje, devolviendo false si al incrementar se superan las `23:59:59`, en cuyo caso no cambiaría nada del objeto que recibe el mensaje. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al incrementar en `t` el tiempo, mostrando un mensaje de error si devuelve `false`.

6. Añadir un nuevo método `decrementar(t:Tiempo):Boolean`, que decrementa en `t`, el total del tiempo que almacena el objeto que recibe el mensaje, devolviendo false si al decrementar se superan las `00:00:00`, en cuyo caso no cambiaría nada del objeto que recibe el mensaje. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al decrementar en `t` el tiempo, mostrando un mensaje de error si devuelve `false`.

7. Añadir un nuevo método `comparar(t:Tiempo):Int`, que compara el tiempo que almacena el objeto que recibe el mensaje con el tiempo que almacena `t`, devolviendo -1 si el tiempo del objeto que recibe el mensaje es menor que `t`, 0 si son iguales y 1 si es mayor. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al comparar el tiempo del objeto que recibe el mensaje con el tiempo de `t`.

8. Añadir un nuevo método `copiar():Tiempo`, que devuelve un objeto `Tiempo` con el mismo tiempo que almacena el objeto que recibe el mensaje. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al copiar el tiempo del objeto que recibe el mensaje en un nuevo objeto `Tiempo`.

9. Añadir un nuevo método `copiar(t:Tiempo):Tiempo`, que copia el tiempo que almacena `t` en el objeto que recibe el mensaje. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al copiar el tiempo de `t` en el objeto que recibe el mensaje.

10. Añadir un nuevo método `sumar(t:Tiempo):Tiempo?`, que suma el tiempo que almacena el objeto que recibe el mensaje con el tiempo que almacena `t`, devolviendo un nuevo objeto `Tiempo` con el resultado o `null` si el resultado es mayor que `23:59:59`. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al sumar el tiempo del objeto que recibe el mensaje con el tiempo de `t`.

11. Añadir un nuevo método `restar(t:Tiempo):Tiempo?`, que resta el tiempo que almacena el objeto que recibe el mensaje con el tiempo que almacena `t`, devolviendo un nuevo objeto `Tiempo` con el resultado o `null` si el resultado es menor que `00:00:00`. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al restar el tiempo del objeto que recibe el mensaje con el tiempo de `t`.

12. Añadir un nuevo método `esMayorQue(t:Tiempo):Boolean`, que devuelve true si el tiempo que almacena el objeto que recibe el mensaje es mayor que el tiempo que almacena `t`. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al comparar si el tiempo del objeto que recibe el mensaje es mayor que el tiempo de `t`.

13. Añadir un nuevo método `esMenorQue(t:Tiempo):Boolean`, que devuelve true si el tiempo que almacena el objeto que recibe el mensaje es menor que el tiempo que almacena `t`. En el programa principal, debe solicitar por teclado hora, minuto y segundo del objeto `t`. Mostrará por pantalla el resultado obtenido al comparar si el tiempo del objeto que recibe el mensaje es menor que el tiempo de `t`.
 **/

/**
 * Clase Tiempo.
 * Representa una unidad de tiempo con hora, minuto y segundo.
 * Permite realizar operaciones como incrementar, decrementar, comparar y sumar/restar tiempos.
 * Incluye validaciones para asegurar que los valores sean coherentes con las convenciones del reloj.
 * @param hora Hora del tiempo (debe estar entre 0 y 23).
 * @param minuto Minuto del tiempo (debe estar entre 0 y 59).
 * @param segundo Segundo del tiempo (debe estar entre 0 y 59).
 */
class Tiempo(hora: Int, minuto: Int, segundo: Int) {

    /**
     * Hora del tiempo.
     * Validación: debe estar entre 0 y 23.
     */
    var hora: Int = hora
        set(value) {
            require(value in 0..23) { "Hora no puede ser mayor que 23" }
            field = value
        }

    /**
     * Minuto del tiempo.
     * Validación: debe estar entre 0 y 59.
     */
    var minuto: Int = minuto
        set(value) {
            require(value in 0..59) { "Minuto no puede ser mayor que 59" }
            field = value
        }

    /**
     * Segundo del tiempo.
     * Validación: debe estar entre 0 y 59.
     */
    var segundo: Int = segundo
        set(value) {
            require(value in 0..59) { "Segundo no puede ser mayor que 59" }
            field = value
        }

    init {
        // Ajustes iniciales para normalizar valores mayores a 59 en minutos y segundos.
        var h = hora
        var m = minuto
        var s = segundo
        if (s > 59) {
            m += s / 60 // Incrementa los minutos según los segundos excedentes.
            s %= 60 // Calcula los segundos restantes.
        }
        if (m > 59) {
            h += m / 60 // Incrementa las horas según los minutos excedentes.
            m %= 60 // Calcula los minutos restantes.
        }
        require(h in 0..23) { "Hora inicial no puede ser mayor que 23" }
        this.hora = h
        this.minuto = m
        this.segundo = s
    }

    /**
     * Devuelve el tiempo en formato "XXh XXm XXs".
     * @return Representación del tiempo en formato legible.
     */
    override fun toString(): String {
        return "${hora}h ${minuto}m ${segundo}s"
    }

    /**
     * Incrementa el tiempo actual con los valores de otro objeto Tiempo.
     * @param t Objeto Tiempo a incrementar.
     * @return True si el incremento es exitoso, false si se supera "23:59:59".
     */
    fun incrementar(t: Tiempo): Boolean {
        var h = hora + t.hora // Suma las horas de ambos objetos.
        var m = minuto + t.minuto // Suma los minutos de ambos objetos.
        var s = segundo + t.segundo // Suma los segundos de ambos objetos.
        if (s > 59) {
            m += s / 60 // Convierte los segundos excedentes en minutos.
            s %= 60 // Calcula los segundos restantes.
        }
        if (m > 59) {
            h += m / 60 // Convierte los minutos excedentes en horas.
            m %= 60 // Calcula los minutos restantes.
        }
        if (h > 23) {
            return false // El incremento excede el límite de tiempo permitido.
        }
        hora = h
        minuto = m
        segundo = s
        return true
    }

    /**
     * Decrementa el tiempo actual con los valores de otro objeto Tiempo.
     * @param t Objeto Tiempo a decrementar.
     * @return True si el decremento es exitoso, false si se supera "00:00:00".
     */
    fun decrementar(t: Tiempo): Boolean {
        var h = hora - t.hora // Resta las horas de ambos objetos.
        var m = minuto - t.minuto // Resta los minutos de ambos objetos.
        var s = segundo - t.segundo // Resta los segundos de ambos objetos.
        if (s < 0) { // Si los segundos son negativos, ajusta los minutos.
            m -= 1 // Resta un minuto.
            s += 60 // Ajusta los segundos sumando 60.
        }
        if (m < 0) { // Si los minutos son negativos, ajusta las horas.
            h -= 1 // Resta una hora.
            m += 60 // Ajusta los minutos sumando 60.
        }
        if (h < 0) {
            return false // El decremento excede el límite de tiempo permitido.
        }
        hora = h
        minuto = m
        segundo = s
        return true
    }

    /**
     * Compara el tiempo actual con otro objeto Tiempo.
     * @param t Objeto Tiempo a comparar.
     * @return -1 si es menor, 0 si es igual, 1 si es mayor.
     */
    fun comparar(t: Tiempo): Int {
        return when {
            hora > t.hora -> 1 // El tiempo actual tiene más horas.
            hora < t.hora -> -1 // El tiempo actual tiene menos horas.
            minuto > t.minuto -> 1 // El tiempo actual tiene más minutos.
            minuto < t.minuto -> -1 // El tiempo actual tiene menos minutos.
            segundo > t.segundo -> 1 // El tiempo actual tiene más segundos.
            segundo < t.segundo -> -1 // El tiempo actual tiene menos segundos.
            else -> 0 // Los tiempos son iguales.
        }
    }

    /**
     * Crea una copia del tiempo actual.
     * @return Nuevo objeto Tiempo con los mismos valores.
     */
    fun copiar(): Tiempo {
        return Tiempo(hora, minuto, segundo) // Crea una nueva instancia con los valores actuales.
    }

    /**
     * Copia los valores de otro objeto Tiempo al tiempo actual.
     * @param t Objeto Tiempo del que se copiarán los valores.
     */
    fun copiar(t: Tiempo) {
        hora = t.hora
        minuto = t.minuto
        segundo = t.segundo
    }

    /**
     * Suma el tiempo actual con otro objeto Tiempo.
     * @param t Objeto Tiempo a sumar.
     * @return Nuevo objeto Tiempo con el resultado, o null si se supera "23:59:59".
     */
    fun sumar(t: Tiempo): Tiempo? {
        var h = hora + t.hora // Suma las horas de ambos objetos.
        var m = minuto + t.minuto // Suma los minutos de ambos objetos.
        var s = segundo + t.segundo // Suma los segundos de ambos objetos.
        if (s > 59) {
            m += s / 60 // Convierte los segundos excedentes en minutos.
            s %= 60 // Calcula los segundos restantes.
        }
        if (m > 59) {
            h += m / 60 // Convierte los minutos excedentes en horas.
            m %= 60 // Calcula los minutos restantes.
        }
        return if (h > 23) null else Tiempo(h, m, s) // Devuelve null si excede el límite permitido.
    }

    /**
     * Resta el tiempo actual con otro objeto Tiempo.
     * @param t Objeto Tiempo a restar.
     * @return Nuevo objeto Tiempo con el resultado, o null si se supera "00:00:00".
     */
    fun restar(t: Tiempo): Tiempo? {
        var h = hora - t.hora // Resta las horas de ambos objetos.
        var m = minuto - t.minuto // Resta los minutos de ambos objetos.
        var s = segundo - t.segundo // Resta los segundos de ambos objetos.
        if (s < 0) { // Si los segundos son negativos, ajusta los minutos.
            m -= 1 // Resta un minuto.
            s += 60 // Ajusta los segundos sumando 60.
        }
        if (m < 0) { // Si los minutos son negativos, ajusta las horas.
            h -= 1 // Resta una hora.
            m += 60 // Ajusta los minutos sumando 60.
        }
        return if (h < 0) null else Tiempo(h, m, s) // Devuelve null si excede el límite permitido.
    }

    /**
     * Verifica si el tiempo actual es mayor que otro objeto Tiempo.
     * @param t Objeto Tiempo a comparar.
     * @return True si es mayor, false en caso contrario.
     */
    fun esMayorQue(t: Tiempo): Boolean {
        return comparar(t) == 1 // Devuelve true si el resultado de comparar es 1.
    }

    /**
     * Verifica si el tiempo actual es menor que otro objeto Tiempo.
     * @param t Objeto Tiempo a comparar.
     * @return True si es menor, false en caso contrario.
     */
    fun esMenorQue(t: Tiempo): Boolean {
        return comparar(t) == -1 // Devuelve true si el resultado de comparar es -1.
    }
}

fun main() {
    // Ejemplos de uso y pruebas de la clase Tiempo.
    println("Creando un tiempo inicial...")
    val t = Tiempo(12, 45, 30) // Inicializa un objeto Tiempo con valores específicos.
    println("Tiempo inicial: $t")

    println("Incrementando el tiempo...")
    val incremento = Tiempo(2, 15, 40) // Crea un objeto Tiempo para incrementar.
    println("Tiempo a incrementar: $incremento")
    if (t.incrementar(incremento)) {
        println("Tiempo tras incremento: $t")
    } else {
        println("Error: Incremento supera el límite permitido.")
    }

    println("Decrementando el tiempo...")
    val decremento = Tiempo(1, 50, 50) // Crea un objeto Tiempo para decrementar.
    println("Tiempo a decrementar: $decremento")
    if (t.decrementar(decremento)) {
        println("Tiempo tras decremento: $t")
    } else {
        println("Error: Decremento supera el límite permitido.")
    }

    println("Comparando tiempos...")
    val otroTiempo = Tiempo(10, 30, 20) // Crea un objeto Tiempo para comparar.
    println("Tiempo a comparar: $otroTiempo")
    when (t.comparar(otroTiempo)) {
        -1 -> println("$t es menor que $otroTiempo")
        0 -> println("$t es igual que $otroTiempo")
        1 -> println("$t es mayor que $otroTiempo")
    }

    println("Copiando tiempo...")
    val copiaTiempo = t.copiar() // Crea una copia del objeto Tiempo actual.
    println("Tiempo copiado: $copiaTiempo")

    println("Sumando tiempos...")
    println("Tiempo a sumar: $otroTiempo")
    val sumaTiempo = t.sumar(otroTiempo) // Suma los valores de dos objetos Tiempo.
    if (sumaTiempo != null) {
        println("Resultado de la suma: $sumaTiempo")
    } else {
        println("Error: La suma supera el límite permitido.")
    }

    println("Restando tiempos...")
    println("Tiempo a restar: $otroTiempo")
    val restaTiempo = t.restar(otroTiempo) // Resta los valores de dos objetos Tiempo.
    if (restaTiempo != null) {
        println("Resultado de la resta: $restaTiempo")
    } else {
        println("Error: La resta supera el límite permitido.")
    }

    println("¿Es mayor el tiempo inicial que otro tiempo?")
    println("Resultado: ${t.esMayorQue(otroTiempo)}")

    println("¿Es menor el tiempo inicial que otro tiempo?")
    println("Resultado: ${t.esMenorQue(otroTiempo)}")
}