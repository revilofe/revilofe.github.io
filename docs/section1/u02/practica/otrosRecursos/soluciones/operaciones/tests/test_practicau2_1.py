import pytest

from src.practicau2_1_sol_basico.py import (
    comprobar_importe, comprobar_comando, procesar_compra, procesar_venta,
    mostrar_saldo, resetear_saldo, recuperar_comando_e_importe, mostrar_mensaje_error
)

@pytest.mark.parametrize(
    "valor, expected",
    [
        ("100", True),
        ("-50", True),
        ("10.50", True),
        ("10.5.0", False),
        ("abc", False),
        ("", False)
    ]
)
def test_comprobar_importe(valor, expected):
    """
    Prueba para la función comprobar_importe.
    """
    assert comprobar_importe(valor) == expected


@pytest.mark.parametrize(
    "comando, expected",
    [
        ("compra", True),
        ("venta", True),
        ("saldo", True),
        ("reset", True),
        ("fin", True),
        ("otro_comando", False)
    ]
)
def test_comprobar_comando(comando, expected):
    """
    Prueba para la función comprobar_comando.
    """
    assert comprobar_comando(comando) == expected


@pytest.mark.parametrize(
    "saldo, importe, expected",
    [
        (100.0, 50.0, 50.0),
        (200.0, 100.0, 100.0),
        (0.0, 50.0, -50.0),
    ]
)
def test_procesar_compra(saldo, importe, expected):
    """
    Prueba para la función procesar_compra.
    """
    assert procesar_compra(saldo, importe) == expected


@pytest.mark.parametrize(
    "saldo, importe, expected",
    [
        (100.0, 50.0, 150.0),
        (200.0, 100.0, 300.0),
        (0.0, 50.0, 50.0),
    ]
)
def test_procesar_venta(saldo, importe, expected):
    """
    Prueba para la función procesar_venta.
    """
    assert procesar_venta(saldo, importe) == expected


@pytest.mark.parametrize(
    "saldo, cont_compras, cont_ventas, expected_output",
    [
        (100.0, 1, 2, "Saldo actual = 100.00 (1 compras y 2 ventas)\n"),
        (-50.0, 0, 1, "Saldo actual = -50.00 (0 compras y 1 ventas)\n"),
        (0.0, 3, 4, "Saldo actual = 0.00 (3 compras y 4 ventas)\n"),
    ]
)
def test_mostrar_saldo(capsys, saldo, cont_compras, cont_ventas, expected_output):
    """
    Prueba para la función mostrar_saldo.
    """
    mostrar_saldo(saldo, cont_compras, cont_ventas)
    captured = capsys.readouterr()
    assert captured.out == expected_output


@pytest.mark.parametrize(
    "saldo, cont_compras, cont_ventas, expected_saldo, expected_compras, expected_ventas, expected_output",
    [
        (100.0, 1, 2, 0.0, 0, 0, "Saldo anterior = 100.00 (1 compras y 2 ventas)\n"),
        (200.0, 3, 4, 0.0, 0, 0, "Saldo anterior = 200.00 (3 compras y 4 ventas)\n"),
    ]
)
def test_resetear_saldo(capsys, saldo, cont_compras, cont_ventas, expected_saldo, expected_compras, expected_ventas, expected_output):
    """
    Prueba para la función resetear_saldo.
    """
    result_saldo, result_compras, result_ventas = resetear_saldo(saldo, cont_compras, cont_ventas)
    captured = capsys.readouterr()
    
    assert captured.out == expected_output
    assert result_saldo == expected_saldo
    assert result_compras == expected_compras
    assert result_ventas == expected_ventas


@pytest.mark.parametrize(
    "linea, expected_comando, expected_importe",
    [
        ("compra 100", "compra", "100"),
        ("venta 50.5", "venta", "50.5"),
        ("saldo", "saldo", None),
        ("reset", "reset", None),
        ("", None, None),
        ("compra", "compra", None)  # Cambiado None por 'compra'
    ]
)
def test_recuperar_comando_e_importe(linea, expected_comando, expected_importe):
    """
    Prueba para la función recuperar_comando_e_importe.
    """
    comando, importe = recuperar_comando_e_importe(linea)
    assert comando == expected_comando
    assert importe == expected_importe


def test_mostrar_mensaje_error(capsys):
    """
    Prueba para la función mostrar_mensaje_error.
    Verifica si el mensaje de error se muestra correctamente.
    """
    mostrar_mensaje_error()
    captured = capsys.readouterr()
    assert captured.out == "*ERROR* Entrada inválida\n"
