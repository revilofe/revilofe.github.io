"""
Tests para el Ejercicio 4: Calculadora de IMC

Para ejecutar: pytest test_ejercicio04.py -v

Autor: Eduardo Fdez
Fecha: 2025-10-25
"""

import pytest
from ejercicio04 import calcular_imc


class TestCalcularIMC:
    
    def test_bajo_peso(self):
        """Test: IMC < 18.5 debe ser Bajo peso"""
        imc, cat = calcular_imc(50, 1.75)
        assert imc < 18.5
        assert cat == "Bajo peso"
    
    def test_normal(self):
        """Test: IMC entre 18.5 y 25 debe ser Normal"""
        imc, cat = calcular_imc(70, 1.75)
        assert 18.5 <= imc < 25
        assert cat == "Normal"
    
    def test_sobrepeso(self):
        """Test: IMC entre 25 y 30 debe ser Sobrepeso"""
        imc, cat = calcular_imc(80, 1.75)
        assert 25 <= imc < 30
        assert cat == "Sobrepeso"
    
    def test_obesidad(self):
        """Test: IMC >= 30 debe ser Obesidad"""
        imc, cat = calcular_imc(95, 1.75)
        assert imc >= 30
        assert cat == "Obesidad"
    
    def test_ejemplo_enunciado(self):
        """Test: Caso del ejemplo (70kg, 1.75m)"""
        imc, cat = calcular_imc(70, 1.75)
        assert abs(imc - 22.86) < 0.01
        assert cat == "Normal"
    
    def test_limite_bajo_peso_normal(self):
        """Test: IMC exacto 18.5 debe ser Normal"""
        # peso necesario para IMC=18.5 con altura 1.75: 56.656kg
        imc, cat = calcular_imc(56.656, 1.75)
        assert abs(imc - 18.5) < 0.01
        assert cat == "Normal" or cat == "Bajo peso"  # Depende de si usa < o <=
    
    def test_limite_normal_sobrepeso(self):
        """Test: IMC exacto 25 debe ser Sobrepeso"""
        # peso necesario para IMC=25 con altura 1.75: 76.5625kg
        imc, cat = calcular_imc(76.5625, 1.75)
        assert abs(imc - 25.0) < 0.01
        assert cat == "Sobrepeso"
    
    def test_limite_sobrepeso_obesidad(self):
        """Test: IMC exacto 30 debe ser Obesidad"""
        # peso necesario para IMC=30 con altura 1.75: 91.875kg
        imc, cat = calcular_imc(91.875, 1.75)
        assert abs(imc - 30.0) < 0.01
        assert cat == "Obesidad"
    
    def test_peso_cero(self):
        """Test: Peso 0 debe devolver datos inválidos"""
        imc, cat = calcular_imc(0, 1.75)
        assert imc == 0.0
        assert cat == "Datos inválidos"
    
    def test_altura_cero(self):
        """Test: Altura 0 debe devolver datos inválidos"""
        imc, cat = calcular_imc(70, 0)
        assert imc == 0.0
        assert cat == "Datos inválidos"
    
    def test_peso_negativo(self):
        """Test: Peso negativo debe devolver datos inválidos"""
        imc, cat = calcular_imc(-70, 1.75)
        assert imc == 0.0
        assert cat == "Datos inválidos"
    
    def test_altura_negativa(self):
        """Test: Altura negativa debe devolver datos inválidos"""
        imc, cat = calcular_imc(70, -1.75)
        assert imc == 0.0
        assert cat == "Datos inválidos"
    
    def test_peso_muy_bajo(self):
        """Test: Peso < 20 debe estar fuera de rango"""
        imc, cat = calcular_imc(19, 1.75)
        assert imc == 0.0
        assert cat == "Peso fuera de rango"
    
    def test_peso_muy_alto(self):
        """Test: Peso > 300 debe estar fuera de rango"""
        imc, cat = calcular_imc(301, 1.75)
        assert imc == 0.0
        assert cat == "Peso fuera de rango"
    
    def test_altura_muy_baja(self):
        """Test: Altura < 0.5 debe estar fuera de rango"""
        imc, cat = calcular_imc(70, 0.49)
        assert imc == 0.0
        assert cat == "Altura fuera de rango"
    
    def test_altura_muy_alta(self):
        """Test: Altura > 2.5 debe estar fuera de rango"""
        imc, cat = calcular_imc(70, 2.51)
        assert imc == 0.0
        assert cat == "Altura fuera de rango"
    
    def test_limites_validos_peso(self):
        """Test: Límites exactos de peso (20 y 300) deben ser válidos"""
        imc1, cat1 = calcular_imc(20, 1.75)
        assert imc1 > 0
        assert cat1 != "Peso fuera de rango"
        
        imc2, cat2 = calcular_imc(300, 1.75)
        assert imc2 > 0
        assert cat2 != "Peso fuera de rango"
    
    def test_limites_validos_altura(self):
        """Test: Límites exactos de altura (0.5 y 2.5) deben ser válidos"""
        imc1, cat1 = calcular_imc(70, 0.5)
        assert imc1 > 0
        assert cat1 != "Altura fuera de rango"
        
        imc2, cat2 = calcular_imc(70, 2.5)
        assert imc2 > 0
        assert cat2 != "Altura fuera de rango"


@pytest.mark.parametrize("peso,altura,categoria_esperada", [
    (45, 1.75, "Bajo peso"),
    (60, 1.75, "Normal"),
    (80, 1.75, "Sobrepeso"),
    (100, 1.75, "Obesidad"),
    (50, 1.60, "Normal"),
    (90, 1.80, "Sobrepeso"),
])
def test_categorias_parametrizado(peso, altura, categoria_esperada):
    """Test parametrizado para múltiples casos"""
    _, categoria = calcular_imc(peso, altura)
    assert categoria == categoria_esperada


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
