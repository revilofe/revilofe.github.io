"""
Tests para el Ejercicio 10: Calculadora de Estadísticas Básicas

Este archivo contiene los tests automáticos que se usarán para evaluar
la función calcular_promedio del ejercicio 10.
"""

import pytest
from ejercicio10 import calcular_promedio


def test_promedio_simple():
    """
    Test: Promedio de números simples
    """
    # Suma 100, cantidad 5 -> promedio 20
    assert calcular_promedio(100, 5) == 20.0
    
    # Suma 50, cantidad 10 -> promedio 5
    assert calcular_promedio(50, 10) == 5.0
    
    # Suma 30, cantidad 3 -> promedio 10
    assert calcular_promedio(30, 3) == 10.0


def test_promedio_decimal():
    """
    Test: Promedio que resulta en decimal
    """
    # Suma 10, cantidad 3 -> promedio 3.333...
    resultado = calcular_promedio(10, 3)
    assert abs(resultado - 3.333333) < 0.00001
    
    # Suma 7, cantidad 2 -> promedio 3.5
    assert calcular_promedio(7, 2) == 3.5
    
    # Suma 100, cantidad 3 -> promedio 33.333...
    resultado = calcular_promedio(100, 3)
    assert abs(resultado - 33.333333) < 0.00001


def test_un_solo_numero():
    """
    Test: Promedio de un solo número
    """
    # Suma 50, cantidad 1 -> promedio 50
    assert calcular_promedio(50, 1) == 50.0
    
    # Suma 1, cantidad 1 -> promedio 1
    assert calcular_promedio(1, 1) == 1.0
    
    # Suma 100, cantidad 1 -> promedio 100
    assert calcular_promedio(100, 1) == 100.0


def test_numeros_grandes():
    """
    Test: Promedio con números grandes
    """
    # Suma 10000, cantidad 100 -> promedio 100
    assert calcular_promedio(10000, 100) == 100.0
    
    # Suma 1000000, cantidad 1000 -> promedio 1000
    assert calcular_promedio(1000000, 1000) == 1000.0


def test_cantidad_invalida():
    """
    Test: Cantidad <= 0 debe devolver 0.0
    """
    assert calcular_promedio(100, 0) == 0.0
    assert calcular_promedio(50, -1) == 0.0
    assert calcular_promedio(200, -10) == 0.0


def test_suma_invalida():
    """
    Test: Suma < 0 debe devolver 0.0
    """
    assert calcular_promedio(-100, 5) == 0.0
    assert calcular_promedio(-50, 10) == 0.0
    assert calcular_promedio(-1, 1) == 0.0


def test_ambos_invalidos():
    """
    Test: Ambos parámetros inválidos
    """
    assert calcular_promedio(-100, 0) == 0.0
    assert calcular_promedio(-50, -5) == 0.0
    assert calcular_promedio(0, 0) == 0.0


def test_suma_cero_cantidad_valida():
    """
    Test: Suma 0 con cantidad válida (promedio 0)
    """
    # Si no se suman números (todos ceros), el promedio es 0
    assert calcular_promedio(0, 5) == 0.0
    assert calcular_promedio(0, 1) == 0.0
    assert calcular_promedio(0, 100) == 0.0


def test_promedios_exactos():
    """
    Test: Promedios que dan números exactos
    """
    # Suma 100, cantidad 4 -> promedio 25
    assert calcular_promedio(100, 4) == 25.0
    
    # Suma 200, cantidad 10 -> promedio 20
    assert calcular_promedio(200, 10) == 20.0
    
    # Suma 60, cantidad 12 -> promedio 5
    assert calcular_promedio(60, 12) == 5.0


def test_casos_ejemplo():
    """
    Test: Casos del ejemplo del enunciado
    """
    # Ejemplo: 10, 20, 15, 25, 30
    # Suma: 100, Cantidad: 5, Promedio: 20.0
    assert calcular_promedio(100, 5) == 20.0


def test_precision_float():
    """
    Test: Verificar que devuelve float con precisión adecuada
    """
    resultado = calcular_promedio(10, 3)
    assert isinstance(resultado, float)
    
    resultado = calcular_promedio(7, 2)
    assert isinstance(resultado, float)
    assert resultado == 3.5


def test_numeros_iguales():
    """
    Test: Todos los números son iguales
    """
    # Si todos son 5: suma 25, cantidad 5 -> promedio 5
    assert calcular_promedio(25, 5) == 5.0
    
    # Si todos son 10: suma 100, cantidad 10 -> promedio 10
    assert calcular_promedio(100, 10) == 10.0


def test_cantidad_grande():
    """
    Test: Cantidad muy grande de números
    """
    # Suma 5000, cantidad 1000 -> promedio 5
    assert calcular_promedio(5000, 1000) == 5.0
    
    # Suma 10000, cantidad 500 -> promedio 20
    assert calcular_promedio(10000, 500) == 20.0


def test_diferentes_combinaciones():
    """
    Test: Diferentes combinaciones de suma y cantidad
    """
    assert calcular_promedio(15, 5) == 3.0
    assert calcular_promedio(24, 4) == 6.0
    assert calcular_promedio(35, 7) == 5.0
    assert calcular_promedio(88, 8) == 11.0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
