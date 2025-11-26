---
title: "UD 3 - 3.9 Seguridad y Monitorización en Servidores Web"
description: Seguridad en servidores web, autenticación HTTP, control de acceso, logs y monitorización
summary: Autenticación HTTP Basic y Digest, control de acceso por IP, configuración de seguridad, archivos de registro logs CLF, rotación de logs, monitorización de servidores
authors:
    - Eduardo Fdez
date: 2025-11-19
icon: "material/file-document-outline"
permalink: /daw/unidad3/3.9
categories:
    - DAW
tags:
    - Seguridad
    - Autenticación
    - Logs
    - Monitorización
    - Apache
    - Control Acceso
---

## 3.9. Seguridad y Monitorización en Servidores Web

Hemos llegado al punto final de nuestra unidad sobre desarrollo y despliegue de aplicaciones web. Hemos aprendido cómo funcionan las aplicaciones, cómo se despliegan, cómo escalarlas y cómo gestionarlas. Pero hay dos aspectos absolutamente críticos que no podemos ignorar y que son transversales a todo lo anterior: **seguridad** y **monitorización**.

Imaginad que habéis desplegado una aplicación perfecta: rápida, escalable, con un código impecable. Pero un día, un atacante encuentra una vulnerabilidad y accede a datos sensibles de vuestros usuarios. O peor aún, vuestra aplicación se cae y no os enteráis hasta que los usuarios empiezan a quejarse en redes sociales. Estos escenarios son evitables si implementamos correctamente seguridad y monitorización desde el principio.

En esta última unidad, exploraremos los fundamentos de la seguridad en servidores web y cómo monitorizar nuestras aplicaciones para detectar problemas antes de que se conviertan en crisis. Este conocimiento es **esencial** para cualquier profesional responsable del despliegue de aplicaciones web.

### 1. La importancia de la seguridad: no es opcional

Antes de adentrarnos en técnicas específicas, debemos comprender por qué la seguridad es absolutamente crítica en aplicaciones web.

#### 1.1. El panorama de amenazas

Las aplicaciones web son **objetivos constantes** de ataques. Cada día, miles de bots y atacantes escanean Internet buscando vulnerabilidades.

**Tipos de atacantes:**

**Script Kiddies**

Atacantes novatos que usan herramientas automáticas:
- Buscan vulnerabilidades conocidas
- Usan exploits públicos
- Poco sofisticados pero numerosos

**Hackers organizados**

Grupos con motivación económica:
- Robo de datos para venta
- Ransomware
- Cryptomining malicioso
- Ataques dirigidos

**Insiders maliciosos**

Empleados o ex-empleados:
- Acceso legítimo mal usado
- Conocimiento interno del sistema
- Difíciles de detectar

**Estado-nación**

Ataques patrocinados por gobiernos:
- Altamente sofisticados
- Recursos ilimitados
- Objetivos específicos (espionaje, sabotaje)

#### 1.2. Consecuencias de una brecha de seguridad

Las consecuencias de un ataque exitoso son devastadoras:

**Pérdida financiera directa**

- Robo de datos de tarjetas de crédito
- Fraude financiero
- Multas regulatorias (GDPR puede multar hasta €20 millones)
- Costes de recuperación

**Daño reputacional**

- Pérdida de confianza de clientes
- Cobertura negativa en medios
- Abandono de usuarios
- Difícil recuperar la imagen

**Consecuencias legales**

- Demandas de usuarios afectados
- Investigaciones regulatorias
- Responsabilidades penales en casos graves

**Impacto operacional**

- Downtime mientras se resuelve
- Pérdida de datos
- Necesidad de reconstruir sistemas

**Casos reales:**

- **Equifax (2017)**: 147 millones de datos personales robados. Coste: $1.4 mil millones
- **Yahoo (2013-2014)**: 3 mil millones de cuentas comprometidas
- **Target (2013)**: 40 millones de tarjetas de crédito robadas. Coste: $162 millones

#### 1.3. Principios de seguridad

**Defensa en profundidad**

No confíes en una sola medida de seguridad. Múltiples capas:

```
Firewall → WAF → Servidor Web → Aplicación → Base de Datos
```

Si una capa falla, las otras siguen protegiendo.

**Principio de mínimo privilegio**

Cada usuario, proceso y sistema debe tener solo los permisos mínimos necesarios para su función. Nada más.

