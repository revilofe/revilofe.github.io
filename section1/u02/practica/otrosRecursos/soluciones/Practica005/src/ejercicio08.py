"""
Ejercicio 8: Validador de Contraseñas Seguras

Descripción:
    Programa que valida si una contraseña cumple los requisitos de seguridad:
    longitud mínima, mayúsculas, minúsculas, dígitos y caracteres especiales.
    
Autor: Eduardo Fdez
Fecha: 2025-10-25
"""


def validar_contrasena(contrasena: str) -> tuple[bool, int, int, int, int, int]:
    """
    Valida si una contraseña cumple los requisitos de seguridad.
    
    Esta función es la que se evaluará mediante tests automáticos.
    
    Args:
        contrasena: La contraseña a validar
        
    Returns:
        tuple[bool, int, int, int, int, int]: 
            (es_valida, tiene_longitud, tiene_mayuscula, tiene_minuscula, tiene_digito, tiene_especial)
            donde cada componente booleana se representa como int (1 = True, 0 = False)
        
    Nota:
        - Longitud mínima: 8 caracteres
        - Debe contener al menos: 1 mayúscula, 1 minúscula, 1 dígito, 1 carácter especial (!@#$%&*)
        - Usar bucles para revisar cada carácter
        - Comparar caracteres: 'A' <= c <= 'Z', 'a' <= c <= 'z', '0' <= c <= '9'
    """
    # Validar que no esté vacía
    if contrasena == "":
        return (False, 0, 0, 0, 0, 0)
    
    # Verificar longitud
    longitud_valida: int = 1 if len(contrasena) >= 8 else 0
    
    # Inicializar contadores de requisitos
    tiene_mayuscula: int = 0
    tiene_minuscula: int = 0
    tiene_digito: int = 0
    tiene_especial: int = 0
    
    # Caracteres especiales permitidos
    caracteres_especiales: str = "!@#$%&*"
    
    # Revisar cada carácter de la contraseña
    i: int = 0
    while i < len(contrasena):
        caracter: str = contrasena[i]
        
        # Verificar si es mayúscula (A-Z)
        if caracter >= 'A' and caracter <= 'Z':
            tiene_mayuscula = 1
        
        # Verificar si es minúscula (a-z)
        if caracter >= 'a' and caracter <= 'z':
            tiene_minuscula = 1
        
        # Verificar si es dígito (0-9)
        if caracter >= '0' and caracter <= '9':
            tiene_digito = 1
        
        # Verificar si es carácter especial
        j: int = 0
        while j < len(caracteres_especiales):
            if caracter == caracteres_especiales[j]:
                tiene_especial = 1
            j += 1
        
        i += 1
    
    # Determinar si es válida (cumple todos los requisitos)
    es_valida: bool = (longitud_valida == 1 and tiene_mayuscula == 1 and 
                       tiene_minuscula == 1 and tiene_digito == 1 and tiene_especial == 1)
    
    return (es_valida, longitud_valida, tiene_mayuscula, tiene_minuscula, tiene_digito, tiene_especial)


def solicitar_contrasena() -> str:
    """
    Solicita al usuario una contraseña.
    
    Returns:
        str: La contraseña introducida
    """
    contrasena: str = input("Introduce una contraseña: ")
    return contrasena


def mostrar_resultado(es_valida: bool, long_ok: int, may_ok: int, min_ok: int, dig_ok: int, esp_ok: int, contrasena: str) -> None:
    """
    Muestra el resultado de la validación de forma clara.
    
    Args:
        es_valida: Si la contraseña es válida
        long_ok: Si tiene longitud adecuada (1) o no (0)
        may_ok: Si tiene mayúsculas (1) o no (0)
        min_ok: Si tiene minúsculas (1) o no (0)
        dig_ok: Si tiene dígitos (1) o no (0)
        esp_ok: Si tiene caracteres especiales (1) o no (0)
        contrasena: La contraseña analizada
    """
    # Mostrar análisis
    print(f"\nAnalizando contraseña: {'*' * len(contrasena)}")
    print(f"Longitud: {len(contrasena)} caracteres")
    print()
    
    # Mostrar cada requisito
    if long_ok == 1:
        print("✓ Longitud adecuada (>= 8 caracteres)")
    else:
        print("✗ Longitud insuficiente (< 8 caracteres)")
    
    if may_ok == 1:
        print("✓ Contiene mayúsculas")
    else:
        print("✗ No contiene mayúsculas")
    
    if min_ok == 1:
        print("✓ Contiene minúsculas")
    else:
        print("✗ No contiene minúsculas")
    
    if dig_ok == 1:
        print("✓ Contiene números")
    else:
        print("✗ No contiene números")
    
    if esp_ok == 1:
        print("✓ Contiene caracteres especiales")
    else:
        print("✗ No contiene caracteres especiales")
    
    # Mostrar resultado final
    print()
    if es_valida:
        print("✓ CONTRASEÑA SEGURA - Cumple todos los requisitos")
    else:
        print("✗ CONTRASEÑA INSEGURA - No cumple todos los requisitos")


def main() -> None:
    """
    Función principal que coordina la ejecución del programa.
    
    Flujo:
        1. Solicita una contraseña al usuario (lectura)
        2. Valida la contraseña usando la función obligatoria (procesamiento)
        3. Muestra el resultado detallado (salida)
    """
    # Paso 1: Lectura - Obtener contraseña del usuario
    contrasena: str = solicitar_contrasena()
    
    # Paso 2: Procesamiento - Validar usando la función obligatoria
    es_valida: bool
    long_ok: int
    may_ok: int
    min_ok: int
    dig_ok: int
    esp_ok: int
    es_valida, long_ok, may_ok, min_ok, dig_ok, esp_ok = validar_contrasena(contrasena)
    
    # Paso 3: Salida - Mostrar resultado
    mostrar_resultado(es_valida, long_ok, may_ok, min_ok, dig_ok, esp_ok, contrasena)


if __name__ == "__main__":
    main()
