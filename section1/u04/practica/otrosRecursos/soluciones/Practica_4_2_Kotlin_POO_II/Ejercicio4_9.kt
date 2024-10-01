package vtresvcuatro.u4

import com.github.ajalt.mordant.rendering.TextColors.*
import com.github.ajalt.mordant.rendering.TextStyles.bold
import com.github.ajalt.mordant.rendering.TextStyles.strikethrough
import com.github.ajalt.mordant.terminal.Terminal
import vtresvcuatro.u4.Estado.*
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter


/**
 * ### **Ejercicio 4.9**
 *
 *    1. Realizar un programa para gestionar una Lista de tareas con POO.
 *
 *    2. El programa debe mostrar un menú en el que se pueda agregar (por defecto una nueva tarea tendrá el estado pendiente), eliminar y cambiar el estado de una tarea. También será posible mostrar la lista de tareas (todas las tareas), mostrar la lista de tareas pendientes y la lista de tareas ya realizadas.
 *
 *    3. Una tarea debe tener un identificador (podrá indicarlo o generarlo automáticamente), una descripción y un estado que indique si está pendiente o ya fue realizada (en este caso, deberá mostrar la fecha, con formato DD-MM-AAAA HH:MM:SS, en la que se marcó cómo realizada) *
 *
 *    4. Os muestro un ejemplo de cómo generar una fecha:
 *
 *       ```
 *       import java.time.LocalDateTime
 *       import java.time.format.DateTimeFormatter
 *       fun main() {
 *           val fechaHoraActual: LocalDateTime = LocalDateTime.now()
 *           // Formatear la fecha y hora para imprimir
 *           val formatter: DateTimeFormatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")
 *           val fechaFormateada: String = fechaHoraActual.format(formatter)
 *           println("Fecha y Hora Actual: $fechaFormateada")
 *       }
 *       ```
 *
 *
 *
 */


/**
 * Enumerado Estado
 * @property PENDIENTE Estado pendiente
 * @property REALIZADA Estado realizada
 * @property EN_PROCESO Estado en proceso.
 * @property ELIMINADA Estado eliminada
 * @property CANCELADA Estado cancelada.
 * @constructor Crea un enumerado con los estados de una tarea
 */
enum class Estado {
    PENDIENTE, EN_PROCESO, ELIMINADA, CANCELADA, REALIZADA
}


/**
 * Clase Tarea
 * @param descripcion Descripcion de la tarea
 * @constructor Crea una tarea con descripcion
 *
 */
class Tarea(private val descripcion: String) {

    companion object{
        private var contador = 0

        /**
         * Devuelve un identificador de tarea
         * @return Identificador de tarea
         */
        private fun dameId():String{
            contador++
            return contador.toString()
        }
    }

    /**
     * Identificador de la tarea
     */
    val id: String = dameId()

    /**
     * Estado de la tarea. Por defecto es PENDIENTE. Si el estado es REALIZADA, la fecha de realizacion es la fecha actual. Otros estados no tienen fecha de realización.
     */
    var estado = PENDIENTE
        set(value) {
            field = value
            fechaRealizacion = if (value == REALIZADA)
                dameFecha()
            else
                null
        }

    /**
     * Fecha de realizacion de la tarea. Si el estado no es REALIZADA, la fecha de realizacion es null
     */
    private var fechaRealizacion: String? = null

    /**
     * Devuelve la tarea en formato String
     * @return Tarea en formato String
     */
    override fun toString(): String {
        return "Tarea(id='$id', descripcion='$descripcion', estado=$estado, fechaRealizacion=$fechaRealizacion)"
    }


    private fun dameFecha(): String {
        val fechaHoraActual: LocalDateTime = LocalDateTime.now()
        // Formatear la fecha y hora para imprimir
        val formatter: DateTimeFormatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")
        return fechaHoraActual.format(formatter)
    }

}

/**
 * Clase ListaTareas
 * @constructor Crea una lista de tareas
 *
 */
class ListaTareas {
    private val tareas = mutableListOf<Tarea>()

    /**
     * Agrega una tarea a la lista
     * @param tarea Tarea a agregar
     */
    fun agregarTareas(tarea:Tarea){

        tareas.add(tarea)
    }

    /**
     * Devuelve una lista de tareas por estado
     * @param estado Estado de la tarea
     * @return Lista de tareas por estado
     */
    fun listaTareasPorEstado(estado:Estado):List<Tarea>{
        return tareas.filter { it.estado == estado }
    }