**Security by design**

La seguridad debe considerarse desde el diseño, no añadirse después como parche.

**Seguridad es un proceso, no un producto**

La seguridad requiere vigilancia constante, actualizaciones y mejoras continuas.

### 2. Autenticación HTTP: verificando identidades

La **autenticación** es el proceso de verificar que alguien es quien dice ser. En el contexto de servidores web, queremos controlar quién puede acceder a qué recursos.

#### 2.1. Autenticación HTTP Basic

**HTTP Basic Authentication** es el método de autenticación más simple que HTTP proporciona.

**¿Cómo funciona?**

1. Cliente solicita un recurso protegido
2. Servidor responde: `401 Unauthorized` con cabecera `WWW-Authenticate: Basic realm="Area Protegida"`
3. El navegador muestra un cuadro de diálogo pidiendo usuario y contraseña
4. El navegador envía las credenciales codificadas en Base64 en la cabecera `Authorization`
5. El servidor verifica y, si son correctas, devuelve el recurso

**Formato de la cabecera:**

```http
GET /admin/index.html HTTP/1.1
Host: ejemplo.com
Authorization: Basic dXNlcjpwYXNzd29yZA==
```

Donde `dXNlcjpwYXNzd29yZA==` es `user:password` codificado en Base64.

**Configuración en Apache:**

```apache
# Archivo: /etc/apache2/sites-available/protegido.conf

<VirtualHost *:80>
    ServerName admin.ejemplo.com
    DocumentRoot /var/www/admin
    
    <Directory /var/www/admin>
        # Habilitar autenticación
        AuthType Basic
        AuthName "Area de Administración"
        AuthUserFile /etc/apache2/.htpasswd
        Require valid-user
    </Directory>
</VirtualHost>
```

**Crear archivo de contraseñas:**

```bash
# Crear archivo y añadir primer usuario
sudo htpasswd -c /etc/apache2/.htpasswd admin

# Añadir más usuarios (sin -c)
sudo htpasswd /etc/apache2/.htpasswd usuario2

# Establecer permisos seguros
sudo chmod 640 /etc/apache2/.htpasswd
sudo chown root:www-data /etc/apache2/.htpasswd
```

**Reiniciar Apache:**

```bash
sudo systemctl reload apache2
```

Ahora, al acceder a `http://admin.ejemplo.com`, se pedirá usuario y contraseña.

**Ventajas de Basic Auth:**

- Extremadamente simple de implementar
- Soportado por todos los navegadores
- No requiere sesiones en el servidor
- Bueno para APIs simples

**Desventajas críticas:**

- **Las credenciales se envían con cada petición** (overhead)
- **Base64 NO es encriptación**, solo codificación (fácil de decodificar)
- **Vulnerable a ataques man-in-the-middle** si se usa sobre HTTP
- El navegador guarda las credenciales hasta que se cierra

!!! danger "Basic Auth solo con HTTPS"
    **NUNCA** uses HTTP Basic Authentication sin HTTPS. Las credenciales viajarían en texto plano (aunque codificadas en Base64, que es trivial de decodificar). Siempre usa HTTPS para proteger las credenciales en tránsito.

#### 2.2. Autenticación HTTP Digest

**HTTP Digest Authentication** mejora Basic Auth usando hashes en lugar de enviar contraseñas directamente.

**¿Cómo funciona?**

En lugar de enviar `user:password`, se envía un hash MD5:

1. Servidor envía un `nonce` (número aleatorio usado una sola vez)
2. Cliente calcula: `MD5(username:realm:password)` + `nonce` + `MD5(método:URI)`
3. Cliente envía el hash resultante
4. Servidor hace el mismo cálculo y compara

**Ventaja:** La contraseña nunca viaja por la red, ni siquiera codificada.

**Configuración en Apache:**

```apache
<Directory /var/www/seguro>
    AuthType Digest
    AuthName "Area Segura"
    AuthDigestDomain /var/www/seguro
    AuthDigestProvider file
    AuthUserFile /etc/apache2/.htdigest
    Require valid-user
</Directory>
```

**Crear archivo digest:**

```bash
# Crear usuarios para digest
sudo htdigest -c /etc/apache2/.htdigest "Area Segura" admin
```

**Ventajas sobre Basic:**

- Contraseña no viaja por la red
- Protección contra replay attacks (con nonce)
- Más seguro que Basic

