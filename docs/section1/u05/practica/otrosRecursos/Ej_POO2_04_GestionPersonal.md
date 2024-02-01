### Ejercicio: Sistema de Gestión de Personal en una Empresa

**Requisitos:**

1. **Clase Base `Persona`:**

    - Propiedades:

        - `nombre` (String)
        - `edad` (Int)
    
    - Métodos:

        - `toString()`: Devuelve una cadena con información básica sobre la persona *(por ejemplo, "Nombre: Julia, Edad: 24")*.
        - `celebrarCumple()`: Incrementa la edad en 1 y retorna un mensaje de felicitación *(por ejemplo, "Feliz cumpleaños Julia! Ahora tienes 25 años.")*.  

2. **Clase Derivada `Empleado` (de `Persona`):**
    
    - Propiedades:
        - `salarioBase` (Double) *(Intenta permitir también que se pueda construir un empleado con un argumento Int en esta propiedad)*
        - `porcentajeImpuestos` (Double) *(Intenta permitir también que se pueda construir un empleado con un argumento Int en esta propiedad)* *(El valor por defecto es 10.0)*
    
    - Métodos:
        - `calcularSalario()`: Devuelve el salarioBase aplicando los impuestos.
        - `toString()`: Devuelve una cadena que incluye la información de `Persona` y detalles adicionales del `Empleado`
          *(por ejemplo, "Nombre: Julia, Edad: 24, Salario: 28213.47€" con 2 posiciones decimales para el salario)*.
        - `trabajar()`: Retorna un mensaje que indica que el empleado está trabajando. *(por ejemplo, "Pablo está trabajando en la empresa.")*

3. **Clase Derivada `Gerente` (de `Empleado`):**
    
    - Propiedades:
        - `bonus` (Double)
        - `exentoImpuestos` (Boolean) *(Por defecto no estará exento de los impuestos)*
        - Sobreescribir el porcentajeImpuestos para que los gerentes tengan un porcentaje de impuestos siempre del 33.99%.
    
    - Métodos:
        - `calcularSalario()`: Devuelve el salarioBase más el bonus aplicando los impuestos solo al salario base o sin aplicar impuestos si exentoImpuestos es `true`.
        - `toString()`: Devuelve una cadena que incluye la información de `Persona` y `Empleado`, además de detalles específicos del `Gerente`.
        - `administrar()`: Retorna un mensaje que indica que el gerente está administrando. *(por ejemplo, "Ana está administrando la empresa.")*

4. **Uso en la Función `main`:**

    Crear una persona, un empleado y un gerente. Realizar distintas pruebas... para cada uno mostrar su información y ejecutar los métodos que tienen accesibles.
