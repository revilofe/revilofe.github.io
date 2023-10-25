import pytest
from src.dosdosquince import leerNumerosHastaLeerCero, sumatoriaDePositivos, construyeMensaje

def test_leerNumeros(monkeypatch):
    # Test case 1: Empty input
    input_values = ['0']
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert leerNumerosHastaLeerCero() == []

    # Test case 2: one inputs
    input_values = ['5', "-3", '0']
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert leerNumerosHastaLeerCero() == [5, -3]

    # Test case 3: Multiple inputs
    input_values = ['3', '2', '1', '-4', '0']
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert leerNumerosHastaLeerCero() == [3, 2, 1, -4]

def test_sumatoriaDePositivos():
    # Test case 1: Empty list
    assert sumatoriaDePositivos([]) == 0

    # Test case 2: Single element list
    assert sumatoriaDePositivos([5, -3]) == 5

    # Test case 3: Multiple element list
    assert sumatoriaDePositivos([3, -3, 2, 1, -6]) == 6

def test_construyeMensaje():
    # Test case 1: Zero total
    assert construyeMensaje(0) == "La sumatoria de los números ingresados es: 0"

    # Test case 2: Single element total
    assert construyeMensaje(5) == "La sumatoria de los números ingresados es: 5"

    # Test case 3: Multiple element total
    assert construyeMensaje(6) == "La sumatoria de los números ingresados es: 6"