**Desventajas:**

- Más complejo de implementar
- Menos soportado que Basic
- Aún vulnerable si el archivo .htdigest es comprometido
- MD5 es considerado débil actualmente

!!! tip "Alternativas modernas"
    Tanto Basic como Digest son anticuados. Para aplicaciones modernas, considera:
    - **OAuth 2.0**: Estándar moderno para autorización
    - **JWT (JSON Web Tokens)**: Tokens firmados para APIs
    - **OpenID Connect**: Autenticación sobre OAuth 2.0
    
    Sin embargo, Basic Auth sigue siendo útil para proteger rápidamente recursos internos o de desarrollo.

### 3. Control de acceso: quién puede entrar

Más allá de la autenticación (verificar identidad), necesitamos **control de acceso** (determinar qué pueden hacer).

#### 3.1. Control de acceso por IP

El método más simple: permitir o denegar acceso basándose en la dirección IP del cliente.

**Casos de uso:**

- **Páginas de administración**: Solo accesibles desde la red de la oficina
- **APIs internas**: Solo otros servidores de tu infraestructura
- **Staging**: Solo equipos de desarrollo
- **Protección contra países**: Bloquear IPs de países conocidos por ataques

**Configuración en Apache:**

```apache
# Permitir solo desde red local
<Directory /var/www/admin>
    Require ip 192.168.1.0/24
</Directory>

# Permitir varias IPs específicas
<Directory /var/www/api>
    Require ip 203.0.113.10
    Require ip 198.51.100.20
    Require ip 192.0.2.30
</Directory>

# Denegar acceso a todos excepto algunas IPs
<Directory /var/www/privado>
    Require all denied
    Require ip 192.168.1.100
</Directory>

# Permitir una red pero denegar IPs específicas
<Directory /var/www/mixto>
    Require ip 10.0.0.0/24
    Require not ip 10.0.0.13
</Directory>
```

**Configuración en Nginx:**

```nginx
location /admin {
    # Permitir solo estas IPs
    allow 192.168.1.0/24;
    allow 203.0.113.10;
    
    # Denegar todo lo demás
    deny all;
    
    # Contenido
    root /var/www/admin;
}
```

**Limitaciones del control por IP:**

- **IPs dinámicas**: Los usuarios domésticos cambian de IP frecuentemente
- **Proxies y VPNs**: Pueden enmascarar la IP real
- **IP compartidas**: Redes corporativas, ISPs con NAT
- **IP spoofing**: Aunque difícil, es técnicamente posible

!!! warning "No confíes solo en IPs"
    El control por IP es una capa adicional de seguridad, no debe ser la única. Combínalo con autenticación para mayor seguridad.

#### 3.2. Protección de directorios con .htaccess

En Apache, los archivos `.htaccess` permiten configuración por directorio sin modificar la configuración principal.

**Ejemplo de .htaccess completo:**

```apache
# Archivo: /var/www/html/admin/.htaccess

# Habilitar autenticación
AuthType Basic
AuthName "Área de Administración"
AuthUserFile /etc/apache2/.htpasswd
Require valid-user

# Control adicional por IP
Require ip 192.168.1.0/24

# Prevenir listado de directorios
Options -Indexes

# Denegar acceso a archivos sensibles
<FilesMatch "\.(env|log|sql|conf)$">
    Require all denied
</FilesMatch>

# Proteger contra XSS
<IfModule mod_headers.c>
    Header set X-XSS-Protection "1; mode=block"
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "SAMEORIGIN"
</IfModule>

# Denegar acceso a .htaccess mismo
<Files ".htaccess">
    Require all denied
</Files>
```

**Ventajas de .htaccess:**

- No requiere reiniciar Apache
- Los desarrolladores pueden configurar sin acceso root
- Específico por directorio

**Desventajas:**

- Apache debe leer .htaccess en cada petición (overhead de rendimiento)
- Puede ser un riesgo de seguridad si un atacante puede modificarlo
- Más difícil de mantener (configuración distribuida)

!!! note "AllowOverride"
    Para que .htaccess funcione, Apache debe tener `AllowOverride All` o directivas específicas habilitadas en la configuración principal:
    ```apache
    <Directory /var/www/html>
        AllowOverride All
    </Directory>
    ```

### 4. Seguridad adicional: capas de protección

Más allá de autenticación y control de acceso, hay muchas otras medidas de seguridad importantes.

