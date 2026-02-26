#!/usr/bin/env python3
"""
Script: generar_indice.py
Autor: Eduardo Fernández Oliver (con ayuda de ChatGPT)
Descripción:
------------
Este script genera automáticamente un índice para un archivo markdown de tipo "slides".
El índice se inserta justo en la sección `## Índice`, reemplazando cualquier índice previo.

Funcionamiento:
---------------
1. Se leen todos los títulos del archivo (`##`, `###`, `####`) hasta el nivel indicado:
   - Nivel 1 → solo `##`
   - Nivel 2 (por defecto) → `##` y `###`
   - Nivel >=3 → `##`, `###` y `####`

2. Se ignora siempre el propio `## Índice` inicial, ya que es el marcador de posición
   donde se añadirá el nuevo índice.

3. Los títulos se convierten en una lista jerárquica con guiones:
   - `##` → `- Título`
   - `###` → `    - Subtítulo`
   - `####` → `        - Subsubtítulo`

4. El índice se divide en bloques (`## Índice 1`, `## Índice 2`, etc.) cuando supera
   un máximo de 6 líneas de contenido.
   Reglas para la división:
   - Un padre (`##`) no puede quedar solo sin al menos un hijo.
   - Si un padre ya tiene al menos un hijo listado y no caben más, se corta el bloque.
   - En la nueva slide, el padre se repite junto a los hijos restantes para mantener
     la jerarquía visual.

5. Finalmente, se reemplaza todo el contenido entre `## Índice` y la siguiente línea `---`
   por los nuevos bloques de índice.
   El separador `---` se mantiene (no se duplica).

Opciones:
---------
- `-n` / `--nivel` → Nivel máximo a incluir en el índice (por defecto 2).
- `-b` / `--backup` → Si se indica, no sobrescribe el archivo original, sino que
  genera un nuevo fichero con sufijo `_out.md`.

Ejemplos de uso:
----------------
1. Generar índice sobrescribiendo el archivo:
   $ python3 generar_indice.py slides.md -n 2

2. Generar índice hasta nivel 3 y guardar en copia:
   $ python3 generar_indice.py slides.md -n 3 -b
"""

import argparse
import re
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Generar índice en un archivo markdown de slides.")
    parser.add_argument("file", help="Archivo markdown de entrada (ej: slides.md)")
    parser.add_argument("-n", "--nivel", type=int, default=2,
                        help="Nivel de índice: 1=##, 2=##+###, >=3=##+### +#### (default=2)")
    parser.add_argument("-b", "--backup", action="store_true",
                        help="Si se indica, genera un fichero de salida (slides_out.md) en vez de sobrescribir.")
    return parser.parse_args()

def nivel_titulo(line):
    """Devuelve el nivel del título en número (#=1, ##=2, etc.), o 0 si no es título."""
    if line.startswith("#"):
        return len(line.split(" ")[0])
    return 0

def extraer_titulos(lines, nivel_max):
    """
    Devuelve una lista de (nivel, texto) con los títulos según el nivel.
    Saltamos el '## Índice'.
    """
    titulos = []
    for line in lines:
        if not line.strip().startswith("#"):
            continue
        if line.strip().startswith("## Índice"):
            continue
        lvl = nivel_titulo(line.strip())
        if lvl == 2 and nivel_max >= 1:
            titulos.append((2, line.strip("# ").strip()))
        elif lvl == 3 and nivel_max >= 2:
            titulos.append((3, line.strip("# ").strip()))
        elif lvl == 4 and nivel_max >= 3:
            titulos.append((4, line.strip("# ").strip()))
    return titulos

def formatear_indice(titulos, max_lineas=6):
    """
    Genera el índice dividido en bloques (## Índice X).
    Respeta la regla: un padre no puede quedar solo sin al menos un hijo.
    """
    bloques = []
    bloque_actual = []
    contador = 1

    i = 0
    while i < len(titulos):
        nivel, texto = titulos[i]
        linea = f"{'    ' * (nivel-2)}- {texto}" if nivel >= 2 else f"- {texto}"

        if len(bloque_actual) >= max_lineas:
            bloques.append((contador, bloque_actual))
            contador += 1
            bloque_actual = []

            if nivel > 2:
                padre_idx = i - 1
                while padre_idx >= 0 and titulos[padre_idx][0] >= nivel:
                    padre_idx -= 1
                if padre_idx >= 0:
                    padre_nivel, padre_texto = titulos[padre_idx]
                    linea_padre = f"{'    ' * (padre_nivel-2)}- {padre_texto}"
                    bloque_actual.append(linea_padre)

        bloque_actual.append(linea)
        i += 1

    if bloque_actual:
        bloques.append((contador, bloque_actual))

    resultado = []
    for num, contenido in bloques:
        resultado.append(f"## Índice {num}\n")
        resultado.extend(contenido)
        resultado.append("")
        resultado.append("")
    return "\n".join(resultado).strip()

def reemplazar_indice(lines, nuevo_indice):
    """
    Sustituye la sección entre '## Índice' y el siguiente '---' por el nuevo índice.
    """
    inicio, fin = None, None
    for idx, line in enumerate(lines):
        if line.strip().startswith("## Índice"):
            inicio = idx
        elif inicio is not None and line.strip() == "---":
            fin = idx
            break

    if inicio is None or fin is None:
        raise ValueError("No se encontró sección de índice correctamente delimitada.")

    # eliminamos también la cabecera original ## Índice
    return lines[:inicio] + [nuevo_indice + "\n"] + lines[fin:]

def main():
    args = parse_args()

    with open(args.file, encoding="utf-8") as f:
        lines = f.readlines()

    titulos = extraer_titulos(lines, args.nivel)
    nuevo_indice = formatear_indice(titulos, max_lineas=6)
    nuevas_lineas = reemplazar_indice(lines, nuevo_indice)

    if args.backup:
        out_file = os.path.splitext(args.file)[0] + "_out.md"
    else:
        out_file = args.file

    with open(out_file, "w", encoding="utf-8") as f:
        f.writelines(nuevas_lineas)

    print(f"Índice generado en {out_file}")

if __name__ == "__main__":
    main()
