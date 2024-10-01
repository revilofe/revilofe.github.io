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
 * @param hora Hora del tiempo
 * @param minuto Minuto del tiempo
 * @param segundo Segundo del tiempo
 * @throws IllegalArgumentException Si la hora es mayor que 23
 */
class Tiempo(hora: Int, minuto: Int, segundo: Int) {
    var hora: Int = hora
        set(value) {
            require(value in 0..23) { "Hora no puede ser mayor que 23" }
            field = value
        }
    var minuto: Int = minuto
        set(value) {
            require(value in 0..59) { "Minuto no puede ser mayor que 59" }
            field = value
        }
    var segundo: Int = segundo
        set(value) {
            require(value in 0..59) { "Segundo no puede ser mayor que 59" }
            field = value
        }

    init {
        var h = hora
        var m = minuto
        var s = segundo
        if (s > 59) {
            m += s / 60
            s %= 60
        }
        if (m > 59) {
            h += m / 60
            m %= 60
        }
        //require(value in 0..23) { "Hora no puede ser mayor que 23" }

        this.hora = h
        this.minuto = m
        this.segundo = s
    }

    /**
     * Devuelve el tiempo en formato XXh XXm XXs
     */
    override fun toString(): String {
        return "${hora}h ${minuto}m ${segundo}s"
    }

    /**
     * Incrementa el tiempo en t, el total del tiempo que almacena el objeto que recibe el mensaje, devolviendo false si al incrementar se superan las 23:59:59, en cuyo caso no cambiaría nada del objeto que recibe el mensaje.
     * @param t Tiempo a incrementar
     * @return True si se incrementa correctamente, false en caso contrario
     */
    fun incrementar(t: Tiempo): Boolean {
        var h = hora + t.hora
        var m = minuto + t.minuto
        var s = segundo + t.segundo
        if (s > 59) {
            m += s / 60
            s %= 60
        }
        if (m > 59) {
            h += m / 60
            m %= 60
        }
        if (h > 23) {
            return false
        }
        hora = h
        minuto = m
        segundo = s
        return true
    }

    /**
     * TODO: Decrementa el tiempo en t, el total del tiempo que almacena el objeto que recibe el mensaje, devolviendo false si al decrementar se superan las 00:00:00, en cuyo caso no cambiaría nada del objeto que recibe el mensaje.
     *
     * @param t Tiempo a decrementar
     * @return True si se decrementa correctamente, false en caso contrario
     */
    fun decrementar(t: Tiempo): Boolean {
        var h = hora - t.hora
        var m = minuto - t.minuto
        var s = segundo - t.segundo
        if (s < 0) {
            m -= s / 60
            s %= 60
        }
        if (m < 0) {
            h -= m / 60
            m %= 60
        }
        if (h < 0) {
            return false
        }
        hora = h
        minuto = m
        segundo = s
        return true
    }

    /**
     * Compara el tiempo que almacena el objeto que recibe el mensaje con el tiempo que almacena t, devolviendo -1 si el tiempo del objeto que recibe el mensaje es menor que t, 0 si son iguales y 1 si es mayor.
     *
     * @param t Tiempo a comparar
     * @return -1 si el tiempo del objeto que recibe el mensaje es menor que t, 0 si son iguales y 1 si es mayor
     */
    fun comparar(t: Tiempo): Int {
        if (hora > t.hora) {
            return 1
        } else if (hora < t.hora) {
            return -1
        } else {
            if (minuto > t.minuto) {
                return 1
            } else if (minuto < t.minuto) {
                return -1
            } else {
                if (segundo > t.segundo) {
                    return 1
                } else if (segundo < t.segundo) {
                    return -1
                } else {
                    return 0
                }
            }
        }
    }

    /**
     * Devuelve un objeto Tiempo con el mismo tiempo que almacena el objeto que recibe el mensaje.
     *
     * @return Objeto Tiempo con el mismo tiempo que almacena el objeto que recibe el mensaje
     */
    fun copiar(): Tiempo {
        return Tiempo(hora, minuto, segundo)
    }

    /**
     * Copia el tiempo que almacena t en el objeto que recibe el mensaje.
     *
     * @param t Tiempo a copiar
     */
    fun copiar(t: Tiempo) {
        hora = t.hora
        minuto = t.minuto
        segundo = t.segundo
    }