#### 4.1. HTTPS: cifrado obligatorio

Ya lo hemos mencionado, pero vale la pena enfatizar: **HTTPS es obligatorio** en 2024.

**¿Por qué HTTPS?**

- **Cifra el tráfico**: Nadie puede leer los datos en tránsito
- **Integridad**: Garantiza que los datos no han sido modificados
- **Autenticación del servidor**: Confirma que hablas con el servidor correcto
- **SEO**: Google prioriza sitios HTTPS
- **Confianza del usuario**: Los navegadores marcan HTTP como "No seguro"

**Obtener certificado SSL/TLS gratuito con Let's Encrypt:**

```bash
# Instalar Certbot
sudo apt install certbot python3-certbot-apache

# Obtener e instalar certificado
sudo certbot --apache -d www.ejemplo.com -d ejemplo.com

# Certbot configura Apache automáticamente para HTTPS
```

Certbot renueva automáticamente los certificados antes de que expiren.

#### 4.2. Hardening del servidor

**Hardening** es el proceso de asegurar el servidor eliminando vulnerabilidades.

**Checklist de hardening:**

**1. Mantener software actualizado**

```bash
# Ubuntu/Debian
sudo apt update && sudo apt upgrade

# Habilitar actualizaciones automáticas de seguridad
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

**2. Deshabilitar servicios innecesarios**

```bash
# Listar servicios activos
systemctl list-units --type=service --state=running

# Deshabilitar servicio innecesario
sudo systemctl disable servicio-innecesario
sudo systemctl stop servicio-innecesario
```

**3. Configurar firewall**

```bash
# Ubuntu con UFW (Uncomplicated Firewall)
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw enable
```

**4. Deshabilitar información del servidor**

Evita que Apache revele su versión:

```apache
# En apache2.conf
ServerTokens Prod
ServerSignature Off
```

**5. Limitar tamaño de peticiones**

Previene ataques de denegación de servicio:

```apache
# Limitar tamaño de petición a 10MB
LimitRequestBody 10485760
```

**6. Deshabilitar métodos HTTP peligrosos**

```apache
<Location />
    <LimitExcept GET POST HEAD>
        Require all denied
    </LimitExcept>
</Location>
```

### 5. Monitorización: saber qué está pasando

La **monitorización** es el proceso de observar continuamente tus sistemas para detectar problemas, anomalías y optimizar el rendimiento.

#### 5.1. ¿Por qué monitorizar?

**Detectar problemas antes que los usuarios**

Si tu servidor se queda sin memoria, quieres saberlo antes de que el sitio se caiga.

**Entender el comportamiento**

- ¿Cuándo hay más tráfico?
- ¿Qué páginas son más lentas?
- ¿Qué usuarios están accediendo?

**Seguridad**

- Detectar intentos de intrusión
- Identificar patrones de ataque
- Responder rápidamente a incidentes

**Cumplimiento legal**

Muchas regulaciones requieren mantener logs durante períodos específicos.

#### 5.2. Logs de Apache: la caja negra del servidor

Apache genera dos tipos principales de logs:

**Access Log (Registro de accesos)**

Registra cada petición HTTP recibida:

```
/var/log/apache2/access.log
```

**Error Log (Registro de errores)**

Registra errores del servidor:

```
/var/log/apache2/error.log
```

#### 5.3. Formato CLF (Common Log Format)

El **Common Log Format** es el formato estándar para logs de acceso:

```
127.0.0.1 - usuario [10/Oct/2024:13:55:36 +0200] "GET /index.html HTTP/1.1" 200 2326
```

**Desglose de cada campo:**

```
IP         - Usuario  [Fecha y hora]           "Petición"                   Código  Tamaño
127.0.0.1  -  frank   [10/Oct/2024:13:55:36]   "GET /index.html HTTP/1.1"   200     2326
```

- **IP del cliente**: Quién hizo la petición
- **Usuario**: Si está autenticado (- si no)
- **Fecha/hora**: Cuándo se hizo la petición
- **Petición**: Método, URL y versión HTTP
- **Código de estado**: 200 OK, 404 Not Found, etc.
- **Tamaño**: Bytes enviados

**Combined Log Format (más información):**

Añade referrer y user-agent:

```
192.168.1.10 - - [19/Nov/2024:10:30:15 +0100] "GET /productos.php HTTP/1.1" 200 5234 "https://google.com/search" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
```

<figure markdown="span">
  ![Logs de Apache](assets/log.jpg){ width="700" }
  <figcaption>Ejemplo de archivo de log de Apache mostrando múltiples entradas en formato CLF. Cada línea registra una petición HTTP con IP del cliente, timestamp, método HTTP, URL solicitada, código de respuesta y bytes transferidos. Estos logs son esenciales para monitorización, análisis de tráfico y detección de anomalías de seguridad</figcaption>
</figure>

#### 5.4. Configurar logs en Apache

**Personalizar formato de log:**

```apache
# apache2.conf

