"""
Tests para el Ejercicio 1: Calculadora de Propinas

Este archivo contiene los tests unitarios que se ejecutarán automáticamente
para validar que la función calcular_propina funciona correctamente.

Para ejecutar los tests:
    pytest test_ejercicio01.py -v

Autor: Eduardo Fdez
Fecha: 2025-10-25
"""

import pytest
from ejercicio01 import calcular_propina


class TestCalcularPropina:
    """
    Clase que agrupa todos los tests para la función calcular_propina.
    """
    
    def test_servicio_excelente_importe_50(self):
        """
        Test: Servicio excelente (20%) con importe de 50€
        Esperado: propina 10€, total 60€
        """
        propina, total = calcular_propina(50.0, "excelente")
        assert propina == 10.0, "La propina para servicio excelente de 50€ debe ser 10€"
        assert total == 60.0, "El total para servicio excelente de 50€ debe ser 60€"
    
    def test_servicio_bueno_importe_47_50(self):
        """
        Test: Servicio bueno (15%) con importe de 47.50€
        Esperado: propina 7.125€, total 54.625€
        """
        propina, total = calcular_propina(47.50, "bueno")
        assert abs(propina - 7.125) < 0.01, "La propina para servicio bueno de 47.50€ debe ser aprox 7.12€"
        assert abs(total - 54.625) < 0.01, "El total para servicio bueno de 47.50€ debe ser aprox 54.62€"
    
    def test_servicio_regular_importe_100(self):
        """
        Test: Servicio regular (10%) con importe de 100€
        Esperado: propina 10€, total 110€
        """
        propina, total = calcular_propina(100.0, "regular")
        assert propina == 10.0, "La propina para servicio regular de 100€ debe ser 10€"
        assert total == 110.0, "El total para servicio regular de 100€ debe ser 110€"
    
    def test_servicio_excelente_mayusculas(self):
        """
        Test: Calidad "EXCELENTE" en mayúsculas debe funcionar
        """
        propina, total = calcular_propina(50.0, "EXCELENTE")
        assert propina == 10.0, "Debe aceptar 'EXCELENTE' en mayúsculas"
        assert total == 60.0
    
    def test_servicio_bueno_mixtas(self):
        """
        Test: Calidad "BuEnO" en mayúsculas/minúsculas mezcladas debe funcionar
        """
        propina, total = calcular_propina(50.0, "BuEnO")
        assert propina == 7.5, "Debe aceptar 'BuEnO' con mayúsculas/minúsculas mezcladas"
        assert total == 57.5
    
    def test_importe_cero(self):
        """
        Test: Importe de 0€ debe devolver propina 0 y total 0
        """
        propina, total = calcular_propina(0.0, "excelente")
        assert propina == 0.0, "Con importe 0, la propina debe ser 0"
        assert total == 0.0, "Con importe 0, el total debe ser 0"
    
    def test_importe_negativo(self):
        """
        Test: Importe negativo debe devolver propina 0 y total 0
        """
        propina, total = calcular_propina(-10.0, "bueno")
        assert propina == 0.0, "Con importe negativo, la propina debe ser 0"
        assert total == 0.0, "Con importe negativo, el total debe ser 0"
    
    def test_calidad_invalida(self):
        """
        Test: Calidad no válida debe devolver propina 0 y total = importe
        """
        propina, total = calcular_propina(50.0, "malo")
        assert propina == 0.0, "Con calidad inválida, la propina debe ser 0"
        assert total == 50.0, "Con calidad inválida, el total debe ser el importe original"
    
    def test_calidad_vacia(self):
        """
        Test: Calidad vacía debe devolver propina 0 y total = importe
        """
        propina, total = calcular_propina(30.0, "")
        assert propina == 0.0, "Con calidad vacía, la propina debe ser 0"
        assert total == 30.0, "Con calidad vacía, el total debe ser el importe original"
    
    def test_servicio_excelente_decimal_pequeno(self):
        """
        Test: Servicio excelente con importe decimal pequeño
        """
        propina, total = calcular_propina(5.75, "excelente")
        assert abs(propina - 1.15) < 0.01, "Propina de 5.75€ al 20% debe ser 1.15€"
        assert abs(total - 6.90) < 0.01, "Total debe ser 6.90€"
    
    def test_servicio_regular_importe_grande(self):
        """
        Test: Servicio regular con importe grande
        """
        propina, total = calcular_propina(1250.0, "regular")
        assert propina == 125.0, "Propina de 1250€ al 10% debe ser 125€"
        assert total == 1375.0, "Total debe ser 1375€"
    
    def test_tipos_retorno(self):
        """
        Test: Verificar que se devuelve una tupla de dos elementos
        """
        resultado = calcular_propina(50.0, "bueno")
        assert isinstance(resultado, tuple), "Debe devolver una tupla"
        assert len(resultado) == 2, "La tupla debe tener exactamente 2 elementos"
        assert isinstance(resultado[0], float), "El primer elemento debe ser float"
        assert isinstance(resultado[1], float), "El segundo elemento debe ser float"


class TestCasosEspeciales:
    """
    Tests para casos especiales y límites.
    """
    
    def test_importe_muy_pequeno(self):
        """
        Test: Importe muy pequeño (0.01€)
        """
        propina, total = calcular_propina(0.01, "excelente")
        assert propina > 0, "Debe calcular propina incluso para importes muy pequeños"
        assert total > 0.01, "El total debe ser mayor que el importe"
    
    def test_precision_decimales(self):
        """
        Test: Verificar que los cálculos mantienen precisión decimal razonable
        """
        propina, total = calcular_propina(33.33, "bueno")
        # 33.33 * 0.15 = 4.9995, redondeado a 5.00
        assert abs(propina - 4.9995) < 0.01, "Debe mantener precisión decimal"
        assert abs(total - 38.3295) < 0.01, "Debe mantener precisión en el total"
    
    def test_espacios_en_calidad(self):
        """
        Test: Calidad con espacios al inicio/final
        Nota: Este test fallará si no se hace strip() en la función
        """
        # Este test documenta el comportamiento esperado
        # Si quieres que funcione con espacios, debes hacer .strip() en la función
        propina, total = calcular_propina(50.0, " bueno ")
        # Por ahora, este test fallará intencionalmente para mostrar que 
        # no se maneja este caso. Los alumnos pueden mejorarlo.
        assert propina == 0.0, "Sin .strip(), los espacios hacen que la calidad sea inválida"


# Tests parametrizados para cubrir múltiples casos de forma eficiente
@pytest.mark.parametrize("importe,calidad,propina_esperada,total_esperado", [
    (100.0, "excelente", 20.0, 120.0),
    (100.0, "bueno", 15.0, 115.0),
    (100.0, "regular", 10.0, 110.0),
    (200.0, "excelente", 40.0, 240.0),
    (50.0, "bueno", 7.5, 57.5),
    (25.0, "regular", 2.5, 27.5),
])
def test_calculos_multiples(importe, calidad, propina_esperada, total_esperado):
    """
    Test parametrizado que prueba múltiples combinaciones de importe/calidad.
    """
    propina, total = calcular_propina(importe, calidad)
    assert abs(propina - propina_esperada) < 0.01, f"Propina incorrecta para {importe}€ y calidad '{calidad}'"
    assert abs(total - total_esperado) < 0.01, f"Total incorrecto para {importe}€ y calidad '{calidad}'"


if __name__ == "__main__":
    # Ejecutar tests si se ejecuta este archivo directamente
    pytest.main([__file__, "-v"])
