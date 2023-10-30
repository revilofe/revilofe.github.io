import pytest
from src.dosdosveinticinco import leeFraseDeUsuario, identificarPalabraMasLarga


def test_leeFraseDeUsuario(monkeypatch):
    input_values = ["Hola Consuelo una pregunta rapida"]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert leeFraseDeUsuario() == "Hola Consuelo una pregunta rapida"


def test_leeFraseDeUsuarioVacia(monkeypatch):
    input_values = ["\n", "", "Hola Consuelo una pregunta rapida"]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    assert leeFraseDeUsuario() == "Hola Consuelo una pregunta rapida"


def test_identificarPalabraMasLarga():
    assert identificarPalabraMasLarga("hola") == "hola"
    assert identificarPalabraMasLarga("hola hol") == "hola"
