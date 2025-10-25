"""
Tests para el Ejercicio 8: Validador de Contraseñas Seguras

Este archivo contiene los tests automáticos que se usarán para evaluar
la función validar_contrasena del ejercicio 8.
"""

import pytest
from ejercicio08 import validar_contrasena


def test_contrasena_vacia():
    """
    Test: Contraseña vacía
    """
    assert validar_contrasena("") == (False, 0, 0, 0, 0, 0)


def test_contrasena_valida_simple():
    """
    Test: Contraseña que cumple todos los requisitos
    """
    assert validar_contrasena("Abc123!@") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("MiPass123!") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("Segur1dad!") == (True, 1, 1, 1, 1, 1)


def test_contrasena_solo_longitud_insuficiente():
    """
    Test: Contraseña que solo falla en longitud (< 8)
    """
    assert validar_contrasena("Abc12!") == (False, 0, 1, 1, 1, 1)


def test_contrasena_sin_mayusculas():
    """
    Test: Contraseña sin mayúsculas
    """
    assert validar_contrasena("abcdef123!") == (False, 1, 0, 1, 1, 1)


def test_contrasena_sin_minusculas():
    """
    Test: Contraseña sin minúsculas
    """
    assert validar_contrasena("ABCDEF123!") == (False, 1, 1, 0, 1, 1)


def test_contrasena_sin_digitos():
    """
    Test: Contraseña sin dígitos
    """
    assert validar_contrasena("Abcdefgh!") == (False, 1, 1, 1, 0, 1)


def test_contrasena_sin_especiales():
    """
    Test: Contraseña sin caracteres especiales
    """
    assert validar_contrasena("Abcdef123") == (False, 1, 1, 1, 1, 0)


def test_contrasena_combinacion_fallos():
    """
    Test: Contraseñas con múltiples requisitos faltantes
    """
    # "abc" - corta, sin mayúsculas, sin números, sin especiales
    assert validar_contrasena("abc") == (False, 0, 0, 1, 0, 0)
    
    # "ABCDEFGH" - sin minúsculas, sin números, sin especiales
    assert validar_contrasena("ABCDEFGH") == (False, 1, 1, 0, 0, 0)
    
    # "Ab12" - corta, sin especiales
    assert validar_contrasena("Ab12") == (False, 0, 1, 1, 1, 0)


def test_contrasena_limite_longitud():
    """
    Test: Contraseñas en el límite de longitud (7 y 8 caracteres)
    """
    # 7 caracteres - falta longitud
    assert validar_contrasena("Abc12!#") == (False, 0, 1, 1, 1, 1)
    
    # 8 caracteres exactos - válida
    assert validar_contrasena("Abc123!@") == (True, 1, 1, 1, 1, 1)


def test_contrasena_todos_especiales_validos():
    """
    Test: Verificar que todos los caracteres especiales válidos funcionan
    """
    assert validar_contrasena("Abcdef12!") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("Abcdef12@") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("Abcdef12#") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("Abcdef12$") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("Abcdef12%") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("Abcdef12&") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("Abcdef12*") == (True, 1, 1, 1, 1, 1)


def test_contrasena_caracteres_especiales_invalidos():
    """
    Test: Caracteres que no son especiales válidos
    """
    assert validar_contrasena("Abcdef123.") == (False, 1, 1, 1, 1, 0)
    assert validar_contrasena("Abcdef123-") == (False, 1, 1, 1, 1, 0)
    assert validar_contrasena("Abcdef123_") == (False, 1, 1, 1, 1, 0)


def test_contrasena_solo_numeros_y_letras():
    """
    Test: Contraseña con solo letras y números (sin especiales)
    """
    assert validar_contrasena("Abcdefgh1234") == (False, 1, 1, 1, 1, 0)


def test_contrasena_muy_larga_valida():
    """
    Test: Contraseña muy larga que cumple todos los requisitos
    """
    # Nota: La ñ no es considerada en los rangos A-Z, a-z
    assert validar_contrasena("MiContraseSuperSegura123!@#$%") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg123!") == (True, 1, 1, 1, 1, 1)


def test_contrasena_casos_reales():
    """
    Test: Casos de contraseñas reales típicas
    """
    # Débiles
    result1 = validar_contrasena("password")
    assert result1[0] == False  # Debe fallar
    
    result2 = validar_contrasena("12345678")
    assert result2[0] == False  # Debe fallar
    
    result3 = validar_contrasena("qwerty")
    assert result3[0] == False  # Debe fallar
    
    # Fuertes
    assert validar_contrasena("P@ssw0rd!") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("MyP@ss123") == (True, 1, 1, 1, 1, 1)
    assert validar_contrasena("Secur3*Pass") == (True, 1, 1, 1, 1, 1)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
