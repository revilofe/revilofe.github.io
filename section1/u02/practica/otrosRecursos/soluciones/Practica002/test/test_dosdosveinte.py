from dosdosveinte import leer_frase, leer_letra


def test_leer_frase(monkeypatch):
    # Test case 1: Una frase
    input_values = ["hola", "Esto es una frase"]

    def mock_input(s):
        return input_values.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)
    assert leer_frase() == "Esto es una frase"


def test_leer_letra(monkeypatch):
    # Test case 1: 1 character input
    input_values = ["", " ", "a"]

    def mock_input(s):
        return input_values.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)
    assert leer_letra() == "a"
