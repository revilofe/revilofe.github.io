# U2.3 - Manejo de Excepciones

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son las excepciones?

* Eventos anómalos que interrumpen el flujo normal
* Diferentes de los errores de código
* Se pueden manejar para evitar que el programa se detenga
* Python usa try-except para capturarlas

Note: Las excepciones son situaciones inesperadas que ocurren durante la ejecución. A diferencia de los errores de sintaxis que impiden que el código se ejecute, las excepciones ocurren mientras el programa está corriendo. Por ejemplo, dividir por cero o intentar abrir un archivo que no existe.


### Errores vs Excepciones

* **Errores**: Problemas en el código que deben corregirse
* **Excepciones**: Situaciones inesperadas manejables
* Los errores se arreglan editando código
* Las excepciones se manejan con try-except

Note: Los errores (bugs) son problemas de lógica, sintaxis o diseño que requieren corrección del código fuente. Las excepciones son situaciones que pueden ocurrir incluso con código correcto, como que el usuario introduzca texto en lugar de número.


### ¿Por qué manejar excepciones?

* Evitar que el programa se detenga abruptamente
* Proporcionar mensajes útiles al usuario
* Recuperarse de situaciones inesperadas
* Hacer programas más robustos y profesionales

Note: Sin manejo de excepciones, cualquier error en tiempo de ejecución detiene el programa con un mensaje técnico confuso. Con manejo adecuado, podemos capturar el error, informar al usuario amablemente, y continuar la ejecución o terminar elegantemente.


### Tipos comunes de excepciones

* `ValueError`: Valor inapropiado
* `TypeError`: Tipo de dato incorrecto
* `ZeroDivisionError`: División por cero
* `FileNotFoundError`: Archivo no existe
* `IndexError`: Índice fuera de rango
* `KeyError`: Clave no existe en diccionario

Note: Python tiene docenas de excepciones predefinidas. Conocer las más comunes te ayuda a anticipar y manejar problemas típicos. Cada excepción tiene un nombre descriptivo que indica qué salió mal.

---

## Ejemplos sin Manejo


### Problema: Conversión de tipos

```python
velocidad = input('¿Velocidad de la golondrina? ')
# Usuario escribe: "una golondrina europea"
print(int(velocidad))

# Error:
# ValueError: invalid literal for int() with base 10: 
# 'una golondrina europea'
```

Note: Este es uno de los errores más comunes: intentar convertir texto no numérico a número. Sin manejo de excepciones, el programa termina inmediatamente mostrando un traceback confuso para el usuario.


### Problema: División por cero

```python
numerador = 10
denominador = 0
resultado = numerador / denominador

# Error:
# ZeroDivisionError: division by zero
```

Note: La división por cero es matemáticamente indefinida. Python lanza una excepción porque no puede calcular el resultado. Este error es común en cálculos que dependen de entrada del usuario o datos variables.


### Problema: Índice fuera de rango

```python
lista = [1, 2, 3, 4, 5]
elemento = lista[10]

# Error:
# IndexError: list index out of range
```

Note: Intentar acceder a un índice que no existe es otro error común, especialmente en bucles o al procesar datos dinámicos. Los índices válidos van de 0 a len(lista)-1.


### El traceback

```python
Traceback (most recent call last):
  File "programa.py", line 3, in <module>
    resultado = numerador / denominador
ZeroDivisionError: division by zero
```

* Muestra dónde ocurrió el error
* Tipo de excepción
* Mensaje descriptivo
* Pila de llamadas (call stack)

Note: El traceback es la información que Python muestra cuando hay una excepción no manejada. Es útil para programadores pero confusa para usuarios finales. Por eso debemos capturar y manejar las excepciones apropiadamente.

---

## Try-Except Básico


### Estructura try-except

* Bloque `try`: Código que puede fallar
* Bloque `except`: Código si hay excepción
* Si no hay excepción, except se salta
* Si hay excepción, se ejecuta except

```python
try:
    # Código que puede fallar
    resultado = operacion_arriesgada()
except:
    # Qué hacer si falla
    print('Algo salió mal')
```

