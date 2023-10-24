import pytest
from src.dosdoscatorce import leerNumeros, sumatoria, construyeMensaje

def test_leerNumeros(monkeypatch):
    # Test case 1: Empty input
    input_values = ['0']
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert leerNumeros() == []

    # Test case 2: one inputs
    input_values = ['5', '0']
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert leerNumeros() == [5]

    # Test case 3: Multiple inputs
    input_values = ['3', '2', '1', '0']
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert leerNumeros() == [3, 2, 1]

def test_sumatoria():
    # Test case 1: Empty list
    assert sumatoria([]) == 0

    # Test case 2: Single element list
    assert sumatoria([5]) == 5

    # Test case 3: Multiple element list
    assert sumatoria([3, 2, 1]) == 6

def test_construyeMensaje():
    # Test case 1: Zero total
    assert construyeMensaje(0) == "La sumatoria de los números ingresados es: 0"

    # Test case 2: Single element total
    assert construyeMensaje(5) == "La sumatoria de los números ingresados es: 5"

    # Test case 3: Multiple element total
    assert construyeMensaje(6) == "La sumatoria de los números ingresados es: 6"
