---
title: "UD 2 - 2.1.1 Taxonomía de incidentes"
description: Taxonomía de incidentes
summary: Taxonomía de incidentes
authors:
    - Eduardo Fdez
date: 2024-10-21
icon: "material/file-document-outline"
permalink: /is/unidad1/2.1.1
categories:
    - IS
tags:
    - incidentes
    - taxonomía
---
## 2.1.1 Categorías de Seguridad de los Sistemas de Información

### Categorías de Seguridad de los Sistemas de Información

Desarrollo de como obtener la [categoria de seguridad de los sistemas de información](https://ens.ccn.cni.es/es/soporte-ens/real-decreto-311-2022/anexo/3)

#### **1. Fundamentos para determinar la categoría de seguridad**

La seguridad de un sistema de información se evalúa analizando el impacto de un posible incidente que afecte:

* **Los objetivos de la organización:** Por ejemplo, si una universidad pierde acceso a su sistema de calificaciones, no podrá gestionar evaluaciones ni certificados.
* **Los activos protegidos:** Como bases de datos, correos electrónicos o dispositivos, esenciales para el funcionamiento.
* **El cumplimiento legal:** Imagina que una empresa pierde registros financieros obligatorios; esto podría llevar a sanciones legales.

Es obligatorio reevaluar la seguridad del sistema cada año o si hay cambios importantes, como la introducción de nuevos servicios o tecnologías.

---

#### **2. Dimensiones de la seguridad**

Para saber cómo podría afectar un incidente, se evalúan estas dimensiones de seguridad:

1. **Confidencialidad [C]:**
   Proteger la información para que solo personas autorizadas puedan acceder.
   **Ejemplo:** Si los datos médicos de pacientes se filtran, esto viola su confidencialidad.
2. **Integridad [I]:**
   Garantizar que los datos no sean alterados sin autorización.
   **Ejemplo:** Si las notas de los estudiantes son manipuladas, la integridad del sistema se ve comprometida.
3. **Trazabilidad [T]:**
   Asegurarse de que todas las acciones puedan ser rastreadas hasta la persona que las realizó.
   **Ejemplo:** Si no hay registros claros de quién cambió información en un sistema financiero, la trazabilidad está fallando.
4. **Autenticidad [A]:**
   Confirmar la identidad de los usuarios que acceden al sistema.
   **Ejemplo:** Si alguien se hace pasar por un administrador para robar datos, hay un problema de autenticidad.
5. **Disponibilidad [D]:**
   Garantizar que la información y los servicios estén accesibles cuando se necesiten.
   **Ejemplo:** Si una tienda en línea está caída durante un fin de semana, perderá ventas y confianza del cliente.

---

#### **3. Determinación del nivel de seguridad requerido en cada dimensión**

Cada dimensión de seguridad se clasifica en uno de los tres niveles, en función del impacto de un incidente de seguridad:

1. **Nivel BAJO:**
   Impacto limitado, con las siguientes características:

   - Perjuicio menor en la capacidad operativa de la organización.
   - Daño menor y subsanable en los activos.
   - Incumplimiento legal subsanable.
   - Molestias a individuos, fácilmente reparables.

   **Ejemplo:** Un documento interno poco relevante se filtra, causando molestias menores.
2. **Nivel MEDIO:**
   Impacto grave, caracterizado por:

   - Reducción significativa de la capacidad operativa.
   - Daño significativo en los activos.
   - Incumplimiento legal material o no subsanable.
   - Perjuicio significativo para individuos, difícil de reparar.

   **Ejemplo:** Se alteran registros financieros, causando problemas legales significativos.
3. **Nivel ALTO:**
   Impacto muy grave, definido por:

   - Anulación de la capacidad operativa de la organización.
   - Daño irreparable a los activos.
   - Incumplimiento grave de leyes o regulaciones.
   - Perjuicio grave a individuos, de reparación compleja o imposible.
   
   **Ejemplo:** Una base de datos con información confidencial se pierde o elimina, afectando gravemente a la organización.

Si un sistema trata múltiples informaciones o servicios, el nivel de seguridad de cada dimensión será el más alto de entre las informaciones y servicios evaluados.

---

#### **4. Categorías de seguridad**

Se definen tres categorías para clasificar un sistema:

1. **Categoría ALTA:**
   Si cualquier dimensión alcanza un nivel ALTO.
   **Ejemplo:** Una plataforma bancaria cuya confidencialidad o disponibilidad sea crítica se clasificaría como ALTA.
2. **Categoría MEDIA:**
   Si al menos una dimensión alcanza el nivel MEDIO, pero ninguna alcanza ALTO.
   **Ejemplo:** Un sistema de nóminas que maneja datos sensibles, pero que no pone en riesgo la continuidad de la organización.
3. **Categoría BÁSICA:**
   Si las dimensiones no superan el nivel BAJO.
   **Ejemplo:** Un sistema interno para gestionar la agenda del personal administrativo.

---

#### **5. Pasos para determinar la categoría de seguridad**

La secuencia para determinar la categoría de seguridad de un sistema de información es la siguiente:

1. **Evaluar el nivel de seguridad en cada dimensión, para los servicios e inoformacion gestionada por el sistema:**
   Identifica cómo podría impactar un incidente en la confidencialidad, integridad, trazabilidad, autenticidad y disponibilidad de la información, considerando los niveles BAJO, MEDIO y ALTO.
   **Ejemplo:** Si un sistema de gestión de historias clínicas es vulnerable a filtraciones, la confidencialidad y autenticidad deben evaluarse en detalle.
2. **Determinar la categoría del sistema:**
   Usa los niveles evaluados para definir si el sistema es BÁSICO, MEDIA o ALTA.
   **Ejemplo:** Si un sistema tiene una dimensión en nivel ALTO (por ejemplo, confidencialidad), su categoría será ALTA, sin importar que otras dimensiones estén en niveles más bajos.

---

### **6. Ejemplo: Sistema de Gestión de Nóminas**

#### **Contexto:**

Un sistema de información que gestiona las nóminas de los empleados de una organización. Este sistema maneja datos sensibles como:

* Datos personales (nombre, dirección, número de identificación fiscal, cuenta bancaria).
* Historial salarial.
* Información sobre beneficios y deducciones.

#### **Paso 1: Evaluar cada dimensión de seguridad**

Analizamos el impacto de un incidente de seguridad para cada dimensión:

1. **Confidencialidad [C]:**
   * **Impacto:** Si los datos personales y bancarios son expuestos, podría haber robo de identidad o fraude financiero.
   * **Nivel:****ALTO**, porque el daño para los individuos sería muy grave y difícil de reparar.
2. **Integridad [I]:**
   * **Impacto:** Si los datos de las nóminas son alterados, podría haber errores graves en los pagos, afectando la confianza de los empleados y generando problemas legales para la organización.
   * **Nivel:****MEDIO**, porque afectaría significativamente a los empleados y a la organización, pero el problema sería subsanable.
3. **Disponibilidad [D]:**
   * **Impacto:** Si el sistema no está disponible en el momento del pago, los empleados no recibirían sus salarios a tiempo, causando descontento y posibles conflictos.
   * **Nivel:****MEDIO**, ya que aunque es grave, la organización podría gestionar la situación temporalmente.
4. **Trazabilidad [T]:**
   * **Impacto:** Si no se registran adecuadamente las operaciones en el sistema, podrían surgir disputas sobre pagos o deducciones, afectando la confianza y el cumplimiento legal.
   * **Nivel:****MEDIO**, ya que afectaría la capacidad de auditar el sistema y generar confianza.
5. **Autenticidad [A]:**
   * **Impacto:** Si no se garantiza que los usuarios son quienes dicen ser, podría haber acceso indebido a datos sensibles, resultando en fraude o abuso.
   * **Nivel:****ALTO**, ya que esto comprometería gravemente la seguridad del sistema.

---

#### **Paso 2: Determinar el nivel de seguridad del sistema en cada dimensión**

Tomamos el nivel más alto para cada dimensión evaluada:

* **Confidencialidad [C]: ALTO**
* **Integridad [I]: MEDIO**
* **Disponibilidad [D]: MEDIO**
* **Trazabilidad [T]: MEDIO**
* **Autenticidad [A]: ALTO**

---

#### **Paso 3: Determinar la categoría de seguridad del sistema**

* La dimensión más alta evaluada es **ALTO** (Confidencialidad y Autenticidad).
* Según las reglas:
  * Si **alguna dimensión alcanza ALTO**, la categoría del sistema es **ALTA**.

---

### **Categoría de Seguridad del Sistema: ALTA**

Esto significa que las medidas de seguridad aplicadas al sistema deben ser las más rigurosas para proteger los datos y garantizar su funcionalidad, como cifrado robusto, autenticación multifactorial, y monitorización constante de actividad.



#### **6. Referencias y guías**

Para una categorización precisa, se utilizarán como referencia las guías CCN-STIC del Centro Criptológico Nacional, que detallan los criterios necesarios para determinar correctamente la categoría de seguridad de los sistemas de información.



## Fuente
* [Categoria de seguridad de los sistemas de información](https://ens.ccn.cni.es/es/soporte-ens/real-decreto-311-2022/anexo/3)
* [Repositorio de trabajo de taxonomía de incidentes de seguridad](https://github.com/flosada/RSITaxonomy_ES/blob/master/humanv1.md)
* [guía CCN-STIC 817](https://www.aec.es/wp-media/uploads/DPD-00266.SEG-GUI-004-CCN-STIC-817_Gestion_de_Ciberincidentes_ENS.pdf)
* [GUÍA NACIONAL DE NOTIFICACIÓN Y GESTIÓN DE CIBERINCIDENTES](https://www.incibe.es/sites/default/files/contenidos/guias/doc/guia_nacional_notificacion_gestion_ciberincidentes.pdf)