Note: Try-except es como una "red de seguridad". Intentas ejecutar código arriesgado en el bloque try. Si algo falla, en lugar de detener el programa, Python ejecuta el bloque except.


### Ejemplo: Conversión segura

```python
entrada = input('Introduce temperatura Fahrenheit: ')

try:
    fahr = float(entrada)
    celsius = (fahr - 32.0) * 5.0 / 9.0
    print(f'{fahr}°F = {celsius:.1f}°C')
except:
    print('Por favor, introduce un número válido')
```

Note: Este código intenta convertir la entrada a número. Si el usuario introduce texto, en lugar de terminar con error, captura la excepción y muestra un mensaje amable. El programa continúa ejecutándose.


### Ejemplo: División segura

```python
try:
    numerador = float(input('Numerador: '))
    denominador = float(input('Denominador: '))
    resultado = numerador / denominador
    print(f'Resultado: {resultado}')
except:
    print('Error en el cálculo. Verifica los números.')
```

Note: Este código captura cualquier excepción: ValueError si introducen texto, ZeroDivisionError si el denominador es cero. El mensaje genérico funciona pero no es específico sobre qué salió mal.


### Problema con except genérico

* Captura TODAS las excepciones
* No sabes qué falló exactamente
* Puede ocultar errores inesperados
* Mejor capturar excepciones específicas

```python
# Evitar (demasiado genérico):
try:
    codigo_complejo()
except:
    print('Error')  # ¿Qué error?

# Mejor (específico):
try:
    codigo_complejo()
except ValueError:
    print('Error de valor')
```

Note: Un except sin especificar excepción captura TODO, incluso errores que no anticipabas. Esto puede ocultar bugs reales. Es mejor práctica capturar solo las excepciones específicas que esperas.

---

## Capturar Excepciones Específicas


### Especificar tipo de excepción

```python
try:
    numero = int(input('Introduce número: '))
    resultado = 100 / numero
except ValueError:
    print('Eso no es un número válido')
except ZeroDivisionError:
    print('No se puede dividir por cero')
```

Note: Podemos tener múltiples bloques except, cada uno manejando un tipo diferente de excepción. Esto nos permite dar mensajes específicos y apropiados para cada situación.


### Capturar múltiples excepciones

```python
# Forma 1: Bloques separados
try:
    operacion()
except ValueError:
    manejar_valor_invalido()
except TypeError:
    manejar_tipo_incorrecto()

# Forma 2: Mismo manejo para varias
try:
    operacion()
except (ValueError, TypeError):
    print('Error de valor o tipo')
```

Note: Si varias excepciones requieren el mismo manejo, puedes agruparlas en una tupla. Si cada una necesita manejo diferente, usa bloques except separados.


### Acceder al mensaje de excepción

```python
try:
    numero = int(input('Número: '))
    resultado = 100 / numero
except ValueError as e:
    print(f'Error de valor: {e}')
except ZeroDivisionError as e:
    print(f'Error de división: {e}')
```

Note: La cláusula 'as e' captura el objeto de excepción en la variable e. Esto te permite acceder al mensaje de error específico que Python generó, útil para logging o mensajes detallados.


### Ejemplo completo: Calculadora robusta

```python
def dividir():
    try:
        a = float(input('Primer número: '))
        b = float(input('Segundo número: '))
        resultado = a / b
        print(f'{a} / {b} = {resultado}')
    except ValueError:
        print('Por favor introduce números válidos')
    except ZeroDivisionError:
        print('El divisor no puede ser cero')

dividir()
```

Note: Esta función maneja dos casos de error comunes: entrada no numérica y división por cero. Para cada caso, proporciona un mensaje específico y útil. El programa no se detiene, simplemente informa del problema.


### Orden de los except

* Python evalúa except de arriba hacia abajo
* Usa el primer except que coincida
* Excepciones específicas primero
* Excepciones generales al final

```python
try:
    operacion()
except ValueError:      # Específica primero
    print('Error de valor')
except Exception:        # General al final
    print('Otro error')
```

