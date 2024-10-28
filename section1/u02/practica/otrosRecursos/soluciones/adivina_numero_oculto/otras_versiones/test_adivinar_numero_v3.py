import pytest

from src.adivinar_numero_v3 import *

###################################################################################################

@pytest.mark.parametrize(
    "numero, numero_oculto, frio, caliente, expected",
    [
        (50, 100, 30, 10, 0),
        (85, 100, 30, 10, 1),
        (99, 100, 30, 10, 2),
    ]
)
def test_evaluar_distancia(numero, numero_oculto, frio, caliente, expected):
    assert evaluar_diferencia(numero, numero_oculto, frio, caliente) == expected

###################################################################################################

@pytest.mark.parametrize(
    "numero, numero_oculto, intentos, frio, caliente, expected_output",
    [
        (50, 100, 5, 20, 10, "\n* FRÍO, FRÍO, el número oculto es MAYOR... ¡te quedan 5 intentos!\n\n"),
        (85, 100, 3, 20, 10, "\n* CALIENTE, CALIENTE, el número oculto es MAYOR... ¡te quedan 3 intentos!\n\n"),
        (98, 100, 2, 20, 10, "\n* TE QUEMAS, el número oculto es MAYOR... ¡te quedan 2 intentos!\n\n"),
        (150, 100, 1, 20, 10, "\n* FRÍO, FRÍO, el número oculto es MENOR... ¡te queda 1 intento!\n\n"),
    ]
)
def test_mostrar_pista(capsys, numero, numero_oculto, intentos, frio, caliente, expected_output):
    mostrar_pista(numero, numero_oculto, intentos, frio, caliente)
    captured = capsys.readouterr()
    assert captured.out == expected_output 

###################################################################################################

@pytest.mark.parametrize(
    "numero_oculto, total_intentos, frio, caliente, mock_inputs, expected_result, expected_intentos",
    [
        (100, 5, 20, 10, ['50', '75', '90', '100'], True, 4),  # Adivina en el 4º intento
        (100, 3, 20, 10, ['50', '75', '90'], False, 3),        # No adivina en los 3 intentos
        (100, 2, 20, 10, ['98', '100'], True, 2),              # Adivina en el último intento
        (100, 4, 20, 10, ['150', '140', '120', '100'], True, 4),  # Adivina en el 4º intento
    ]
)
def test_adivina_el_numero(monkeypatch, numero_oculto, total_intentos, frio, caliente, mock_inputs, expected_result, expected_intentos):
    # Simular las entradas del usuario
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))

    # Ejecutar la función y capturar el resultado
    result, intentos_realizados = adivina_el_numero(numero_oculto, total_intentos, frio, caliente)

    # Probar si el número fue adivinado correctamente
    assert result == expected_result
    # Probar si el número de intentos realizados es el esperado
    assert intentos_realizados == expected_intentos

###################################################################################################

@pytest.mark.parametrize(
    "valor, expected",
    [
        ("100", True),
        ("-50", True),
        ("abc", False),
        ("12.5", False),
        ("", False),
    ]
)
def test_comprobar_numero_entero(valor, expected):
    assert comprobar_numero_entero(valor) == expected

###################################################################################################

@pytest.mark.parametrize(
    "minimo, maximo",
    [
        (0, 100),
        (-100, 0),
        (50, 150),
    ]
)
def test_genera_numero_oculto(minimo, maximo):
    numero_oculto = genera_numero_oculto(minimo, maximo)
    assert minimo <= numero_oculto <= maximo

###################################################################################################

