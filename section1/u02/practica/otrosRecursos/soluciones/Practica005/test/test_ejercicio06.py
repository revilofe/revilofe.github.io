"""
Tests para el Ejercicio 6: Detector de Años Bisiestos

Para ejecutar: pytest test_ejercicio06.py -v

Autor: Eduardo Fdez
Fecha: 2025-10-25
"""

import pytest
from ejercicio06 import es_bisiesto


class TestEsBisiesto:
    
    def test_2024_es_bisiesto(self):
        """Test: 2024 es bisiesto (divisible por 4) - código 3"""
        bisiesto, codigo = es_bisiesto(2024)
        assert bisiesto == True
        assert codigo == 3
    
    def test_2023_no_es_bisiesto(self):
        """Test: 2023 no es bisiesto - código 4"""
        bisiesto, codigo = es_bisiesto(2023)
        assert bisiesto == False
        assert codigo == 4
    
    def test_2000_es_bisiesto(self):
        """Test: 2000 es bisiesto (divisible por 400) - código 1"""
        bisiesto, codigo = es_bisiesto(2000)
        assert bisiesto == True
        assert codigo == 1
    
    def test_1900_no_es_bisiesto(self):
        """Test: 1900 no es bisiesto (divisible por 100 pero no por 400) - código 2"""
        bisiesto, codigo = es_bisiesto(1900)
        assert bisiesto == False
        assert codigo == 2
    
    def test_2100_no_es_bisiesto(self):
        """Test: 2100 no es bisiesto (secular no bisiesto) - código 2"""
        bisiesto, codigo = es_bisiesto(2100)
        assert bisiesto == False
        assert codigo == 2
    
    def test_2400_es_bisiesto(self):
        """Test: 2400 es bisiesto (divisible por 400) - código 1"""
        bisiesto, codigo = es_bisiesto(2400)
        assert bisiesto == True
        assert codigo == 1
    
    def test_1600_es_bisiesto(self):
        """Test: 1600 es bisiesto - código 1"""
        bisiesto, codigo = es_bisiesto(1600)
        assert bisiesto == True
        assert codigo == 1
    
    def test_1700_no_es_bisiesto(self):
        """Test: 1700 no es bisiesto - código 2"""
        bisiesto, codigo = es_bisiesto(1700)
        assert bisiesto == False
        assert codigo == 2
    
    def test_1800_no_es_bisiesto(self):
        """Test: 1800 no es bisiesto - código 2"""
        bisiesto, codigo = es_bisiesto(1800)
        assert bisiesto == False
        assert codigo == 2
    
    def test_anio_fuera_de_rango_bajo(self):
        """Test: Año menor a 1582 debe estar fuera de rango - código 0"""
        bisiesto, codigo = es_bisiesto(1581)
        assert bisiesto == False
        assert codigo == 0
    
    def test_anio_fuera_de_rango_alto(self):
        """Test: Año mayor a 3000 debe estar fuera de rango - código 0"""
        bisiesto, codigo = es_bisiesto(3001)
        assert bisiesto == False
        assert codigo == 0
    
    def test_limite_inferior_valido(self):
        """Test: 1582 es un año válido (no debe ser código 0)"""
        bisiesto, codigo = es_bisiesto(1582)
        assert codigo != 0
    
    def test_limite_superior_valido(self):
        """Test: 3000 es un año válido (no debe ser código 0)"""
        bisiesto, codigo = es_bisiesto(3000)
        assert codigo != 0
    
    def test_codigos_validos(self):
        """Test: Verificar que los códigos están en rango 0-4"""
        anios = [1581, 2000, 1900, 2024, 2023, 3001]
        for anio in anios:
            _, codigo = es_bisiesto(anio)
            assert 0 <= codigo <= 4, f"Código {codigo} fuera de rango para año {anio}"
    
    def test_tipo_retorno(self):
        """Test: Verificar que devuelve tupla (bool, int)"""
        resultado = es_bisiesto(2024)
        assert isinstance(resultado, tuple)
        assert len(resultado) == 2
        assert isinstance(resultado[0], bool)
        assert isinstance(resultado[1], int)


@pytest.mark.parametrize("anio,esperado_bisiesto,esperado_codigo", [
    (2000, True, 1),   # Divisible por 400
    (2400, True, 1),   # Divisible por 400
    (1600, True, 1),   # Divisible por 400
    (1900, False, 2),  # Divisible por 100 pero no por 400
    (2100, False, 2),  # Divisible por 100 pero no por 400
    (1700, False, 2),  # Divisible por 100 pero no por 400
    (2024, True, 3),   # Divisible por 4 pero no por 100
    (2020, True, 3),   # Divisible por 4 pero no por 100
    (2016, True, 3),   # Divisible por 4 pero no por 100
    (2023, False, 4),  # No divisible por 4
    (2021, False, 4),  # No divisible por 4
    (2019, False, 4),  # No divisible por 4
    (1581, False, 0),  # Fuera de rango (bajo)
    (3001, False, 0),  # Fuera de rango (alto)
])
def test_bisiestos_con_codigos(anio, esperado_bisiesto, esperado_codigo):
    """Test parametrizado que verifica tanto el resultado como el código"""
    bisiesto, codigo = es_bisiesto(anio)
    assert bisiesto == esperado_bisiesto, f"Error en bisiesto para {anio}"
    assert codigo == esperado_codigo, f"Error en código para {anio}: esperado {esperado_codigo}, obtenido {codigo}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