Note: El orden importa porque Python usa el primer except que coincida. Si pones una excepción general primero, las específicas después nunca se ejecutarán. Siempre de más específico a más general.

---

## Cláusulas Else y Finally


### Cláusula else

* Se ejecuta si NO hubo excepción
* Va después de todos los except
* Código que solo debe correr si todo fue bien

```python
try:
    numero = int(input('Número: '))
except ValueError:
    print('Entrada inválida')
else:
    print(f'Procesando {numero}...')
    resultado = numero * 2
    print(f'Resultado: {resultado}')
```

Note: El else es útil para código que solo debe ejecutarse si el try tuvo éxito. Separa claramente el "código arriesgado" (try) del "código de éxito" (else). Es más claro que poner todo en el try.


### Cláusula finally

* Se ejecuta SIEMPRE
* Haya o no haya habido excepción
* Útil para limpieza (cerrar archivos, conexiones)
* Va al final de toda la estructura

```python
try:
    archivo = open('datos.txt', 'r')
    contenido = archivo.read()
    procesar(contenido)
except FileNotFoundError:
    print('Archivo no encontrado')
finally:
    archivo.close()  # Se ejecuta siempre
    print('Limpieza completada')
```

Note: Finally garantiza que cierto código se ejecute sin importar qué pase. Es crucial para liberar recursos como archivos, conexiones de red o bases de datos. Aunque haya error, el finally se ejecuta.


### Estructura completa try-except-else-finally

```python
try:
    resultado = operacion_arriesgada()
except ValueError:
    print('Error de valor')
except TypeError:
    print('Error de tipo')
else:
    print('Éxito!')
    usar(resultado)
finally:
    print('Limpieza')
```

Note: Esta es la estructura completa. En orden: try (intentar), except (si falla), else (si tiene éxito), finally (siempre). No necesitas usar todos en cada caso, solo los que necesites.


### Ejemplo: Lectura de archivo segura

```python
archivo = None
try:
    archivo = open('config.txt', 'r')
    configuracion = archivo.read()
    print(f'Configuración cargada: {configuracion}')
except FileNotFoundError:
    print('Archivo de configuración no encontrado')
    print('Usando configuración por defecto')
except PermissionError:
    print('Sin permiso para leer el archivo')
finally:
    if archivo is not None:
        archivo.close()
        print('Archivo cerrado')
```

Note: Este ejemplo muestra un patrón común: intentar abrir un archivo, manejar posibles errores específicos, y garantizar que el archivo se cierre pase lo que pase. El finally asegura que no dejamos archivos abiertos.


### Cuándo usar cada cláusula

* **try**: Siempre (código que puede fallar)
* **except**: Siempre (manejar errores específicos)
* **else**: Opcional (código de éxito)
* **finally**: Opcional (limpieza garantizada)

Note: Try-except es el mínimo. Else ayuda a organizar código de éxito separado del try. Finally es esencial cuando trabajas con recursos que deben liberarse (archivos, conexiones, locks).

---

## Lanzar Excepciones


### La sentencia raise

* Lanza una excepción manualmente
* Útil para validación de datos
* Indica condiciones de error en tus funciones

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError('No se puede dividir por cero')
    return a / b

try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(f'Error: {e}')
```

Note: Raise te permite lanzar excepciones desde tu propio código. Esto es útil para validar entradas o señalar condiciones de error en funciones. Haces que tu código sea más explícito sobre qué puede fallar.


### Validación con excepciones

```python
def calcular_edad(año_nacimiento):
    año_actual = 2024
    
    if año_nacimiento < 1900 or año_nacimiento > año_actual:
        raise ValueError('Año de nacimiento inválido')
    
    return año_actual - año_nacimiento

try:
    edad = calcular_edad(2050)
except ValueError as e:
    print(f'Error: {e}')
```

Note: Usar raise para validación hace tu código más robusto. En lugar de retornar valores especiales (-1, None) para indicar error, lanzas una excepción explícita que quien llama tu función debe manejar.


### Re-lanzar excepciones

```python
def procesar_archivo(nombre):
    try:
        with open(nombre) as f:
            return f.read()
    except FileNotFoundError:
        print(f'Advertencia: {nombre} no encontrado')
        raise  # Re-lanza la misma excepción

