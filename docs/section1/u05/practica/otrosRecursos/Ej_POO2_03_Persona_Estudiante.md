## Persona y Estudiante

1. **Clases y Objetos Básicos:**
    - Crea una clase `Persona` que tenga dos propiedades: `nombre` y `edad`. Luego, en el main crea un objeto de esta clase e imprime sus propiedades.

2. **Métodos Simples:**
    - Añade un método `cumple` a la clase `Persona` que incremente la edad de la persona en uno cada vez que se llama.
    - Sobreescribe el método toString() y prográmalo para que se muestre una persona con todas sus propiedades.
      Por ejemplo "Persona (nombre = Lucía, edad = 21)".
    - En el main ejecuta el cumple de la persona y muestra su información de dos formas: accediendo a sus propiedades y mediante el método toString()
      *(recuerda que no es necesario llamar al método toString(), sino que se invocará automáticamente cuando necesite realizar la conversión del contenido a String)*

3. **Encapsulamiento:**
    - Modifica la clase `Persona` para hacer la propiedad `edad` privada y añade un método `mostrarEdad()` para acceder a su valor.

4. **Herencia:**
    - Crea una clase `Estudiante` que herede de `Persona` y añade una propiedad `carrera`. Las propiedades deben incluir el modificador `open` *(vuelve a dejar la propiedad edad pública)*
    - Realiza de nuevo un override de toString() para completar la información de Estudiante *(intenta usar el resultado del método de la clase padre y completarlo)*.

5. **Polimorfismo:**
    - Añade un método `actividad()` a la clase `Persona` que imprima "Lucía está realizando una actividad." y sobrescríbelo en `Estudiante` para que muestre un mensaje específico para estudiantes.
    - Crea en el main a una persona y un estudiante y muestra la actividad que realizan.

6. **Clases y Objetos con Validación:**
    - Modifica la clase `Persona` para que no acepte nombres vacíos y edades negativas. Utiliza un constructor primario con valores por defecto para edad.
    - Prueba a crer un estudiante con una edad negativa, controlando las excepciones y mostrando el mensaje de error específico.
    
