"""
Tests para el Ejercicio 3: Contador de Dígitos Pares e Impares

Este archivo contiene los tests unitarios que se ejecutarán automáticamente
para validar que la función contar_digitos_pares_impares funciona correctamente.

Para ejecutar los tests:
    pytest test_ejercicio03.py -v

Autor: Eduardo Fdez
Fecha: 2025-10-25
"""

import pytest
from ejercicio03 import contar_digitos_pares_impares


class TestContarDigitosParesImpares:
    """
    Clase que agrupa todos los tests para la función contar_digitos_pares_impares.
    """
    
    def test_numero_cero(self):
        """
        Test: El número 0 debe tener 1 dígito par y 0 impares
        """
        pares, impares = contar_digitos_pares_impares(0)
        assert pares == 1, "El número 0 debe tener 1 dígito par"
        assert impares == 0, "El número 0 debe tener 0 dígitos impares"
    
    def test_numero_todos_pares(self):
        """
        Test: Número con solo dígitos pares
        """
        pares, impares = contar_digitos_pares_impares(2468)
        assert pares == 4, "2468 debe tener 4 dígitos pares"
        assert impares == 0, "2468 no debe tener dígitos impares"
    
    def test_numero_todos_impares(self):
        """
        Test: Número con solo dígitos impares
        """
        pares, impares = contar_digitos_pares_impares(1357)
        assert pares == 0, "1357 no debe tener dígitos pares"
        assert impares == 4, "1357 debe tener 4 dígitos impares"
    
    def test_numero_mixto_ejemplo(self):
        """
        Test: Número mixto del ejemplo (1234567890)
        """
        pares, impares = contar_digitos_pares_impares(1234567890)
        assert pares == 5, "1234567890 debe tener 5 dígitos pares (0,2,4,6,8)"
        assert impares == 5, "1234567890 debe tener 5 dígitos impares (1,3,5,7,9)"
    
    def test_numero_un_digito_par(self):
        """
        Test: Número de un solo dígito par
        """
        pares, impares = contar_digitos_pares_impares(8)
        assert pares == 1
        assert impares == 0
    
    def test_numero_un_digito_impar(self):
        """
        Test: Número de un solo dígito impar
        """
        pares, impares = contar_digitos_pares_impares(7)
        assert pares == 0
        assert impares == 1
    
    def test_numero_negativo_mixto(self):
        """
        Test: Número negativo debe trabajar con su valor absoluto
        """
        pares, impares = contar_digitos_pares_impares(-1234)
        assert pares == 2, "-1234 debe contar como 1234: 2 pares (2,4)"
        assert impares == 2, "-1234 debe contar como 1234: 2 impares (1,3)"
    
    def test_numero_negativo_todos_pares(self):
        """
        Test: Número negativo con solo dígitos pares
        """
        pares, impares = contar_digitos_pares_impares(-2468)
        assert pares == 4
        assert impares == 0
    
    def test_numero_con_ceros(self):
        """
        Test: Número que contiene ceros
        """
        pares, impares = contar_digitos_pares_impares(1020304)
        # 1, 0, 2, 0, 3, 0, 4 = 5 pares (0,0,0,2,4) y 2 impares (1,3)
        assert pares == 5, "1020304 tiene 5 pares (0,0,0,2,4)"
        assert impares == 2, "1020304 tiene 2 impares (1,3)"
    
    def test_numero_grande(self):
        """
        Test: Número grande
        """
        pares, impares = contar_digitos_pares_impares(123456789)
        assert pares == 4, "123456789 tiene 4 pares (2,4,6,8)"
        assert impares == 5, "123456789 tiene 5 impares (1,3,5,7,9)"
    
    def test_numero_repetidos_pares(self):
        """
        Test: Número con dígitos pares repetidos
        """
        pares, impares = contar_digitos_pares_impares(2222)
        assert pares == 4
        assert impares == 0
    
    def test_numero_repetidos_impares(self):
        """
        Test: Número con dígitos impares repetidos
        """
        pares, impares = contar_digitos_pares_impares(5555)
        assert pares == 0
        assert impares == 4
    
    def test_tipos_retorno(self):
        """
        Test: Verificar que se devuelve una tupla de dos enteros
        """
        resultado = contar_digitos_pares_impares(123)
        assert isinstance(resultado, tuple), "Debe devolver una tupla"
        assert len(resultado) == 2, "La tupla debe tener 2 elementos"
        assert isinstance(resultado[0], int), "El primer elemento debe ser int"
        assert isinstance(resultado[1], int), "El segundo elemento debe ser int"


class TestCasosEspeciales:
    """
    Tests para casos especiales y límites.
    """
    
    def test_numero_10(self):
        """
        Test: El número 10 tiene 1 par (0) y 1 impar (1)
        """
        pares, impares = contar_digitos_pares_impares(10)
        assert pares == 1
        assert impares == 1
    
    def test_numero_100(self):
        """
        Test: El número 100 tiene 2 pares (0,0) y 1 impar (1)
        """
        pares, impares = contar_digitos_pares_impares(100)
        assert pares == 2
        assert impares == 1
    
    def test_alternancia(self):
        """
        Test: Número con alternancia de pares e impares
        """
        pares, impares = contar_digitos_pares_impares(121212)
        assert pares == 3, "121212 tiene 3 pares (2,2,2)"
        assert impares == 3, "121212 tiene 3 impares (1,1,1)"
    
    def test_empieza_con_cero_imposible(self):
        """
        Test: Números que empiezan con 0 (como 012) no existen como int,
        pero podemos probar 102 que tiene un 0 en medio
        """
        pares, impares = contar_digitos_pares_impares(102)
        assert pares == 2, "102 tiene 2 pares (0,2)"
        assert impares == 1, "102 tiene 1 impar (1)"


# Tests parametrizados para mayor cobertura
@pytest.mark.parametrize("numero,pares_esperados,impares_esperados", [
    (0, 1, 0),
    (1, 0, 1),
    (2, 1, 0),
    (12, 1, 1),
    (123, 1, 2),
    (1234, 2, 2),
    (12345, 2, 3),
    (123456, 3, 3),
    (1234567, 3, 4),
    (12345678, 4, 4),
    (123456789, 4, 5),
    (1234567890, 5, 5),
    (-123, 1, 2),
    (-2468, 4, 0),
    (-1357, 0, 4),
    (2000, 4, 0),
    (1111, 0, 4),
    (2222, 4, 0),
])
def test_conteo_parametrizado(numero, pares_esperados, impares_esperados):
    """
    Test parametrizado que verifica múltiples números.
    """
    pares, impares = contar_digitos_pares_impares(numero)
    assert pares == pares_esperados, f"Error en cantidad de pares para {numero}"
    assert impares == impares_esperados, f"Error en cantidad de impares para {numero}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