try:
    contenido = procesar_archivo('datos.txt')
except FileNotFoundError:
    print('Usando datos por defecto')
```

Note: A veces quieres loggear o procesar una excepción pero dejar que se propague. La palabra raise sola re-lanza la excepción actual sin modificarla. Útil para logging o acciones intermedias.


### Excepciones personalizadas

```python
class TemperaturaInvalidaError(Exception):
    """Excepción para temperaturas fuera de rango"""
    pass

def celsius_a_fahrenheit(celsius):
    if celsius < -273.15:
        raise TemperaturaInvalidaError(
            'Temperatura menor al cero absoluto'
        )
    return celsius * 9/5 + 32

try:
    temp = celsius_a_fahrenheit(-300)
except TemperaturaInvalidaError as e:
    print(f'Error: {e}')
```

Note: Puedes crear tus propias clases de excepción heredando de Exception. Esto hace tu código más expresivo y permite a los usuarios de tu código capturar específicamente tus errores personalizados.


### Cuándo lanzar excepciones

* Datos de entrada inválidos
* Estado inconsistente
* Recursos no disponibles
* Operaciones imposibles
* Precondiciones no cumplidas

Note: Lanza excepciones para condiciones excepcionales, no para flujo normal. Por ejemplo, lanza excepción si un archivo debe existir y no existe, pero no lances excepción porque llegaste al final de un archivo (eso es normal).

---

## Depuración con Excepciones


### Información del traceback

```python
import traceback

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('¡Error!')
    traceback.print_exc()
    # Muestra información detallada del error
```

Note: El módulo traceback te permite capturar y trabajar con información detallada del error. Útil para logging o mostrar información de depuración sin detener el programa.


### Logging de excepciones

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    resultado = operacion_compleja()
except Exception as e:
    logging.error(f'Error en operación: {e}')
    logging.exception('Detalles completos:')
    # logging.exception incluye el traceback
```

Note: En producción, es mejor loggear errores que imprimirlos. Logging.exception() automáticamente incluye el traceback completo, muy útil para depurar problemas en producción.


### Depurar excepciones inesperadas

```python
def operacion():
    try:
        # Código complejo
        resultado = proceso_complicado()
        return resultado
    except Exception as e:
        print(f'Tipo de excepción: {type(e).__name__}')
        print(f'Mensaje: {e}')
        print(f'Args: {e.args}')
        raise  # Re-lanza para ver traceback completo
```

Note: Cuando depuras, a veces capturas cualquier excepción solo para ver qué tipo es. Imprimes información útil y luego re-lanzas para no ocultar el problema. Útil durante desarrollo.


### Usar assert para depuración

```python
def calcular_promedio(numeros):
    assert len(numeros) > 0, "Lista no puede estar vacía"
    assert all(isinstance(n, (int, float)) for n in numeros), \
           "Todos los elementos deben ser números"
    
    return sum(numeros) / len(numeros)

# En producción: python -O programa.py
# (desactiva asserts para mejor rendimiento)
```

Note: Assert lanza AssertionError si la condición es falsa. Útil para verificar precondiciones durante desarrollo. En producción, los asserts pueden desactivarse con -O para mejor rendimiento, así que no los uses para validación crítica.

---

## Patrones Comunes


### Patrón: EAFP vs LBYL

```python
# LBYL (Look Before You Leap) - Verificar primero
if archivo_existe(nombre):
    archivo = abrir(nombre)
else:
    manejar_error()

# EAFP (Easier to Ask for Forgiveness than Permission)
# Pythónico - Intentar y manejar excepción
try:
    archivo = abrir(nombre)
except FileNotFoundError:
    manejar_error()
```

Note: Python favorece EAFP: intenta la operación y maneja la excepción si falla. Es más eficiente (una operación en lugar de dos) y evita condiciones de carrera. LBYL es más común en lenguajes como C.