    /**
     * Cambia el estado de una tarea por su id
     * @param idTarea Identificador de la tarea
     * @param estado Estado de la tarea
     */
    fun cambiaEstadoPorId(idTarea:String, estado:Estado)
    {
        val tarea = tareas.filter { it.id == idTarea }
        if (tarea.isNotEmpty())
            tarea[0].estado = estado
    }

    /**
     * Elimina logicamente una tarea por su id
     * @param idTarea Identificador de la tarea
     */
    fun eliminaLogicoTareaPorId(idTarea:String)
    {
        cambiaEstadoPorId(idTarea, ELIMINADA)
    }

    /**
     * Devuelve una lista de todas las tareas
     * @return Lista de todas las tareas
     */
    fun listaTodasLasTareas():List<Tarea>{
        return tareas.toList()
    }

}

/**
 * Clase MenuConsola
 * @constructor Crea un menu de consola. Realiza las operaciones del menu: agregar, eliminar, cambiar estado y mostrar tareas
 *
 */
object MenuConsola{
    private val listaTareas = ListaTareas()
    private val t = Terminal()

    /**
     * Muestra el menu
     */
    fun mostrarMenu(){
        var opcion: Int
        val style = (bold + green)

        do {
            t.println(style("******************************************"))
            t.println(style("*                  Menu                  *"))
            t.println(style("******************************************"))
            t.println(style("1. Agregar tarea"))
            t.println(style("2. Eliminar tarea"))
            t.println(style("3. Cambiar estado de tarea"))
            t.println(style("4. Mostrar lista de tareas"))
            t.println(style("5. Mostrar lista de tareas pendientes"))
            t.println(style("6. Mostrar lista de tareas realizadas"))
            t.println(style("7. Salir"))
            t.print(cyan("---------------> Introduce una opcion: "))
            opcion = readln().toIntOrNull() ?: 0
            when (opcion) {
                1 -> agregarTarea()
                2 -> eliminarTarea()
                3 -> cambiarEstadoTarea()
                4 -> mostrarTareas()
                5 -> mostrarTareasPendientes()
                6 -> mostrarTareasRealizadas()
                7 -> println("Adios!!")
                else -> println("Opcion incorrecta")
            }
        } while (opcion != 7)
    }

    /**
     * Agrega una tarea
     */
    private fun agregarTarea() {
        println("Agregar tarea")
        println("----------------------------------------")
        print("------> Introduce la descripcion de la tarea: ")
        val descripcion = readlnOrNull() ?: ""
        listaTareas.agregarTareas(Tarea(descripcion))
    }

    /**
     * Muestra las tareas realizadas
     */
    private fun mostrarTareasRealizadas() {
        println("Tareas realizadas")
        println("----------------------------------------")
        listaTareas.listaTareasPorEstado(REALIZADA).forEach { println(it) }
    }

    /**
     * Muestra las tareas pendientes
     */
    private fun mostrarTareasPendientes() {
        println("Tareas pendientes")
        println("----------------------------------------")
        listaTareas.listaTareasPorEstado(PENDIENTE).forEach { println(it) }
    }

    /**
     * Muestra todas las tareas
     */
    private fun mostrarTareas() {
        t.println(blue("Todas las tareas"))
        t.println(blue("----------------------------------------"))
        listaTareas.listaTodasLasTareas().forEach {tarea ->
            when (tarea.estado) {
                PENDIENTE -> {t.println(red(tarea.toString()))}
                REALIZADA -> {t.println(green(tarea.toString()))}
                CANCELADA, ELIMINADA -> {t.println(strikethrough(tarea.toString()))}
                else -> t.println(tarea.toString())
            }
        }
    }

    /**
     * Cambia el estado de una tarea
     */
    private fun cambiarEstadoTarea() {
        t.println(blue("Cambiar estado de tarea"))
        t.println(blue("----------------------------------------"))
        val idTarea = t.prompt("------> Introduce el id de la tarea:") ?: "0"
        Estado.entries.forEachIndexed { indice, estado -> t.println("($indice) $estado") }
        val estado = t.prompt("Introduce el id del estado a asignar a la tarea:") ?: "0"
        listaTareas.cambiaEstadoPorId(idTarea, Estado.entries[estado.toInt()])

    }

    /**
     * Elimina una tarea
     */
    private fun eliminarTarea() {
        t.println("Eliminar tarea")
        t.println("----------------------------------------")
        val idTarea = t.prompt("------> Introduce el id de la tarea:") ?: "0"
        listaTareas.eliminaLogicoTareaPorId(idTarea)
    }


}

fun main()
{
    MenuConsola.mostrarMenu()
}