# Definir formato personalizado
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined
LogFormat "%h %l %u %t \"%r\" %>s %b" common

# Usar en un VirtualHost
<VirtualHost *:80>
    ServerName www.ejemplo.com
    
    # Log de accesos
    CustomLog ${APACHE_LOG_DIR}/ejemplo_access.log combined
    
    # Log de errores
    ErrorLog ${APACHE_LOG_DIR}/ejemplo_error.log
    
    # Nivel de detalle de errores (debug, info, notice, warn, error, crit, alert, emerg)
    LogLevel warn
</VirtualHost>
```

**Variables disponibles:**

- `%h`: IP del cliente
- `%t`: Timestamp
- `%r`: Primera línea de la petición
- `%>s`: Código de estado
- `%b`: Tamaño de la respuesta
- `%{User-Agent}i`: User-agent del navegador
- `%{Referer}i`: De dónde vino el usuario
- `%D`: Tiempo que tardó en servir la petición (microsegundos)

#### 5.5. Analizar logs: encontrando patrones

Los logs son inútiles si no los analizas. Herramientas útiles:

**Comandos básicos:**

```bash
# Ver últimas 50 líneas del log
tail -n 50 /var/log/apache2/access.log

# Seguir el log en tiempo real
tail -f /var/log/apache2/access.log

# Buscar todas las peticiones 404
grep " 404 " /var/log/apache2/access.log

# Contar cuántas peticiones 404 hubo
grep " 404 " /var/log/apache2/access.log | wc -l

# IPs que más acceden
awk '{print $1}' /var/log/apache2/access.log | sort | uniq -c | sort -rn | head -10

# URLs más solicitadas
awk '{print $7}' /var/log/apache2/access.log | sort | uniq -c | sort -rn | head -10

# Peticiones por hora
awk '{print $4}' /var/log/apache2/access.log | cut -d: -f2 | sort | uniq -c
```

**Herramientas de análisis avanzadas:**

**AWStats**

Genera estadísticas visuales de logs:
- Visitas por hora, día, mes
- Países de origen
- Navegadores y sistemas operativos
- Páginas más visitadas

```bash
sudo apt install awstats
sudo /usr/lib/cgi-bin/awstats.pl -config=ejemplo.com -update
```

**GoAccess**

Analizador de logs en tiempo real, terminal o web:

```bash
sudo apt install goaccess

# Modo terminal
goaccess /var/log/apache2/access.log

# Generar reporte HTML
goaccess /var/log/apache2/access.log -o reporte.html
```

**ELK Stack (Elasticsearch, Logstash, Kibana)**

La solución enterprise para análisis de logs:
- **Logstash**: Recolecta y procesa logs
- **Elasticsearch**: Almacena y indexa logs
- **Kibana**: Visualiza datos con dashboards

Potente pero complejo de configurar.

#### 5.6. Rotación de logs: gestión del crecimiento

Los logs crecen indefinidamente si no se gestionan. Un servidor ocupado puede generar **gigabytes de logs al día**.

**Problemas de logs sin rotar:**

- Llenan el disco
- Se vuelven lentos de analizar
- Imposibles de gestionar manualmente

**Solución: Rotación de logs**

Rotar significa:
1. Cerrar el archivo de log actual
2. Renombrarlo (ej: `access.log` → `access.log.1`)
3. Comprimir logs antiguos (ej: `access.log.2.gz`)
4. Crear nuevo archivo de log vacío
5. Eliminar logs muy antiguos

**Rotación con logrotate (estándar en Linux):**

```bash
# Archivo: /etc/logrotate.d/apache2