### Patrón: Reintentar con límite

```python
max_intentos = 3
intento = 0

while intento < max_intentos:
    try:
        conexion = conectar_servidor()
        break  # Éxito, salir del bucle
    except ConexionError:
        intento += 1
        print(f'Intento {intento} fallido')
        if intento == max_intentos:
            print('No se pudo conectar')
            raise
```

Note: Común al trabajar con recursos externos (red, APIs). Intentas la operación, si falla, reintenta un número limitado de veces. Después del límite, dejas que la excepción se propague.


### Patrón: Valor por defecto

```python
def leer_configuracion(archivo):
    try:
        with open(archivo) as f:
            return json.load(f)
    except FileNotFoundError:
        return {'modo': 'default', 'debug': False}
    except json.JSONDecodeError:
        print('Archivo corrupto, usando defaults')
        return {'modo': 'default', 'debug': False}

config = leer_configuracion('config.json')
```

Note: Patrón común: intentar cargar configuración de archivo, si falla usar valores por defecto. Hace tu aplicación más robusta y fácil de usar (funciona aunque falte el archivo de configuración).


### Patrón: Validación de entrada del usuario

```python
def pedir_numero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            numero = float(input(mensaje))
            if minimo is not None and numero < minimo:
                print(f'Debe ser al menos {minimo}')
                continue
            if maximo is not None and numero > maximo:
                print(f'Debe ser máximo {maximo}')
                continue
            return numero
        except ValueError:
            print('Por favor introduce un número válido')

edad = pedir_numero('Edad: ', minimo=0, maximo=120)
```

Note: Este patrón combina bucle, try-except y validación. Sigue pidiendo entrada hasta que sea válida. Muy útil para interfaces de usuario en consola. Hace imposible continuar con datos inválidos.


### Patrón: Context manager (with)

```python
# Sin with - debes recordar cerrar
archivo = open('datos.txt')
try:
    contenido = archivo.read()
finally:
    archivo.close()

# Con with - cierre automático
with open('datos.txt') as archivo:
    contenido = archivo.read()
    # Archivo se cierra automáticamente al salir del with
```

Note: With es un context manager que garantiza limpieza automática. Funciona como try-finally pero más limpio. Se usa con archivos, conexiones de BD, locks, etc. Muy pythónico y previene fugas de recursos.

---

## Testing de Excepciones


### Verificar que se lanza excepción

```python
import pytest

def dividir(a, b):
    if b == 0:
        raise ValueError('Divisor no puede ser cero')
    return a / b

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
    
    # También puedes verificar el mensaje
    with pytest.raises(ValueError, match='Divisor'):
        dividir(10, 0)
```

Note: En testing, a veces necesitas verificar que tu código LANCE una excepción bajo ciertas condiciones. Pytest.raises captura la excepción esperada. Si no se lanza, el test falla.


### Ejemplo completo con test

```python
def fahrenheit_a_celsius(fahr):
    """Convierte Fahrenheit a Celsius"""
    if fahr < -459.67:  # Cero absoluto en Fahrenheit
        raise ValueError(
            f'Temperatura {fahr}°F es menor al cero absoluto'
        )
    return (fahr - 32.0) * 5.0 / 9.0

def test_conversion_normal():
    assert fahrenheit_a_celsius(32) == 0
    assert fahrenheit_a_celsius(212) == 100

def test_temperatura_invalida():
    with pytest.raises(ValueError):
        fahrenheit_a_celsius(-500)
```

Note: Los tests verifican tanto el comportamiento normal (conversión correcta) como el comportamiento de error (excepción cuando la entrada es inválida). Ambos son importantes para código robusto.

---

## Mejores Prácticas


### Captura solo excepciones esperadas

```python
# Mal: captura todo
try:
    operacion()
except:
    pass  # Oculta todos los errores

# Bien: captura específico
try:
    operacion()
except ValueError:
    manejar_valor_invalido()
except TypeError:
    manejar_tipo_incorrecto()
```

