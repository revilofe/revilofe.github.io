---
title: "UD 1 - P7: SSH con Git y GitHub"
summary: SSH con Git y GitHub
description: Generar y usar clave SSH con Git y GitHub
authors:
    - Diego Cano
date: 2024-09-25
icon: 
permalink: /prog/unidad1/p1.7
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---

# P1.7 - Generar y usar clave SSH con Git y GitHub

## 1. Introducción

En esta práctica aprenderás a generar una **clave SSH** en tu ordenador y a configurarla en **GitHub** para usarla en lugar de la autenticación por **HTTPS**. SSH proporciona una autenticación más segura y sin la necesidad de introducir tu contraseña cada vez que subes o descargas cambios de GitHub.

## 2. Pasos:

### 2.1. Verificar si ya tienes una clave SSH

Antes de generar una nueva clave, es recomendable verificar si ya tienes una clave SSH generada en tu máquina. Para ello, abre tu terminal (**Git Bash** si usas Windows) y ejecuta el siguiente comando:

```bash
ls -al ~/.ssh
```

Si este comando devuelve un archivo llamado `id_rsa.pub` o similar, ya tienes una clave SSH. Si no aparece, pasa al siguiente paso para generarla.

### 2.2. Generar una nueva clave SSH

Si no tienes una clave SSH, puedes generar una nueva. Ejecuta el siguiente comando en tu terminal:

```bash
ssh-keygen -t ed25519 -C "tu_correo@ejemplo.com"
```

**Explicación:**
- `-t ed25519`: Especifica el tipo de clave SSH (recomendada por GitHub).
- `-C "tu_correo@ejemplo.com"`: Añade un comentario con tu correo electrónico para identificar la clave.

Cuando se te pida la ruta para guardar la clave, presiona **Enter** para aceptar la ubicación predeterminada (`/home/tu_usuario/.ssh/id_ed25519`). Luego, puedes establecer una contraseña para proteger la clave, o simplemente presionar **Enter** si no deseas usar una contraseña.

### 2.3. Agregar la clave SSH al agente SSH

Para usar la clave SSH, primero debes agregarla al **SSH agent** de tu sistema. Ejecuta los siguientes comandos:

1. Iniciar el agente SSH:
   ```bash
   eval "$(ssh-agent -s)"
   ```

2. Agregar tu clave SSH al agente:
   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

### 2.4. Copiar la clave pública

Debes copiar el contenido de la clave pública para añadirla a tu cuenta de GitHub. Usa el siguiente comando para mostrar la clave pública en la terminal:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copia el contenido que aparece en la terminal.

### 2.5. Añadir la clave SSH a GitHub

1. Ve a [GitHub](https://github.com) y accede a tu cuenta.
2. Dirígete a **Settings** (Configuración) haciendo clic en tu foto de perfil en la parte superior derecha.
3. En el menú de la izquierda, selecciona **SSH and GPG keys**.
4. Haz clic en el botón **New SSH key**.
5. Introduce un título para la clave (por ejemplo, "Clave de mi laptop").
6. Pega la clave pública que copiaste en el campo "Key".
7. Haz clic en **Add SSH key**.

### 2.6. Probar la conexión SSH con GitHub

Para verificar que todo está configurado correctamente, puedes probar la conexión SSH a GitHub con el siguiente comando:

```bash
ssh -T git@github.com
```

Si todo está bien configurado, deberías ver un mensaje de bienvenida de GitHub.

**Te explico lo que debe ocurrir:**

2.6.1. **Advertencia de autenticidad**: Al conectarte por primera vez a **GitHub** mediante **SSH**, tu sistema no tiene aún registrada la huella digital (fingerprint) de los servidores de GitHub. Este es el motivo por el cual te pidió confirmar la autenticidad:
   ```bash
   The authenticity of host 'github.com (140.82.121.3)' can't be established.
   ```
   Esto es normal cuando te conectas por primera vez a un servidor a través de SSH. Al responder **"yes"**, se agregó la clave del servidor de GitHub a la lista de **"known hosts"** (servidores conocidos) en tu máquina, lo que permite futuras conexiones sin tener que volver a confirmar la autenticidad del servidor.

2.6.2. **Advertencia agregada**: Luego de aceptar la autenticidad, te mostró:
   ```bash
   Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
   ```
   Esto confirma que el servidor de GitHub fue agregado a la lista de hosts conocidos de tu sistema.

2.6.3. **Autenticación exitosa**: Finalmente, el mensaje:
   ```bash
   Hi nombreUsuario! You've successfully authenticated, but GitHub does not provide shell access.
   ```
   Esto indica que te has autenticado correctamente con **GitHub** usando **SSH**. Sin embargo, GitHub no proporciona acceso a una shell interactiva a través de SSH (es decir, no puedes usar SSH para ejecutar comandos en los servidores de GitHub, solo para interactuar con los repositorios).

   Ahora que has autenticado con éxito, puedes usar **Git** con **SSH** para ejecutar comandos como `git clone`, `git push`, y `git pull` sin necesidad de introducir tu usuario y contraseña.

   Todo está funcionando correctamente, y estás listo para trabajar con **GitHub** usando tu clave SSH.

### 2.7. Configurar tu repositorio local para usar SSH

Si ya tienes un repositorio configurado con HTTPS, puedes cambiar el enlace remoto para usar SSH. Ejecuta este comando en la carpeta de tu repositorio:

```bash
git remote set-url origin git@github.com:tu_usuario/nombre_repositorio.git
```

Ahora, cuando realices operaciones como `git push` o `git pull`, se usará la autenticación por SSH.

### 2.8. Usar Git con SSH

A partir de ahora, puedes seguir usando los comandos `git push`, `git pull`, etc., pero sin tener que introducir tu usuario y contraseña cada vez, ya que la autenticación se hará automáticamente mediante la clave SSH.

## Ejercicio:

1. Genera tu clave SSH y configúrala en GitHub siguiendo los pasos anteriores.
2. Clona un repositorio desde GitHub usando SSH:
   ```bash
   git clone git@github.com:tu_usuario/tu_repositorio.git
   ```
3. Realiza cambios en el repositorio local y súbelos a GitHub usando `git push` con autenticación SSH.

---

## **Nota importante:**
Asegúrate de proteger tu clave privada SSH (no compartirla) y, si trabajas en varios dispositivos, tendrás que generar y añadir claves SSH para cada uno en GitHub.
