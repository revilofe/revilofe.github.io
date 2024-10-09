# BORRADOR

## Ideas para que realicen los alumnos:

### Falta relacionar con los RA y CE...

1. Unifica las funciones es_binario, es_octal, es_decimal, y es_hexadecimal, que verifican si un número es válido en una base particular, en una única función más genérica que acepte la base y realice la validación basada en esa entrada. 

2. Permite la conversión de números negativos. Muy simple, permitiendo números negativos y la conversión debe llevar el mismo signo negativo. Si realizas este cambio los tests unitarios funcionarán y podrás ver su resultado.

3. Una vez eliminadas las funciones es_binario, es_octal, es_decimal y es_hexadecimal refactoriza la función comprobar_valor_base. 

4. Ejecuta los tests unitarios y corrije los posibles errores que se produzcan.
	
5. Haz que el programa solo termine cuando se introduzca ENTER en la primera pregunta, cuando se introduce la base original del número. 

	5.1. Si se introduce una cadena vacía o solo con espacios, debe realizar la pregunta "¿Desea salir del programa? (S/N) "... si contesta "S", "s", "  s ", "  S  ", "si", " Si", " S I ", "sI", "s  i" (tanto en español con "s" y "si", como en inglés con "y" y "yes" con cualquier combinación de mayúsculas, minúsculas y espacios entre las letras, por delante y por detrás) terminará el programa, pero si contesta cualquier otra cosa continuará.

	5.2. Cuando el programa realice una conversión debe mostrar el mensaje de salida o el error si se ha producido, limpiar pantalla y volver a preguntar.

6. Cuando acabe el programa, justo antes debe mostrar un mensaje con el número de conversiones realizadas.

7. Cambia el código para evitar que se pueda convertir un número a la misma base numérica de origen, es decir, no se puede convertir un número en base decimal a la misma base decimal.

8. Utiliza DocStrings para documentar las funciones que no están documentadas, las que hayas modificado si lo necesitan y las nuevas funciones desarrolladas en el código explicando brevemente que hace cada una.

9. Refactoriza el código y elimina las funciones que ya no se utilizan si existe alguna que ya no se llame desde ningún luigar del código, es decir, si no se utiliza.