Note: Nunca uses except desnudo en producción. Captura solo las excepciones que esperas y sabes manejar. Dejar que excepciones inesperadas se propaguen es mejor que ocultarlas silenciosamente.


### No usar excepciones para flujo normal

```python
# Mal: excepción para flujo normal
def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return None

# Bien: verificación normal
def obtener_elemento(lista, indice):
    if 0 <= indice < len(lista):
        return lista[indice]
    return None
```

Note: Las excepciones son para situaciones excepcionales, no para control de flujo normal. Verificar condiciones es más eficiente y más claro que lanzar y capturar excepciones constantemente.


### Mensajes de error útiles

```python
# Mal: mensaje genérico
raise ValueError('Error')

# Bien: mensaje descriptivo
raise ValueError(
    f'Edad {edad} fuera de rango válido (0-120)'
)

# Mejor: incluye contexto
raise ValueError(
    f'Edad {edad} inválida para usuario {nombre}. '
    f'Debe estar entre 0 y 120'
)
```

Note: Los mensajes de error son para humanos que necesitan entender qué salió mal. Incluye valores relevantes, rangos esperados y contexto. Haz que sea fácil diagnosticar y corregir el problema.


### Documentar excepciones en funciones

```python
def procesar_archivo(ruta: str) -> dict:
    """
    Procesa archivo de configuración.
    
    Args:
        ruta: Ruta al archivo de configuración
        
    Returns:
        Diccionario con configuración
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        ValueError: Si el archivo está mal formateado
        PermissionError: Si no hay permiso de lectura
    """
    # Implementación...
```

Note: Documenta qué excepciones puede lanzar tu función. Esto ayuda a quienes usan tu código a saber qué excepciones deben manejar. Es parte de tu contrato con el usuario de la función.


### Limpiar recursos apropiadamente

```python
# Bien: usar with (preferido)
with open('archivo.txt') as f:
    procesar(f)

# También bien: try-finally explícito
f = open('archivo.txt')
try:
    procesar(f)
finally:
    f.close()

# Mal: sin garantía de cierre
f = open('archivo.txt')
procesar(f)
f.close()  # ¿Se ejecuta si procesar falla?
```

Note: Siempre asegura liberación de recursos. With es preferido (más limpio). Si no puedes usar with, usa try-finally. Nunca dejes recursos sin garantía de liberación.


### Logging vs Print para errores

```python
import logging

# Desarrollo: prints están bien
try:
    operacion()
except ValueError as e:
    print(f'Error: {e}')

# Producción: usa logging
try:
    operacion()
except ValueError as e:
    logging.error(f'Error en operación: {e}')
    logging.exception('Detalles completos')
```

Note: Prints son útiles durante desarrollo. En producción, usa logging: puedes controlar niveles, enviar a archivos, filtrar, etc. Logging.exception() incluye automáticamente el traceback completo.

---

## Ejemplos Completos


### Ejemplo 1: Calculadora robusta

```python
def calculadora():
    """Calculadora simple con manejo de errores"""
    while True:
        try:
            print('\n=== CALCULADORA ===')
            a = float(input('Primer número (o "q" para salir): '))
            operador = input('Operador (+, -, *, /): ')
            b = float(input('Segundo número: '))
            
            if operador == '+':
                resultado = a + b
            elif operador == '-':
                resultado = a - b
            elif operador == '*':
                resultado = a * b
            elif operador == '/':
                if b == 0:
                    raise ZeroDivisionError('No se puede dividir por cero')
                resultado = a / b
            else:
                print('Operador no válido')
                continue
                
            print(f'Resultado: {resultado}')
            
        except ValueError:
            if 'q' in str(e):
                print('¡Hasta luego!')
                break
            print('Por favor introduce números válidos')
        except ZeroDivisionError as e:
            print(f'Error: {e}')
        except KeyboardInterrupt:
            print('\n¡Hasta luego!')
            break

calculadora()
```

Note: Este ejemplo completo muestra: manejo de múltiples excepciones, validación de entrada, bucle interactivo, salida elegante. Es un patrón común en aplicaciones de consola.


### Ejemplo 2: Procesador de archivos

