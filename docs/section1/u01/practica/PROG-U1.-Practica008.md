---
title: "UD 1 - P8: Sincronizar con la plantilla original del assignment"
summary: Sincronizar con la plantilla original del assignment
description: Sincronizar tu repositorio con los cambios realizados en la plantilla original del profesor (assignment)
authors:
    - Diego Cano
date: 2024-09-30
icon: 
permalink: /prog/unidad1/p1.8
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---

## P1.8 - Sincronizar tu repositorio con los cambios realizados en la plantilla original del profesor (assignment)

Este es el flujo de comandos que debes seguir para **sincronizar tu repositorio local** con los cambios que el profesor haya realizado en la plantilla del assignment en GitHub Classroom.

### 1. **Verificar si ya tienes configurado el `upstream`**

Antes de empezar a obtener los cambios del repositorio del profesor, es importante verificar si ya tienes configurado el **remote** `upstream`, que es el repositorio de la plantilla original.

Para hacerlo, ejecuta el siguiente comando en **Git Bash**:

```bash
git remote -v
```

Este comando te mostrará los **remotes** que tienes configurados en tu repositorio local. Debes ver algo como esto:

```bash
origin    git@github.com:tu-usuario/repo-alumno.git (fetch)
origin    git@github.com:tu-usuario/repo-alumno.git (push)
upstream  https://github.com/profesor/repo-plantilla.git (fetch)
upstream  https://github.com/profesor/repo-plantilla.git (push)
```

- **`origin`**: Es tu propio repositorio en GitHub (el que usas para hacer `push` y `pull` de tus cambios).
- **`upstream`**: Es el repositorio de la plantilla del profesor, desde donde obtendrás los cambios que él haya realizado.

#### Si no ves la línea de `upstream`...

Si no ves la línea de `upstream`, debes añadir el remote con la **URL HTTPS** del repositorio del profesor. Para agregar el `upstream`, ejecuta el siguiente comando:

```bash
git remote add upstream https://github.com/profesor/repo-plantilla.git
```

> **Nota**: Debe ser la URL **HTTPS** porque la URL SSH solo está configurada para que puedas hacer `push` a tu propio repositorio. No puedes usar SSH para el repositorio del profesor sin tener su clave pública.

### 2. **Obtener los cambios del repositorio de plantilla (`upstream`)**

Una vez que hayas configurado el `upstream`, o si ya lo tenías configurado, puedes proceder a **obtener los cambios** que el profesor haya hecho en la plantilla original. Para hacerlo, ejecuta este comando en **Git Bash**:

```bash
git fetch upstream
```

Este comando descarga los cambios del repositorio del profesor (el `upstream`), pero no los fusiona todavía. Simplemente los trae a tu repositorio local.

### 3. **Fusionar los cambios con tu rama principal (`main`)**

Después de haber obtenido los cambios del profesor, el siguiente paso es **fusionar esos cambios con tu rama principal** (la rama `main`). Para hacerlo, debes ejecutar:

```bash
git merge upstream/main
```

Este comando intentará fusionar los cambios de la rama `main` del repositorio del profesor en la rama `main` de tu repositorio local. Git hará esto automáticamente, a menos que haya conflictos.

### 4. **Si aparece el error "unrelated histories" (historias no relacionadas)**

Si Git detecta que los historiales de tu repositorio y el del profesor no están relacionados, es posible que veas este error:

```
fatal: refusing to merge unrelated histories
```

Este error ocurre cuando los commits en el repositorio del profesor han cambiado significativamente después de que aceptaste el assignment.

#### Solución para "historias no relacionadas":

Para solucionar esto, debes **forzar la fusión de las historias** ejecutando el siguiente comando:

```bash
git merge upstream/main --allow-unrelated-histories
```

Este comando le dice a Git que ignore el hecho de que los historiales no están relacionados y que fusione los cambios de todos modos.

### 5. **Resolver conflictos (si los hay)**

Si durante el proceso de fusión Git detecta **conflictos** (por ejemplo, cuando tanto tú como el profesor han modificado el mismo archivo), tendrás que resolverlos manualmente.

#### Pasos para resolver conflictos:

1. **Abrir los archivos en conflicto**: Los archivos en conflicto estarán marcados por Git. Debes abrir esos archivos en tu editor de texto (como **VSCode** o **Notepad++**).

2. **Identificar los conflictos**: Los conflictos estarán marcados de la siguiente manera:

   ```bash
   <<<<<<< HEAD
   # Esta es la versión de tu repositorio local
   =======
   # Esta es la versión del upstream (repositorio del profesor)
   >>>>>>> upstream/main
   ```

3. **Resolver los conflictos**: Decide qué versión quieres conservar (la tuya, la del profesor o una combinación de ambas) y elimina las marcas `<<<<<<<`, `=======`, y `>>>>>>>`.

4. **Añadir los archivos resueltos**: Una vez que hayas resuelto los conflictos, debes añadir los archivos resueltos usando:

   ```bash
   git add <archivo_resuelto>
   ```

5. **Completar la fusión**: Después de haber añadido todos los archivos resueltos, puedes completar la fusión con:

   ```bash
   git commit
   ```

### 6. **Subir los cambios a tu repositorio remoto en GitHub**

Después de realizar la fusión y resolver los conflictos, debes subir los cambios a tu repositorio remoto en GitHub. Para hacerlo, debes ejecutar:

```bash
git push
```

Este comando subirá todos los commits locales (incluyendo la fusión) a tu repositorio remoto en GitHub.

### Resumen de los comandos que debes ejecutar:

1. **Verificar los remotes configurados**:

   ```bash
   git remote -v
   ```

2. **Añadir el remote `upstream` (si no está configurado)**:

   ```bash
   git remote add upstream https://github.com/profesor/repo-plantilla.git
   ```

3. **Obtener los cambios del repositorio de plantilla**:

   ```bash
   git fetch upstream
   ```

4. **Fusionar los cambios con la rama `main`**:

   ```bash
   git merge upstream/main
   ```

5. **Si ves "historias no relacionadas"**:

   ```bash
   git merge upstream/main --allow-unrelated-histories
   ```

6. **Resolver conflictos (si los hay)**:

   - Abrir los archivos en conflicto.
   - Resolver los conflictos manualmente.
   - Añadir los archivos resueltos:

     ```bash
     git add <archivo_resuelto>
     ```

   - Completar la fusión:

     ```bash
     git commit
     ```

7. **Subir los cambios a tu repositorio remoto**:

   ```bash
   git push
   ```

---

### Conclusión:

Siguiendo estos pasos, podrás sincronizar los cambios que el profesor haya hecho en la plantilla de GitHub Classroom con tu propio repositorio. Si necesitas forzar la fusión debido a "historias no relacionadas" o resolver conflictos, estos comandos te ayudarán a manejar cualquier situación que se presente.
