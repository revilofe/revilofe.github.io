"""
Tests para el Ejercicio 5: Conversor de Tiempo

Para ejecutar: pytest test_ejercicio05.py -v

Autor: Eduardo Fdez
Fecha: 2025-10-25
"""

import pytest
from ejercicio05 import convertir_segundos


class TestConvertirSegundos:
    
    def test_ejemplo_enunciado(self):
        """Test: 100000 segundos = 1 día, 3 horas, 46 minutos, 40 segundos"""
        dias, horas, minutos, segundos = convertir_segundos(100000)
        assert dias == 1
        assert horas == 3
        assert minutos == 46
        assert segundos == 40
    
    def test_cero_segundos(self):
        """Test: 0 segundos debe devolver todo en 0"""
        dias, horas, minutos, segundos = convertir_segundos(0)
        assert dias == 0
        assert horas == 0
        assert minutos == 0
        assert segundos == 0
    
    def test_solo_segundos(self):
        """Test: Menos de 60 segundos"""
        dias, horas, minutos, segundos = convertir_segundos(45)
        assert dias == 0
        assert horas == 0
        assert minutos == 0
        assert segundos == 45
    
    def test_solo_minutos(self):
        """Test: Múltiplo exacto de 60"""
        dias, horas, minutos, segundos = convertir_segundos(180)  # 3 minutos
        assert dias == 0
        assert horas == 0
        assert minutos == 3
        assert segundos == 0
    
    def test_solo_horas(self):
        """Test: Múltiplo exacto de 3600"""
        dias, horas, minutos, segundos = convertir_segundos(7200)  # 2 horas
        assert dias == 0
        assert horas == 2
        assert minutos == 0
        assert segundos == 0
    
    def test_solo_dias(self):
        """Test: Múltiplo exacto de 86400"""
        dias, horas, minutos, segundos = convertir_segundos(172800)  # 2 días
        assert dias == 2
        assert horas == 0
        assert minutos == 0
        assert segundos == 0
    
    def test_un_dia_exacto(self):
        """Test: Exactamente 1 día"""
        dias, horas, minutos, segundos = convertir_segundos(86400)
        assert dias == 1
        assert horas == 0
        assert minutos == 0
        assert segundos == 0
    
    def test_una_hora_exacta(self):
        """Test: Exactamente 1 hora"""
        dias, horas, minutos, segundos = convertir_segundos(3600)
        assert dias == 0
        assert horas == 1
        assert minutos == 0
        assert segundos == 0
    
    def test_un_minuto_exacto(self):
        """Test: Exactamente 1 minuto"""
        dias, horas, minutos, segundos = convertir_segundos(60)
        assert dias == 0
        assert horas == 0
        assert minutos == 1
        assert segundos == 0
    
    def test_combinacion_completa(self):
        """Test: Todos los componentes presentes"""
        # 2 días + 5 horas + 30 minutos + 15 segundos
        total = 2*86400 + 5*3600 + 30*60 + 15
        dias, horas, minutos, segundos = convertir_segundos(total)
        assert dias == 2
        assert horas == 5
        assert minutos == 30
        assert segundos == 15
    
    def test_numero_negativo(self):
        """Test: Número negativo debe devolver (0,0,0,0)"""
        dias, horas, minutos, segundos = convertir_segundos(-100)
        assert dias == 0
        assert horas == 0
        assert minutos == 0
        assert segundos == 0
    
    def test_23_horas_59_minutos_59_segundos(self):
        """Test: Casi un día completo"""
        total = 23*3600 + 59*60 + 59
        dias, horas, minutos, segundos = convertir_segundos(total)
        assert dias == 0
        assert horas == 23
        assert minutos == 59
        assert segundos == 59
    
    def test_semana_completa(self):
        """Test: 7 días exactos"""
        dias, horas, minutos, segundos = convertir_segundos(604800)  # 7*86400
        assert dias == 7
        assert horas == 0
        assert minutos == 0
        assert segundos == 0
    
    def test_tipo_retorno(self):
        """Test: Verificar que devuelve tupla de 4 enteros"""
        resultado = convertir_segundos(12345)
        assert isinstance(resultado, tuple)
        assert len(resultado) == 4
        assert all(isinstance(x, int) for x in resultado)


@pytest.mark.parametrize("segundos,dias_esp,horas_esp,min_esp,seg_esp", [
    (0, 0, 0, 0, 0),
    (1, 0, 0, 0, 1),
    (59, 0, 0, 0, 59),
    (60, 0, 0, 1, 0),
    (61, 0, 0, 1, 1),
    (3600, 0, 1, 0, 0),
    (3661, 0, 1, 1, 1),
    (86400, 1, 0, 0, 0),
    (90061, 1, 1, 1, 1),
    (100000, 1, 3, 46, 40),
])
def test_conversiones_parametrizadas(segundos, dias_esp, horas_esp, min_esp, seg_esp):
    """Test parametrizado para múltiples conversiones"""
    dias, horas, minutos, segundos_result = convertir_segundos(segundos)
    assert dias == dias_esp
    assert horas == horas_esp
    assert minutos == min_esp
    assert segundos_result == seg_esp


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