```python
import json
import logging

def procesar_datos(archivo_entrada, archivo_salida):
    """
    Procesa archivo JSON y guarda resultados.
    
    Raises:
        FileNotFoundError: Si archivo entrada no existe
        ValueError: Si JSON es inválido
        PermissionError: Sin permisos de escritura
    """
    datos_procesados = []
    
    try:
        # Leer archivo
        with open(archivo_entrada, 'r') as f:
            datos = json.load(f)
        
        # Procesar datos
        for item in datos:
            try:
                procesado = procesar_item(item)
                datos_procesados.append(procesado)
            except ValueError as e:
                logging.warning(f'Item inválido: {item}. Error: {e}')
                continue  # Continuar con siguiente item
        
        # Guardar resultados
        with open(archivo_salida, 'w') as f:
            json.dump(datos_procesados, f, indent=2)
        
        logging.info(f'Procesados {len(datos_procesados)} items')
        return len(datos_procesados)
        
    except FileNotFoundError:
        logging.error(f'Archivo {archivo_entrada} no encontrado')
        raise
    except json.JSONDecodeError as e:
        logging.error(f'JSON inválido: {e}')
        raise ValueError(f'Archivo {archivo_entrada} corrupto')
    except PermissionError:
        logging.error(f'Sin permiso para escribir {archivo_salida}')
        raise

def procesar_item(item):
    """Procesa un item individual"""
    if 'id' not in item:
        raise ValueError('Item sin id')
    if 'valor' not in item:
        raise ValueError('Item sin valor')
    return {
        'id': item['id'],
        'valor_procesado': item['valor'] * 2
    }

# Uso
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        total = procesar_datos('datos.json', 'resultados.json')
        print(f'Éxito: {total} items procesados')
    except Exception as e:
        print(f'Error fatal: {e}')
```

Note: Ejemplo realista de procesamiento de archivos. Muestra: manejo de archivos con context managers, logging apropiado, manejo de errores por item vs errores fatales, propagación selectiva de excepciones.

---

## Resumen


### Conceptos clave

* Try-except captura y maneja excepciones
* Excepciones específicas mejor que genéricas
* Else para código de éxito
* Finally para limpieza garantizada
* Raise para lanzar excepciones
* With para manejo automático de recursos

Note: El manejo de excepciones es fundamental para escribir código robusto y profesional. Estos conceptos te permiten anticipar, capturar y recuperarte de situaciones inesperadas.


### Cuándo usar excepciones

* ✅ Situaciones excepcionales e inesperadas
* ✅ Validación de entrada de usuario
* ✅ Operaciones con recursos externos
* ✅ Señalar errores en tus funciones
* ❌ Control de flujo normal
* ❌ Condiciones que puedes verificar fácilmente

Note: Las excepciones son para situaciones excepcionales. No las uses para control de flujo normal. Si puedes verificar una condición fácilmente (como len(lista) > 0), hazlo en lugar de capturar IndexError.


### Mejores prácticas recordadas

* Captura excepciones específicas, no genéricas
* Proporciona mensajes de error útiles
* Documenta qué excepciones lanza tu código
* Usa with para recursos que requieren limpieza
* Loggea errores en producción
* Prueba tanto éxito como fallos

Note: Estas prácticas harán tu código más robusto, mantenible y fácil de depurar. El manejo apropiado de excepciones es marca de código profesional.


### Próximos pasos

* Practicar con código real
* Aprender sobre context managers personalizados
* Estudiar jerarquía completa de excepciones
* Explorar decoradores para manejo de errores
* Leer código de proyectos establecidos

Note: El manejo de excepciones se vuelve natural con práctica. Lee código de librerías establecidas para ver cómo los profesionales manejan errores. Practica añadiendo manejo robusto a tu propio código.

---

## ¿Preguntas?

Note: El manejo de excepciones puede parecer complicado al principio, pero es una habilidad esencial. Asegúrate de que los estudiantes entiendan cuándo y cómo usar excepciones. Anima a que compartan situaciones donde han tenido errores y cómo podrían manejarlos mejor.
