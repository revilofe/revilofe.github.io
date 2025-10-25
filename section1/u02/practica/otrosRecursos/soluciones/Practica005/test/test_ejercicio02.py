"""
Tests para el Ejercicio 2: Clasificador de Temperaturas

Este archivo contiene los tests unitarios que se ejecutarán automáticamente
para validar que la función clasificar_temperatura funciona correctamente.

Para ejecutar los tests:
    pytest test_ejercicio02.py -v

Autor: Eduardo Fdez
Fecha: 2025-10-25
"""

import pytest
from ejercicio02 import clasificar_temperatura


class TestClasificarTemperatura:
    """
    Clase que agrupa todos los tests para la función clasificar_temperatura.
    """
    
    def test_helada_negativa(self):
        """
        Test: Temperatura negativa debe clasificarse como Helada
        """
        clasificacion, es_extrema = clasificar_temperatura(-5.0)
        assert clasificacion == "Helada", "Temperatura -5°C debe ser Helada"
        assert es_extrema == False, "Temperatura -5°C NO es extrema"
    
    def test_helada_extrema(self):
        """
        Test: Temperatura muy negativa debe ser Helada y extrema
        """
        clasificacion, es_extrema = clasificar_temperatura(-15.0)
        assert clasificacion == "Helada", "Temperatura -15°C debe ser Helada"
        assert es_extrema == True, "Temperatura -15°C ES extrema"
    
    def test_frio_cero(self):
        """
        Test: Temperatura 0°C debe clasificarse como Frío
        """
        clasificacion, es_extrema = clasificar_temperatura(0.0)
        assert clasificacion == "Frío", "Temperatura 0°C debe ser Frío"
        assert es_extrema == False
    
    def test_frio_limite_superior(self):
        """
        Test: Temperatura 10°C debe clasificarse como Frío
        """
        clasificacion, es_extrema = clasificar_temperatura(10.0)
        assert clasificacion == "Frío", "Temperatura 10°C debe ser Frío"
        assert es_extrema == False
    
    def test_frio_medio(self):
        """
        Test: Temperatura 5°C debe clasificarse como Frío
        """
        clasificacion, es_extrema = clasificar_temperatura(5.0)
        assert clasificacion == "Frío"
        assert es_extrema == False
    
    def test_templado_limite_inferior(self):
        """
        Test: Temperatura 11°C debe clasificarse como Templado
        """
        clasificacion, es_extrema = clasificar_temperatura(11.0)
        assert clasificacion == "Templado", "Temperatura 11°C debe ser Templado"
        assert es_extrema == False
    
    def test_templado_medio(self):
        """
        Test: Temperatura 15°C debe clasificarse como Templado
        """
        clasificacion, es_extrema = clasificar_temperatura(15.0)
        assert clasificacion == "Templado"
        assert es_extrema == False
    
    def test_templado_limite_superior(self):
        """
        Test: Temperatura 20°C debe clasificarse como Templado
        """
        clasificacion, es_extrema = clasificar_temperatura(20.0)
        assert clasificacion == "Templado", "Temperatura 20°C debe ser Templado"
        assert es_extrema == False
    
    def test_calido_limite_inferior(self):
        """
        Test: Temperatura 21°C debe clasificarse como Cálido
        """
        clasificacion, es_extrema = clasificar_temperatura(21.0)
        assert clasificacion == "Cálido", "Temperatura 21°C debe ser Cálido"
        assert es_extrema == False
    
    def test_calido_medio(self):
        """
        Test: Temperatura 25°C debe clasificarse como Cálido
        """
        clasificacion, es_extrema = clasificar_temperatura(25.0)
        assert clasificacion == "Cálido"
        assert es_extrema == False
    
    def test_calido_limite_superior(self):
        """
        Test: Temperatura 30°C debe clasificarse como Cálido
        """
        clasificacion, es_extrema = clasificar_temperatura(30.0)
        assert clasificacion == "Cálido", "Temperatura 30°C debe ser Cálido"
        assert es_extrema == False
    
    def test_caluroso_normal(self):
        """
        Test: Temperatura 35°C debe clasificarse como Caluroso
        """
        clasificacion, es_extrema = clasificar_temperatura(35.0)
        assert clasificacion == "Caluroso", "Temperatura 35°C debe ser Caluroso"
        assert es_extrema == False, "Temperatura 35°C NO es extrema"
    
    def test_caluroso_extremo(self):
        """
        Test: Temperatura 45°C debe ser Caluroso y extrema
        """
        clasificacion, es_extrema = clasificar_temperatura(45.0)
        assert clasificacion == "Caluroso", "Temperatura 45°C debe ser Caluroso"
        assert es_extrema == True, "Temperatura 45°C ES extrema"
    
    def test_temperatura_extrema_fria_limite(self):
        """
        Test: Temperatura -10°C NO es extrema (límite)
        """
        clasificacion, es_extrema = clasificar_temperatura(-10.0)
        assert es_extrema == False, "Temperatura -10°C NO es extrema (límite)"
    
    def test_temperatura_extrema_fria(self):
        """
        Test: Temperatura -11°C ES extrema
        """
        clasificacion, es_extrema = clasificar_temperatura(-11.0)
        assert es_extrema == True, "Temperatura -11°C ES extrema"
    
    def test_temperatura_extrema_calida_limite(self):
        """
        Test: Temperatura 40°C NO es extrema (límite)
        """
        clasificacion, es_extrema = clasificar_temperatura(40.0)
        assert es_extrema == False, "Temperatura 40°C NO es extrema (límite)"
    
    def test_temperatura_extrema_calida(self):
        """
        Test: Temperatura 41°C ES extrema
        """
        clasificacion, es_extrema = clasificar_temperatura(41.0)
        assert es_extrema == True, "Temperatura 41°C ES extrema"
    
    def test_temperatura_invalida_muy_baja(self):
        """
        Test: Temperatura menor a -50°C debe ser Inválida
        """
        clasificacion, es_extrema = clasificar_temperatura(-51.0)
        assert clasificacion == "Inválida", "Temperatura -51°C debe ser Inválida"
        assert es_extrema == False
    
    def test_temperatura_invalida_muy_alta(self):
        """
        Test: Temperatura mayor a 60°C debe ser Inválida
        """
        clasificacion, es_extrema = clasificar_temperatura(61.0)
        assert clasificacion == "Inválida", "Temperatura 61°C debe ser Inválida"
        assert es_extrema == False
    
    def test_temperatura_limite_inferior_valido(self):
        """
        Test: Temperatura -50°C es válida (límite)
        """
        clasificacion, es_extrema = clasificar_temperatura(-50.0)
        assert clasificacion == "Helada", "Temperatura -50°C es válida"
        assert es_extrema == True, "Temperatura -50°C ES extrema"
    
    def test_temperatura_limite_superior_valido(self):
        """
        Test: Temperatura 60°C es válida (límite)
        """
        clasificacion, es_extrema = clasificar_temperatura(60.0)
        assert clasificacion == "Caluroso", "Temperatura 60°C es válida"
        assert es_extrema == True, "Temperatura 60°C ES extrema"
    
    def test_tipos_retorno(self):
        """
        Test: Verificar que se devuelve una tupla con string y bool
        """
        resultado = clasificar_temperatura(25.0)
        assert isinstance(resultado, tuple), "Debe devolver una tupla"
        assert len(resultado) == 2, "La tupla debe tener 2 elementos"
        assert isinstance(resultado[0], str), "El primer elemento debe ser string"
        assert isinstance(resultado[1], bool), "El segundo elemento debe ser bool"


