![](assets/IS-U321-AnalisisDeEvidenciasEInvestigacionDeIncidentes0.png)

__Análisis de evidencias e investigación de incidente__

#### RA3
b) Se ha realizado un análisis de evidencias.
c) Se ha realizado la investigación de incidentes de ciberseguridad.

#### ÍNDICE

#### Análisis de evidencias

<span style="color:#FF0000"> __working in progress__ </span>

#### Análisis de evidencias e investigación del incidente

ANÁLISIS DE EVIDENCIAS

El objetivo de esta fase es identificar o detectar un ciber incidente para lo cual es importante realizar una monitorización lo más completa posible\. Teniendo en cuenta la máxima de que no todos los eventos o alertas de ciberseguridad son ciber incidentes\.

INVESTIGACIÓN DEL INCIDENTE

Los incidentes son cualquier evento que no sea parte de la operación estándar de un servicio que ocasione\, o pueda ocasionar\, una interrupción o una reducción de la calidad de ese servicio\.

#### Análisis de evidencias

Una vez recopiladas las evidencias digitales y almacenadas adecuadamente\, el  _análisis forense_  digital debe encargarse de:

la  __reconstrucción__

la  __temporalización__

de los  _hechos ocurridos _ con los datos recopilados\.

Deberán  __recopilarse__  los hechos desde el momento inicial del incidente hasta su descubrimiento\.

Esta fase  __no termina hasta__  que no se puede determinar

qué o quién realizó el incidente

cómo lo hizo/cómo se produjo

cuál fue el objetivo y bajo qué circunstancias se cometió

qué afectación ha tenido en el sistema\.

Es el núcleo duro de la investigación y tiene que concluir con esta información\.

#### Análisis de evidencias - Premisas

Para llevar a cabo este proceso\, es importante recordar las premisas básicas:

__No__  se debe  __trabajar__   __con los datos originales__ \.

Se debe r __espetar cada una de las leyes vigentes__  en la jurisdicción donde se lleva a cabo la investigación\.

Los  __resultados__  que se obtengan de todo el proceso han de ser  __verificables y reproducibles__

* Para llevar a cabo este proceso\, es importante recordar las premisas básicas:
* Es importante disponer de documentación adicional con información de diversa índole:
  * Sistema operativo del sistema
  * Programas instalados en el equipo\.
  * Hardware\, accesorios y periféricos que forman parte del sistema\.
  * Datos relativos a la conectividad del equipo:
    * Si dispone de firewall\, ya sea físico o lógico\.
    * Si el equipo se encuentra en zonas de red especiales\, por ejemplo\, DMZ\.
    * Si tiene conexión a Internet o utiliza proxies\.
  * Datos generales de configuración que puedan ser de interés para el investigador para ayudar en la tarea\.

#### Análisis de evidencias - Pasos a seguir

* Fase de análisis:
* No existe ningún procedimiento estándar que dicte los pasos a seguir en la investigación\.
* Habŕa que estudiar cada caso por separado teniendo en cuenta las particularidades del sistema afectado:
  * No será lo mismo analizar un SO Windows o uno Linux
  * No será lo mismo un caso de intrusión en el correo electrónico de alguien o un ataque de denegación de servicio\.
  * De igual forma\, no se actuará igual en un caso de instalación de malware que destruye información en disco que uno que envíe lo que se teclea en un equipo\.

En todo caso\, Se pueden destacar varios pasos\, que habrá que adaptar en cada caso:

Preparar un  __entorno de trabajo__  adaptado a las necesidades del incidente\.

Reconstruir una  __línea temporal __ con los hechos sucedidos\.

Determinar qué __ procedimiento se llevó a cabo__  por parte del atacante\.

Identificar el  __autor o autores__  de los hechos\.

Evaluar el  __impacto causado__  y si es posible la recuperación del sistema\.

#### Pasos

#### Preparar un entorno de trabajo

* Preparar un entorno adecuado para llevar la investigación\. Premisa de  _no tocar los dispositivos originales y trabajar con copias de las evidencias_ :
* Decidir si realizar la investigación sobre discos originales\, lo que conlleva riesgos\, por tanto:
* Caliente
  * Precaución\, poniendo el disco en modo solo lectura\.
  * Cuidad para no cometer un error que invalide las pruebas\.

* Preparar un entorno adecuado para llevar la investigación\. Premisa de  _no tocar los dispositivos originales y trabajar con copias de las evidencias_ :
* Decidir si realizar la investigación sobre discos originales\, lo que conlleva riesgos\, por tanto:
* Frio
  * Preparar un entorno\, con el mismo SO de equipo afectado y montar la imagen\.
    * Crear imagen de la copia original
    * Podremos ejecutar archivos\, realizar tareas más intrusivas\, siempre habrá marcha atrás\.
    * En caso de malware se podrá ejecutar sin miedo\, sin que la copia original se vea afectada\, pudiendo ser más agresivos en los trabajos de investigación

* Preparar un entorno adecuado para llevar la investigación\. Premisa de  _no tocar los dispositivos originales y trabajar con copias de las evidencias_ :
* Posible entorno\, con dos estaciones de trabajo \(WS\):
* Primera WS: dos discos duros
  * Primero: SO anfitrión con el que se realizará el análisis de evidencias
  * Segundo: Imágen del disco duro del equipo atacado\.
