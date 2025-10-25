"""
Tests para el Ejercicio 9: Simulador de Carrera de Caracoles

Este archivo contiene los tests automáticos que se usarán para evaluar
la función simular_carrera del ejercicio 9.
"""

import pytest
from ejercicio09 import simular_carrera


def test_velocidades_invalidas():
    """
    Test: Velocidades fuera del rango permitido (1-10)
    """
    # Velocidad menor a 1
    assert simular_carrera(0, 5, 5, 100) == (0, 0)
    assert simular_carrera(5, 0, 5, 100) == (0, 0)
    assert simular_carrera(5, 5, 0, 100) == (0, 0)
    
    # Velocidad mayor a 10
    assert simular_carrera(11, 5, 5, 100) == (0, 0)
    assert simular_carrera(5, 11, 5, 100) == (0, 0)
    assert simular_carrera(5, 5, 11, 100) == (0, 0)


def test_distancia_invalida():
    """
    Test: Distancia de meta inválida (<= 0)
    """
    assert simular_carrera(5, 5, 5, 0) == (0, 0)
    assert simular_carrera(5, 5, 5, -10) == (0, 0)


def test_ganador_caracol1():
    """
    Test: Caracol 1 es más rápido y debe ganar
    """
    ganador, turnos = simular_carrera(10, 5, 3, 100)
    assert ganador == 1
    assert turnos == 10  # 100 / 10 = 10 turnos


def test_ganador_caracol2():
    """
    Test: Caracol 2 es más rápido y debe ganar
    """
    ganador, turnos = simular_carrera(3, 10, 5, 100)
    assert ganador == 2
    assert turnos == 10  # 100 / 10 = 10 turnos


def test_ganador_caracol3():
    """
    Test: Caracol 3 es más rápido y debe ganar
    """
    ganador, turnos = simular_carrera(3, 5, 10, 100)
    assert ganador == 3
    assert turnos == 10  # 100 / 10 = 10 turnos


def test_empate_gana_primero():
    """
    Test: En caso de empate, gana el caracol con número más bajo
    """
    # Todos con la misma velocidad - debe ganar caracol 1
    ganador, turnos = simular_carrera(5, 5, 5, 50)
    assert ganador == 1
    assert turnos == 10  # 50 / 5 = 10 turnos
    
    # Caracol 2 y 3 empatan pero más rápidos - debe ganar caracol 2
    ganador, turnos = simular_carrera(3, 7, 7, 70)
    assert ganador == 2
    assert turnos == 10  # 70 / 7 = 10 turnos


def test_distancia_no_divisible():
    """
    Test: Distancia que no es múltiplo exacto de la velocidad
    """
    # Velocidad 3, distancia 10: necesita 4 turnos (3+3+3+3=12 >= 10)
    ganador, turnos = simular_carrera(3, 1, 1, 10)
    assert ganador == 1
    assert turnos == 4
    
    # Velocidad 7, distancia 20: necesita 3 turnos (7+7+7=21 >= 20)
    ganador, turnos = simular_carrera(7, 2, 2, 20)
    assert ganador == 1
    assert turnos == 3


def test_carrera_corta():
    """
    Test: Carrera muy corta (meta cercana)
    """
    # Meta a 5 cm, velocidad 10: termina en 1 turno
    ganador, turnos = simular_carrera(10, 5, 3, 5)
    assert ganador == 1
    assert turnos == 1


def test_carrera_larga():
    """
    Test: Carrera muy larga
    """
    # Meta a 1000 cm, velocidad 10: necesita 100 turnos
    ganador, turnos = simular_carrera(10, 5, 3, 1000)
    assert ganador == 1
    assert turnos == 100


def test_velocidades_minimas_maximas():
    """
    Test: Velocidades en los límites (1 y 10)
    """
    # Velocidad mínima (1)
    ganador, turnos = simular_carrera(1, 1, 1, 10)
    assert ganador == 1
    assert turnos == 10
    
    # Velocidad máxima (10)
    ganador, turnos = simular_carrera(10, 10, 10, 100)
    assert ganador == 1
    assert turnos == 10
    
    # Mezcla de mínima y máxima
    ganador, turnos = simular_carrera(1, 5, 10, 50)
    assert ganador == 3
    assert turnos == 5


def test_diferencias_velocidad_pequeñas():
    """
    Test: Velocidades muy similares
    """
    # Velocidades consecutivas
    ganador, turnos = simular_carrera(5, 6, 7, 70)
    assert ganador == 3
    assert turnos == 10  # 70 / 7 = 10 turnos


def test_casos_reales():
    """
    Test: Casos de carreras realistas
    """
    # Caracol 1 rápido, otros lentos
    ganador, turnos = simular_carrera(8, 3, 2, 80)
    assert ganador == 1
    assert turnos == 10
    
    # Caracol 2 mediano gana
    ganador, turnos = simular_carrera(2, 6, 4, 60)
    assert ganador == 2
    assert turnos == 10
    
    # Todos diferentes
    ganador, turnos = simular_carrera(4, 7, 9, 90)
    assert ganador == 3
    assert turnos == 10


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