class TestCasosLimite:
    """
    Tests para casos límite y bordes de rangos.
    """
    
    def test_transicion_helada_frio(self):
        """
        Test: Verificar la transición entre Helada y Frío
        """
        # -0.1 debe ser Helada
        clasificacion1, _ = clasificar_temperatura(-0.1)
        assert clasificacion1 == "Helada"
        
        # 0.0 debe ser Frío
        clasificacion2, _ = clasificar_temperatura(0.0)
        assert clasificacion2 == "Frío"
    
    def test_transicion_frio_templado(self):
        """
        Test: Verificar la transición entre Frío y Templado
        """
        clasificacion1, _ = clasificar_temperatura(10.0)
        assert clasificacion1 == "Frío"
        
        clasificacion2, _ = clasificar_temperatura(10.1)
        assert clasificacion2 == "Templado"
    
    def test_decimales_precision(self):
        """
        Test: Verificar que funciona con decimales
        """
        clasificacion, _ = clasificar_temperatura(15.7)
        assert clasificacion == "Templado"


# Tests parametrizados para mayor cobertura
@pytest.mark.parametrize("temperatura,clasificacion_esperada,extrema_esperada", [
    (-50, "Helada", True),
    (-25, "Helada", True),
    (-10, "Helada", False),
    (-5, "Helada", False),
    (0, "Frío", False),
    (5, "Frío", False),
    (10, "Frío", False),
    (15, "Templado", False),
    (20, "Templado", False),
    (25, "Cálido", False),
    (30, "Cálido", False),
    (35, "Caluroso", False),
    (40, "Caluroso", False),
    (45, "Caluroso", True),
    (60, "Caluroso", True),
])
def test_clasificaciones_parametrizadas(temperatura, clasificacion_esperada, extrema_esperada):
    """
    Test parametrizado que verifica múltiples temperaturas.
    """
    clasificacion, es_extrema = clasificar_temperatura(temperatura)
    assert clasificacion == clasificacion_esperada, f"Fallo en clasificación de {temperatura}°C"
    assert es_extrema == extrema_esperada, f"Fallo en detección de extrema para {temperatura}°C"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