* Segunda WS: SO configurado exactamente igual q el equipo atacado
* Se podrá analizar los cambios producidos en ambos equipos pudiendo detectar los efectos ocasionados por los ataques sufridos en el equipo\.

#### Creación de línea temporal

El primer paso\, crear una línea temporal donde ubica los acontecimientos que han tenido lugar en el equipo\. Para crear línea temporal construir un esbozo de los puntos clave en el tiempo:

Instalación del sistema operativo

Borrado de determinados archivos

Instalación de determinados programas

* Referirnos a los tiempos MACD de los archivos
  * \(Modificación\, Acceso\, Cambio\, Borrado\)
  * Importante los husos horarios\, importante para dar crédito a las pruebas\.
* Identificar la fecha de instalación del SO y los usuarios creados
  * Estudiar discrepancia o usuarios fuera de lo común en los últimos instantes
* Buscar más información en los ficheros que se ven “a simple vista”
  * Que programas fuero lo últimos en ser instalados\. Seguramente en rutas poco habituales: archivos temporales\, mezclados con librerías u otros archivos\.
  * Qué cambios repercutieron en el sistema
* Buscar información en archivos que no están “a la vista”\.
  * Habilitar la visualización de archivos ocultos y sus extensiones\.
  * Utilizar herramientas que permitan recuperar archivos borrados\.
  * Utilizar programas que permitan obtener información mediante esteganografía

#### Determinar cómo se actuó

* Para obtener esta información\, es necesario investigar la memoria\. Por tanto\, en la medida de lo posible\, realizar un volcado de memoria para:
* Obtener procesos que se estaban ejecutando y ocultados\, nos dará pistas de cómo se actuó\.
  * Los procesos legítimos pueden ocultar procesos malintencionados camuflados
    * Sin proceso padre
    * Con nombres parecidos a procesos legítimos
* Obtener ejecutables y librerías involucrados\.
  * Estudiar mediante programas que nos aportan esta información\, si tienen cadenas \(String\) sospechosas\.
* Comandos ejecutados desde consola\.

#### Identificar autores

Es importante analizar dos vertientes a la hora de continuar en el análisis de las evidencias\, y en concreto con la la identificación de los autores:

Si se realiza un peritaje con fin:

inculpatorios: Intentar resolver quién es el autor o dar pistas fiables para que se continúe el estudio en otros ámbitos\.

correctivos: no nos interesa perder el tiempo en esta fase\, y sería mejor dedicar el tiempo al estudio de impacto causado y mejoras para evitar cuestiones similares\.

* Si decidimos dedicar tiempo\, para identificar los autores\, podemos
* Del volcado de memoria\, obtener las conexiones abiertas: IPs origen\, teniendo en cuenta que puede estar falseada\.
* Hay que ser crítico con la información que se obtiene\, no siempre se obtendrá éxito a la primera\, será difícil averiguar el origen del incidente\.
* Recapacitar en los perfiles de atacantes\, para mimetizarse y entender quién pudo ser el autor:
  * Org\. criminales con ánimo de lucro\, buscan robar información y sacar rendimiento
  * Quien busca prestigio y reconocimiento en el ambiente: publicando su fechoría\.

#### Impacto causado

* No hay un método único para obtener esta información\. Puedes usar BIA \(Business Impact Analysis\) para determinar el impacto de ciertos eventos ayudando a valorar los daños económicos\. Estos podrán tener asociado:
* __gastos __  __económicos__ \, que habrá que cuantificar en función de los ítems afectados\.
  * Fácil cálculo: Estos gastos resultará de reemplazar una máquina o dispositivo que quedó inservible tras el ataque\, o las horas de reinstalación de un sistema\.
  * Difícil cálculo\.También pueden deberse por el robo de información de secreto industrial que habrá que cuantificar\, ya que la empresa se verá afectada a largo plazo\.
* Otros\, que posiblemente también supondrán un problema económico\.
  * tiempo de inactividad de oficinas y fábricas\, que dejarán de realizar su trabajo\.

#### Herramientas

TODO

#### Bibliografía

_[UNE 71506 \- Metodología para el análisis forense de evidencia electrónica](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/resource/view.php?id=528409)_

_[Metodologías para un análisis forense](http://openaccess.uoc.edu/webapps/o2/bitstream/10609/39681/6/cgervillarTFM1214memoria.pdf)_

_[https://www\.incibe\-cert\.es/blog/rfc3227](https://www.incibe-cert.es/blog/rfc3227)_

_[https://www\.ra\-ma\.es/libro/gestion\-de\-incidentes\-de\-ciberseguridad\_139033/](https://www.ra-ma.es/libro/gestion-de-incidentes-de-ciberseguridad_139033/)_

#### Actividad

#### Actividad II

Recopilación y análisis de evidencias sobre un incidente:

<span style="color:#005591"> _[3\.abc\.01 \- Recolección\, almacenamiento y análisis](https://educacionadistancia.juntadeandalucia.es/centros/cadiz/mod/assign/view.php?id=542235)_ </span>

![](assets/IS-U321-AnalisisDeEvidenciasEInvestigacionDeIncidentes1.png)

#### 

