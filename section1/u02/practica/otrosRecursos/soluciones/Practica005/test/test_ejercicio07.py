"""
Tests para el Ejercicio 7: Calculadora de Descuentos Progresivos

Para ejecutar: pytest test_ejercicio07.py -v

Autor: Eduardo Fdez
Fecha: 2025-10-25
"""

import pytest
from ejercicio07 import calcular_precio_final


class TestCalcularPrecioFinal:
    
    def test_sin_descuento_no_premium(self):
        """Test: Compra < 100€ sin descuento, no premium"""
        desc_vol, desc_prem, final = calcular_precio_final(50.0, False)
        assert desc_vol == 0.0
        assert desc_prem == 0.0
        assert final == 50.0
    
    def test_descuento_10_no_premium(self):
        """Test: Compra entre 100-200€, descuento 10%, no premium"""
        desc_vol, desc_prem, final = calcular_precio_final(150.0, False)
        assert desc_vol == 15.0  # 10% de 150
        assert desc_prem == 0.0
        assert final == 135.0
    
    def test_descuento_15_no_premium(self):
        """Test: Compra entre 200-500€, descuento 15%, no premium"""
        desc_vol, desc_prem, final = calcular_precio_final(300.0, False)
        assert desc_vol == 45.0  # 15% de 300
        assert desc_prem == 0.0
        assert final == 255.0
    
    def test_descuento_20_no_premium(self):
        """Test: Compra > 500€, descuento 20%, no premium"""
        desc_vol, desc_prem, final = calcular_precio_final(600.0, False)
        assert desc_vol == 120.0  # 20% de 600
        assert desc_prem == 0.0
        assert final == 480.0
    
    def test_sin_descuento_premium(self):
        """Test: Compra < 100€, cliente premium"""
        desc_vol, desc_prem, final = calcular_precio_final(50.0, True)
        assert desc_vol == 0.0
        assert desc_prem == 2.5  # 5% de 50
        assert final == 47.5
    
    def test_descuento_10_premium(self):
        """Test: Compra 100-200€, descuento 10% + premium"""
        desc_vol, desc_prem, final = calcular_precio_final(150.0, True)
        assert desc_vol == 15.0  # 10% de 150
        assert desc_prem == 6.75  # 5% de 135
        assert abs(final - 128.25) < 0.01
    
    def test_descuento_15_premium(self):
        """Test: Compra 200-500€, descuento 15% + premium"""
        desc_vol, desc_prem, final = calcular_precio_final(300.0, True)
        assert desc_vol == 45.0  # 15% de 300
        assert desc_prem == 12.75  # 5% de 255
        assert abs(final - 242.25) < 0.01
    
    def test_descuento_20_premium(self):
        """Test: Compra > 500€, descuento 20% + premium"""
        desc_vol, desc_prem, final = calcular_precio_final(600.0, True)
        assert desc_vol == 120.0  # 20% de 600
        assert desc_prem == 24.0  # 5% de 480
        assert final == 456.0
    
    def test_ejemplo_enunciado(self):
        """Test: Caso del enunciado (250€, premium)"""
        desc_vol, desc_prem, final = calcular_precio_final(250.0, True)
        assert desc_vol == 37.5  # 15% de 250
        assert abs(desc_prem - 10.625) < 0.01  # 5% de 212.5
        assert abs(final - 201.875) < 0.01
    
    def test_limite_100_exacto(self):
        """Test: Exactamente 100€ debe tener 10% descuento"""
        desc_vol, desc_prem, final = calcular_precio_final(100.0, False)
        assert desc_vol == 10.0
        assert desc_prem == 0.0
        assert final == 90.0
    
    def test_limite_200_exacto(self):
        """Test: Exactamente 200€ debe tener 15% descuento"""
        desc_vol, desc_prem, final = calcular_precio_final(200.0, False)
        assert desc_vol == 30.0
        assert desc_prem == 0.0
        assert final == 170.0
    
    def test_limite_500_exacto(self):
        """Test: Exactamente 500€ debe tener 20% descuento"""
        desc_vol, desc_prem, final = calcular_precio_final(500.0, False)
        assert desc_vol == 100.0
        assert desc_prem == 0.0
        assert final == 400.0
    
    def test_99_euros_sin_descuento(self):
        """Test: 99€ no debe tener descuento por volumen"""
        desc_vol, desc_prem, final = calcular_precio_final(99.0, False)
        assert desc_vol == 0.0
    
    def test_101_euros_con_descuento(self):
        """Test: 101€ debe tener descuento del 10%"""
        desc_vol, desc_prem, final = calcular_precio_final(101.0, False)
        assert abs(desc_vol - 10.1) < 0.001  # Tolerancia para floats
    
    def test_importe_cero(self):
        """Test: Importe 0 debe devolver (0, 0, 0)"""
        desc_vol, desc_prem, final = calcular_precio_final(0.0, False)
        assert desc_vol == 0.0
        assert desc_prem == 0.0
        assert final == 0.0
    
    def test_importe_negativo(self):
        """Test: Importe negativo debe devolver (0, 0, 0)"""
        desc_vol, desc_prem, final = calcular_precio_final(-50.0, False)
        assert desc_vol == 0.0
        assert desc_prem == 0.0
        assert final == 0.0
    
    def test_compra_muy_grande(self):
        """Test: Compra de 10000€"""
        desc_vol, desc_prem, final = calcular_precio_final(10000.0, True)
        assert desc_vol == 2000.0  # 20% de 10000
        assert desc_prem == 400.0   # 5% de 8000
        assert final == 7600.0
    
    def test_tipo_retorno(self):
        """Test: Verificar que devuelve tupla de 3 floats"""
        resultado = calcular_precio_final(100.0, False)
        assert isinstance(resultado, tuple)
        assert len(resultado) == 3
        assert all(isinstance(x, float) for x in resultado)