/var/log/apache2/*.log {
    # Rotar semanalmente
    weekly
    
    # Mantener 52 rotaciones (1 año de logs semanales)
    rotate 52
    
    # Comprimir logs antiguos
    compress
    delaycompress
    
    # No rotar si el log está vacío
    notifempty
    
    # Crear nuevo log con estos permisos
    create 640 root adm
    
    # Si falta el log, no generar error
    missingok
    
    # Ejecutar después de rotar
    postrotate
        # Recargar Apache para que use el nuevo archivo
        /usr/sbin/apache2ctl graceful > /dev/null
    endscript
}
```

**Forzar rotación manual:**

```bash
sudo logrotate -f /etc/logrotate.d/apache2
```

**Política de retención típica:**

- **Logs diarios**: Mantener 7 días
- **Logs semanales**: Mantener 4-8 semanas
- **Logs mensuales**: Mantener 12 meses
- **Logs anuales**: Archivar para cumplimiento legal

#### 5.7. Monitorización del servidor completo

Más allá de logs, monitoriza el estado del servidor:

**Métricas clave a monitorizar:**

**CPU**

```bash
# Ver uso de CPU
top

# Más visual
htop
```

**Memoria**

```bash
# Ver memoria disponible
free -h
```

**Disco**

```bash
# Espacio disponible
df -h

# Uso de directorios
du -sh /var/www/*
```

**Conexiones de red**

```bash
# Conexiones activas
netstat -an | grep :80 | wc -l

# Con más detalle
ss -s
```

**Herramientas de monitorización:**

**Nagios**: Monitorización enterprise

**Zabbix**: Potente y open source

**Prometheus + Grafana**: Solución moderna, especialmente para contenedores

**New Relic / Datadog**: SaaS, muy fáciles de usar

**Ejemplo de alerta simple con cron:**

```bash
#!/bin/bash
# Archivo: /usr/local/bin/check-disk.sh

THRESHOLD=90
USAGE=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')

if [ $USAGE -gt $THRESHOLD ]; then
    echo "ALERTA: Disco al ${USAGE}%" | mail -s "Disco lleno" admin@ejemplo.com
fi
```

```bash
# Añadir a crontab (ejecutar cada hora)
0 * * * * /usr/local/bin/check-disk.sh
```

## Resumen de la unidad

Hemos completado la unidad con los aspectos críticos de seguridad y monitorización:

1. **La seguridad no es opcional**: Las consecuencias de brechas son devastadoras; debemos implementar defensa en profundidad.

2. **Autenticación HTTP Basic y Digest** verifican identidades, aunque deben usarse siempre con HTTPS.

3. **Control de acceso por IP** añade una capa adicional de protección, especialmente para áreas administrativas.

4. **Hardening del servidor** reduce la superficie de ataque mediante actualizaciones, firewalls y configuración segura.

5. **Los logs** son la caja negra del servidor; registran todo y son esenciales para debugging, análisis y seguridad.

6. **La rotación de logs** gestiona el crecimiento infinito mediante archivado, compresión y eliminación programada.

7. **La monitorización continua** detecta problemas antes de que afecten a usuarios, mediante métricas y alertas.

Con este conocimiento, estáis preparados para desplegar y mantener aplicaciones web seguras y monitorizadas profesionalmente.

## Referencias y bibliografía

- [Jose Luis González](https://github.com/joseluisgs). *Despliegue de aplicaciones Web - 2025 2026*. [https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026](https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026)
- OWASP. (2024). *OWASP Top 10*. [https://owasp.org/www-project-top-ten/](https://owasp.org/www-project-top-ten/)
- Apache Software Foundation. (2024). *Apache Security Tips*. [https://httpd.apache.org/docs/2.4/misc/security_tips.html](https://httpd.apache.org/docs/2.4/misc/security_tips.html)
- Mozilla. (2024). *Web Security Guidelines*. [https://infosec.mozilla.org/guidelines/web_security](https://infosec.mozilla.org/guidelines/web_security)

## Recursos adicionales

- [Let's Encrypt](https://letsencrypt.org/) - Certificados SSL/TLS gratuitos
- [Security Headers](https://securityheaders.com/) - Verifica headers de seguridad
- [SSL Labs](https://www.ssllabs.com/ssltest/) - Analiza configuración HTTPS
- [GoAccess](https://goaccess.io/) - Analizador de logs en tiempo real
- [Fail2Ban](https://www.fail2ban.org/) - Protección contra fuerza bruta
