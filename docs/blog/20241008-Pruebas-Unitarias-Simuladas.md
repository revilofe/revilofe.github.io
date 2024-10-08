---
title: Pruebas Unitarias con monkeypatch y capfd.

description: Pruebas Unitarias con monkeypatch y capfd.

authors:
    - Diego Cano.

date: 2024-10-08

tags:
  - monkeypatch
  - capfd
  - python
  - test
  - pytest
---
# Pruebas Unitarias con "monkeypatch" y "capfd"

## Pruebas con entradas simuladas ***(monkeypatch)***

Supongamos que tenemos la siguiente función:

```python
def introduce_entero(msj: str) -> int:
    while True:
        valor = input(msj).strip()
        if valor.isdigit() or (valor.startswith("-") and valor[1:].isdigit()):
            return int(valor)
        else:
            print(f"**ERROR** \'{valor}\' no es un número entero válido!")
```

Para poder probarla corectamente *de forma aislada*, la función input() que contiene debemos ***simularla***. Para ello, observa el siguiente ejemplo de prueba unitaria, dónde únicamente vamos a probar la función con entradas válidas:

```python
import pytest

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ('  10', 10),   # Número positivo válido
        ('-5', -5),     # Número negativo válido
        ('0', 0),       # Número cero
    ]
)
def test_introduce_entero_valid(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert introduce_entero("Introduce un entero: ") == expected
```

### Explicación detallada:

#### 1. **`@pytest.mark.parametrize(...)`**:
   - Esta línea de código es un **decorador** que le dice a **pytest** que la misma prueba se debe ejecutar varias veces, cambiando los valores de entrada y salida esperados para cada prueba.
   - **`mock_input`**: Simula lo que el usuario introduciría en el teclado (por ejemplo, `'10'` o `'-5'`).
   - **`expected`**: Es el valor esperado que debería devolver la función después de convertir la entrada en un número entero.
   - El decorador ejecutará la prueba para cada uno de los casos:
     - **('  10', 10)**: Esperamos que el valor de entrada `'  10'` se convierta en `10`.
     - **('-5', -5)**: Esperamos que el valor de entrada `'-5'` se convierta en `-5`.
     - **('0', 0)**: El valor `'0'` debe devolver el número `0`.

#### 2. **La función de prueba `test_introduce_entero_valid(...)`**:
   ```python
   def test_introduce_entero_valid(mock_input, expected, monkeypatch):
   ```

   - **`mock_input`**: Este valor es la entrada simulada (lo que el usuario "introduce").
   - **`expected`**: Es el valor que esperamos obtener al final.
   - **`monkeypatch`**: Este parámetro es una herramienta que nos permite simular el comportamiento de la función **`input()`** para que, durante la prueba, no tengamos que escribir nada en el teclado. 

#### 3. **`monkeypatch.setattr('builtins.input', lambda _: mock_input)`**:
   - Aquí, estamos usando **`monkeypatch`** para reemplazar la función **`input()`** por una versión que siempre devuelve el valor **`mock_input`**. Esto es como si estuviéramos "engañando" a la función para que piense que el usuario ha introducido un valor específico.
   - **`lambda _: mock_input`**: Es una función anónima que siempre devuelve **`mock_input`**, ignorando cualquier parámetro (el mensaje que mostraría el **`input()`**).

#### 4. **`assert introduce_entero(...) == expected`**:
   - Esta línea ejecuta la función **`introduce_entero()`** con los parámetros de prueba, y después compara el resultado devuelto por la función con el valor **`expected`**.
   - Si la función devuelve un valor distinto al esperado, la prueba fallará.

### Ejecución del test:
Cada vez que pytest ejecuta este test, usa uno de los conjuntos de parámetros definidos en **`@pytest.mark.parametrize`**. Por ejemplo:
1. Cuando la entrada simulada es `'  10'`, la función **`introduce_entero`** debería devolver `10`, y la prueba comprobará si ese es el caso.
2. Si la función devuelve algo diferente a lo esperado (por ejemplo, si la función falla y devuelve `'10'` en lugar de `10`), entonces la prueba fallará.

### Consideraciones:
- **`isdigit()`** en **`introduce_entero()`** se asegura de que solo se consideren cadenas que representan enteros positivos. Para los números negativos, la función también verifica si la cadena comienza con un `-` y el resto de la cadena es un número.
- **`strip()`** elimina los espacios adicionales alrededor del número introducido, lo cual garantiza que el valor se procese correctamente incluso si el usuario introduce espacios accidentales.

## Pruebas con capturas de mensajes de error ***(monkeypatch y capfd)***

Ahora vamos a realizar un **test para simular una entrada inválida en la función `introduce_entero`**, capturando y comprobando el mensaje de error en la salida de la consola.