@pytest.mark.parametrize(
    "frio, caliente, expected",
    [
        (30, 10, True),
        (50, 25, True),
    ]
)
def test_configurar_pistas(frio, caliente, expected):
    result = frio > caliente
    assert result == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (['  10'], 10),            # Entrada válida con espacios
        (['-5'], -5),              # Número negativo válido
        (['0'], 0),                # Número cero
        (['abc', '10'], 10),       # Entrada no válida seguida de entrada válida
        (['', '100'], 100),        # Entrada vacía seguida de número válido
    ]
)
def test_pedir_numero_usuario(mock_inputs, expected, monkeypatch):
    # Simular múltiples entradas del usuario usando monkeypatch
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Llamar a la función y comparar el resultado con lo esperado
    assert pedir_numero_usuario("Introduce un número: ") == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (['0', '200'], (0, 200)),        # Rango válido con diferencia de 100
        (['100', '500'], (100, 500)),    # Otro rango válido
        (['50', '50', '50', '200'], (50, 200)),  # Caso inválido (misma entrada dos veces) seguido de entrada válida
        (['0', '50', '0', '150'], (0, 150)),     # Caso inválido (diferencia menor a 100) seguido de entrada válida
    ]
)
def test_configurar_rangos_numeros(mock_inputs, expected, monkeypatch):
    # Simular entradas para mínimo y máximo
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Probar si el rango es configurado correctamente
    assert configurar_rangos_numeros() == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_inputs, minimo, maximo, expected",
    [
        (['20', '10'], 0, 100, (20, 10)),    # Pistas válidas: frío > caliente y dentro del rango
        (['30', '15'], 1, 200, (30, 15)),  # Otro set válido dentro del rango
        (['10', '10', '25', '5'], 0, 100, (25, 5)),  # Caso inválido (frío y caliente iguales) seguido de entrada válida
        (['60', '70', '50', '10'], 0, 100, (50, 10)),  # Caso inválido (frío < caliente) seguido de entrada válida
    ]
)
def test_configurar_pistas(mock_inputs, minimo, maximo, expected, monkeypatch):
    # Simular entradas para frío y caliente
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Probar si las pistas son configuradas correctamente
    assert configurar_pistas(minimo, maximo) == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_input, expected",
    [
        (['5'], 5),    # Intentos válidos
        (['10'], 10),  # Otro valor válido
        (['-1', '7'], 7),    # Caso inválido (número negativo) seguido de entrada válida
        (['0', '20'], 20), # Caso inválido (entrada no numérica) seguido de entrada válida
    ]
)
def test_configurar_intentos(mock_input, expected, monkeypatch):
    # Simular la entrada para el número de intentos
    inputs_iter = iter(mock_input)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Probar si los intentos son configurados correctamente
    assert configurar_intentos() == expected

###################################################################################################

@pytest.mark.parametrize(
    "seccion, intentos, expected_output",
    [
        (1, 0, "--- BIENVENIDOS AL JUEGO DE ADIVINAR EL NÚMERO OCULTO ---\n\n\n"),
        (2, 0, "--- MENÚ DE ADIVINA EL NÚMERO OCULTO ---\n\n\n"),
        (3, 5, "--- ADIVINA EL NÚMERO OCULTO EN 5 INTENTOS ---\n\n\n"),
        (0, 0, "--- SECCIÓN NO DEFINIDA ---\n\n\n"),  # Sección no válida, debería usar el título por defecto
        (3, 0, "--- ADIVINA EL NÚMERO OCULTO EN {intentos} INTENTOS ---\n\n\n"),  # Sección con intentos en 0, no formatea
        (10, 0, "--- SECCIÓN NO DEFINIDA ---\n\n\n"), # Sección fuera de rango, debería usar el título por defecto
    ]
)
def test_mostrar_titulo(capsys, seccion, intentos, expected_output):
    # Ejecutar la función mostrar_titulo
    mostrar_titulo(seccion, intentos)
    
    # Capturar la salida impresa
    captured = capsys.readouterr()
    
    # Verificar que la salida sea la esperada
    assert captured.out == expected_output

###################################################################################################

@pytest.mark.parametrize(
    "opcion, expected",
    [
        (1, True),    # Opción válida
        (4, True),    # Opción válida
        (0, False),   # Opción inválida (menor a 1)
        (5, False),   # Opción inválida (mayor a 4)
    ]
)
def test_comprobar_opcion(opcion, expected):
    assert comprobar_opcion(opcion) == expected

###################################################################################################

@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (['0', '1'], 1),    # Entrada inválida seguida de entrada válida
        (['abc', '2'], 2),  # Entrada no numérica seguida de entrada válida
        (['4'], 4),         # Entrada válida en el primer intento
    ]
)
def test_elegir_opcion_menu(mock_inputs, expected, monkeypatch):
    # Simular las entradas del usuario
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Probar si la opción es configurada correctamente
    assert elegir_opcion_menu() == expected

###################################################################################################

def test_mostrar_menu(capsys):
    mostrar_menu()
    captured = capsys.readouterr()
    expected_output = "--- MENÚ DE ADIVINA EL NÚMERO OCULTO ---\n\n\n1. Jugar.\n2. Configurar.\n3. Mostrar configuración.\n4. Salir.\n\n"
    assert captured.out == expected_output

###################################################################################################

@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (['0', '200', '30', '10', '5'], (0, 200, 5, 30, 10)),  # Rango válido, pistas válidas, intentos válidos
        (['1', '500', '50', '20', '7'], (1, 500, 7, 50, 20)),  # Otro set válido
    ]
)
def test_configurar_juego(mock_inputs, expected, monkeypatch):
    # Simular entradas para rango, pistas e intentos
    inputs_iter = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iter))
    
    # Probar si el juego es configurado correctamente
    assert configurar_juego() == expected

