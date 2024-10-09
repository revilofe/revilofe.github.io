
import pytest
from otros.conversiones_numericas import introduce_base, introduce_numero

#
# Pruebas para la función introduce_base()
#

@pytest.mark.parametrize(
    "mock_input, permitir_entrada_vacia, expected",
    [
        ('10', False, 10),  # Base decimal
        ('  10 ', False, 10),  # Base decimal
        ('2', False, 2),    # Base binaria
        (' 8 ', False, 8),    # Base octal
        ('16      ', False, 16),  # Base hexadecimal
        ('', True, None)   # Entrada vacía permitida
    ]
)
def test_introduce_base_valid(mock_input, permitir_entrada_vacia, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert introduce_base("Introduce una base: ", permitir_entrada_vacia) == expected


@pytest.mark.parametrize(
    "mock_inputs, expected",
    [
        (['5', '2'], 2),  # Entrada inválida primero, luego válida (no se comprueba mensaje de error)
        (['9', '16  '], 16), # Entrada inválida primero, luego válida hexadecimal (no se comprueba mensaje de error)
        (['-', '  8  '], 8) # Entrada inválida primero, luego válida octal (no se comprueba mensaje de error)
    ]
)
def test_introduce_base_invalid_and_valid(mock_inputs, expected, monkeypatch):
    input_iterator = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    assert introduce_base("Introduce una base: ") == expected


@pytest.mark.parametrize(
    "mock_inputs, error_msg",
    [
        (['  ', '  10'], "**ERROR** no ha introducido una base correcta!\n"),  # Base '  ' no es válida, después la base 10 si
        (['0', '8'], "**ERROR** no ha introducido una base correcta!\n"), # Base 0 no es válida, después la base 8 si
        (['', '         10'], "**ERROR** no ha introducido una base correcta!\n") # Base '' no es válida, después la base 10 si
    ]
)
def test_introduce_base_invalid_with_error(mock_inputs, error_msg, monkeypatch, capfd):
    input_iterator = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    introduce_base("Introduce una base: ")  # Este continuará hasta que haya una entrada válida

    # Capturar la salida estándar y comprobar el mensaje de error
    captured = capfd.readouterr()
    assert error_msg in captured.out


@pytest.mark.parametrize(
    "mock_inputs, error_msg",
    [
        ([''], "**ERROR** no ha introducido una base correcta!\n"),  # Base vacía no válida
        (['hola'], "**ERROR** no ha introducido una base correcta!\n"),  # Base hola no válida
        (['999'], "**ERROR** no ha introducido una base correcta!\n")  # Base hola no válida
    ]
)
def test_introduce_base_invalid_only(mock_inputs, error_msg, monkeypatch, capfd):
    input_iterator = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Manejar el agotamiento del iterador para forzar la salida del test
    with pytest.raises(StopIteration):
        introduce_base("Introduce una base: ")  # Esto seguirá esperando una entrada válida

    # Capturar la salida estándar y verificar si se imprimió el mensaje de error
    captured = capfd.readouterr()
    assert error_msg in captured.out


#
# Pruebas para la función introduce_numero()
#

@pytest.mark.parametrize(
    "mock_input, base, expected",
    [
        ('  101 ', 2, '101'),     # Binario
        ('  -111 ', 2, '-111'),     # Binario
        ('377   ', 8, '377'),     # Octal
        ('     1234', 10, '1234'),  # Decimal
        ('1A3F', 16, '1A3F'),   # Hexadecimal
        ('-ABC  ', 16, '-ABC')   # Hexadecimal
    ]
)
def test_introduce_numero_valid(mock_input, base, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert introduce_numero("Introduce un número: ", base) == expected


@pytest.mark.parametrize(
    "mock_inputs, base, expected",
    [
        (['ABC ', ' 101  '], 2, '101'),   # Primero entrada inválida (ABC), luego válida (101)
        (['  -  ', '  1A3F'], 16, '1A3F'), # Primero entrada inválida (-), luego válida hexadecimal (1A3F)
        (['FF', '156'], 10, '156') # Primero entrada inválida (FF), luego válida decimal (156)
    ]
)
def test_introduce_numero_invalid_and_valid(mock_inputs, base, expected, monkeypatch):
    input_iterator = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))
    assert introduce_numero("Introduce un número: ", base) == expected

@pytest.mark.parametrize(
    "mock_inputs, base, error_msg",
    [
        (['101A', '101'], 2, "**ERROR** el número '101A' no es válido para la base binaria!\n"),  # Entrada inválida primero, luego válida
        (['89', '77'], 8, "**ERROR** el número '89' no es válido para la base octal!\n"),  # Entrada inválida primero, luego válida
        (['', '558'], 10, "**ERROR** el número '' no es válido para la base decimal!\n")  # Entrada inválida primero, luego válida
    ]
)
def test_introduce_numero_invalid_with_error(mock_inputs, base, error_msg, monkeypatch, capfd):
    input_iterator = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Simulamos el flujo completo hasta obtener una entrada válida
    introduce_numero("Introduce un número: ", base)

    # Capturar la salida estándar y verificar si se imprimió el mensaje de error
    captured = capfd.readouterr()
    assert error_msg in captured.out


@pytest.mark.parametrize(
    "mock_inputs, base, error_msg",
    [
        (['ABC'], 2, "**ERROR** el número 'ABC' no es válido para la base binaria!\n"),  # Entrada inválida sin valor válido posterior
        (['123G'], 16, "**ERROR** el número '123G' no es válido para la base hexadecimal!\n")  # Entrada inválida sin valor válido posterior
    ]
)
def test_introduce_numero_invalid_only(mock_inputs, base, error_msg, monkeypatch, capfd):
    input_iterator = iter(mock_inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Manejar el agotamiento del iterador para forzar la salida del test
    with pytest.raises(StopIteration):
        introduce_numero("Introduce un número: ", base)

    # Capturar la salida estándar y verificar si se imprimió el mensaje de error
    captured = capfd.readouterr()
    assert error_msg in captured.out