Vamos a construir el código del test y la explicación detallada para entender cómo realizar este tipo de pruebas.

### Test para `introduce_entero` con entrada inválida y captura del error:

```python
import pytest

@pytest.mark.parametrize(
    "mock_inputs, error_msg",
    [
        (['abc'], "**ERROR** 'abc' no es un número entero válido!\n"),  # Entrada inválida sin valor válido posterior
        (['123abc'], "**ERROR** '123abc' no es un número entero válido!\n"),  # Entrada con mezcla de caracteres
        (['-123a'], "**ERROR** '-123a' no es un número entero válido!\n"),  # Entrada con número negativo y caracteres inválidos
    ]
)
def test_introduce_entero_invalid_only(mock_inputs, error_msg, monkeypatch, capfd):
    input_iterator = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Usamos pytest.raises para manejar el agotamiento del iterador
    with pytest.raises(StopIteration):
        introduce_entero("Introduce un entero: ")  # Esto seguirá esperando una entrada válida

    # Capturamos el mensaje de salida y verificamos si se imprimió el mensaje de error
    captured = capfd.readouterr()
    assert error_msg in captured.out
```

### Explicación detallada:

#### 1. **`@pytest.mark.parametrize(...)`**:
   - **`@pytest.mark.parametrize`**: Le indica a **pytest** que debe ejecutar la prueba varias veces con diferentes combinaciones de entradas y mensajes de error.
   - **`mock_inputs`**: Simula lo que el usuario introduciría (por ejemplo, `'abc'` o `'-123a'`), que en este caso son entradas inválidas.
   - **`error_msg`**: El mensaje de error esperado que debería imprimirse cuando se detecte una entrada inválida.
   - Cada uno de estos casos simula una entrada incorrecta:
     - **`['abc']`**: Entrada completamente no numérica.
     - **`['123abc']`**: Entrada con una mezcla de números y caracteres no válidos.
     - **`['-123a']`**: Un número negativo con caracteres adicionales no válidos.

#### 2. **La función de prueba `test_introduce_entero_invalid_only(...)`**:
   ```python
   def test_introduce_entero_invalid_only(mock_inputs, error_msg, monkeypatch, capfd):
   ```

   - **`mock_inputs`**: Es una lista de entradas simuladas (cada una en su propio caso de prueba).
   - **`error_msg`**: Es el mensaje que esperamos que aparezca en la consola cuando el usuario introduce un valor no válido.
   - **`monkeypatch`**: Simula las entradas que el usuario introduciría, reemplazando la llamada a **`input()`**.
   - **`capfd`**: Captura la salida estándar (lo que se imprime en la consola), para verificar que se está mostrando el mensaje de error correcto.

#### 3. **`monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))`**:
   - Estamos usando **`monkeypatch`** para interceptar la función **`input()`** y devolver la entrada simulada de **`mock_inputs`** usando un iterador.
   - **`lambda _: next(input_iterator)`**: Simula el comportamiento de **`input()`**, devolviendo un valor de la lista **`mock_inputs`** cada vez que se llama.

#### 4. **Manejo del agotamiento del iterador con `pytest.raises(StopIteration)`**:
   - Este bloque permite que el test se maneje correctamente cuando el iterador se queda sin entradas simuladas.
   - Como estamos simulando entradas inválidas, la función **`introduce_entero`** quedaría atrapada en un bucle infinito esperando una entrada válida. Para manejar esto, usamos **`pytest.raises(StopIteration)`** para finalizar la prueba cuando el iterador se queda sin entradas.

#### 5. **Captura del mensaje de salida con `capfd.readouterr()`**:
   - **`capfd.readouterr()`**: Captura todo lo que se ha imprimido en la consola durante la ejecución de la prueba. Esto nos permite verificar que el mensaje de error que imprimió la función es exactamente el que esperamos.
   - **`assert error_msg in captured.out`**: Aquí verificamos que el mensaje de error esperado se encuentra en la salida capturada.

### Ejecución del test:
1. **Simulación de entradas inválidas**: En cada ejecución del test, se simula una entrada no válida como `'abc'` o `'123abc'`.
2. **Verificación de errores**: La función **`introduce_entero`** debería imprimir el mensaje de error esperado, como **`"**ERROR** 'abc' no es un número entero válido!"**.
3. **Agotamiento del iterador**: Cuando el iterador de entradas se queda sin valores, **`pytest.raises(StopIteration)`** finaliza el test.

### Conclusión:
Este test ayuda a comprobar que la función **`introduce_entero`** detecta correctamente las entradas no válidas, imprime el mensaje de error adecuado y maneja de manera adecuada la espera de entradas válidas, incluso cuando solo se simulan entradas incorrectas.