    /**
     * Suma el tiempo que almacena el objeto que recibe el mensaje con el tiempo que almacena t, devolviendo un nuevo objeto Tiempo con el resultado o null si el resultado es mayor que 23:59:59.
     *
     * @param t Tiempo a sumar
     * @return Objeto Tiempo con el resultado de la suma o null si el resultado es mayor que 23:59:59
     */
    fun sumar(t: Tiempo): Tiempo? {
        var h = hora + t.hora
        var m = minuto + t.minuto
        var s = segundo + t.segundo
        if (s > 59) {
            m += s / 60
            s %= 60
        }
        if (m > 59) {
            h += m / 60
            m %= 60
        }
        if (h > 23) {
            return null
        }
        return Tiempo(h, m, s)
    }

    /**
     * Resta el tiempo que almacena el objeto que recibe el mensaje con el tiempo que almacena t, devolviendo un nuevo objeto Tiempo con el resultado o null si el resultado es menor que 00:00:00.
     *
     * @param t Tiempo a restar
     * @return Objeto Tiempo con el resultado de la resta o null si el resultado es menor que 00:00:00
     */
    fun restar(t: Tiempo): Tiempo? {
        var h = hora - t.hora
        var m = minuto - t.minuto
        var s = segundo - t.segundo
        if (s < 0) {
            m -= s / 60
            s %= 60
        }
        if (m < 0) {
            h -= m / 60
            m %= 60
        }
        if (h < 0) {
            return null
        }
        return Tiempo(h, m, s)
    }

    /**
     * Devuelve true si el tiempo que almacena el objeto que recibe el mensaje es mayor que el tiempo que almacena t.
     *
     * @param t Tiempo a comparar
     * @return True si el tiempo que almacena el objeto que recibe el mensaje es mayor que el tiempo que almacena t
     */
    fun esMayorQue(t: Tiempo): Boolean {
        return comparar(t) == 1
    }

    /**
     * Devuelve true si el tiempo que almacena el objeto que recibe el mensaje es menor que el tiempo que almacena t.
     *
     * @param t Tiempo a comparar
     * @return True si el tiempo que almacena el objeto que recibe el mensaje es menor que el tiempo que almacena t
     */
    fun esMenorQue(t: Tiempo): Boolean {
        return comparar(t) == -1
    }
}

fun main(){
    println("Creando tiempo con 0,0,0, y seteando hora, minuto y segundo")
    var t = Tiempo(0,0,0)
    println("Introduce hora:")
    t.hora = readln().toInt()
    println("Introduce minuto:")
    t.minuto = readln().toInt()
    println("Introduce segundo:")
    t.segundo = readln().toInt()
    println(t)
    println("Creando tiempo a partir de hora, minuto y segundo")
    println("Introduce hora:")
    var h = readln().toInt()
    println("Introduce minuto:")
    var m = readln().toInt()
    println("Introduce segundo:")
    var s = readln().toInt()
    var t2 = Tiempo(h,m,s)
    println("Incrementando $t con $t2")
    if (t.incrementar(t2)) {
        println(t)
    } else {
        println("Error al incrementar")
    }
    println("Decrementando $t con $t2")
    if (t.decrementar(t2)) {
        println(t)
    } else {
        println("Error al decrementar")
    }
    readln()
    println("Comparando $t con $t2")
    when (t.comparar(t2)) {
        -1 -> println("$t es menor que $t2")
        0 -> println("$t es igual que $t2")
        1 -> println("$t es mayor que $t2")
    }
    readln()
    println("Copiando $t en t2")
    var t3 = t.copiar()
    println(t3)
    println("Copiando $t2 en t")
    t.copiar(t2)
    println(t)
    readln()
    println("Sumando $t con $t2")
    var t4 = t.sumar(t2)
    if (t4 != null) {
        println(t4)
    } else {
        println("Error al sumar")
    }
    readln()
    println("Restando $t con $t2")
    var t5 = t.restar(t2)
    if (t5 != null) {
        println(t5)
    } else {
        println("Error al restar")
    }
    readln()
    println("¿$t es mayor que $t2?")
    println(t.esMayorQue(t2))
    println("¿$t es menor que $t2?")
    println(t.esMenorQue(t2))
    
}