@pytest.mark.parametrize("importe,premium,desc_vol_esp,desc_prem_esp,final_esp", [
    (50.0, False, 0.0, 0.0, 50.0),
    (50.0, True, 0.0, 2.5, 47.5),
    (100.0, False, 10.0, 0.0, 90.0),
    (100.0, True, 10.0, 4.5, 85.5),
    (200.0, False, 30.0, 0.0, 170.0),
    (200.0, True, 30.0, 8.5, 161.5),
    (500.0, False, 100.0, 0.0, 400.0),
    (500.0, True, 100.0, 20.0, 380.0),
    (1000.0, False, 200.0, 0.0, 800.0),
    (1000.0, True, 200.0, 40.0, 760.0),
])
def test_calculos_parametrizados(importe, premium, desc_vol_esp, desc_prem_esp, final_esp):
    """Test parametrizado para múltiples casos"""
    desc_vol, desc_prem, final = calcular_precio_final(importe, premium)
    assert abs(desc_vol - desc_vol_esp) < 0.01, f"Error en desc_vol para {importe}"
    assert abs(desc_prem - desc_prem_esp) < 0.01, f"Error en desc_prem para {importe}"
    assert abs(final - final_esp) < 0.01, f"Error en final para {importe}"


@pytest.mark.parametrize("importe,premium", [
    (99.99, False),
    (100.01, False),
    (199.99, False),
    (200.01, False),
    (499.99, False),
    (500.01, False),
    (99.99, True),
    (100.01, True),
])
def test_limites_rangos(importe, premium):
    """Test para verificar límites de rangos"""
    desc_vol, desc_prem, final = calcular_precio_final(importe, premium)
    
    # Verificar que la suma es correcta
    ahorro_total = desc_vol + desc_prem
    assert abs((importe - ahorro_total) - final) < 0.01
    
    # Verificar que final es positivo
    assert final >= 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
