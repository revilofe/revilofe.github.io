---
title: "UD 5 - 5.2 Diagrama de clases"
description: Introducción al Lenguaje Unificado de Modelado (UML).
summary: Conoce qué es UML, sus características principales, tipos de diagramas y más.
authors:
    - Eduardo Fdez
date: 2024-11-27
icon: "material/file-document-outline"
permalink: /prog/unidad5/5.1
categories:
    - EDES
    - Modelado
tags:
    - UML
    - Diagramas
    - Software
---
## 5.2 Diagrama dec lases
Antes de programar una aplicación, es importante tener una idea clara de cómo se estructurará el sistema. Para ello, se utilizan diagramas de clases, que permiten visualizar las clases y sus relaciones en un sistema de información. A continuación, se describen los elementos que componen un diagrama de clases y cómo se representan.

### 1. Introducción
El **diagramade clases ** es uno de los diagramas incluidos en UML 2.5 clasificado dentro de los diagramas de estructura y, como tal, se utiliza para representar los elementos que componen un sistema de información desde un punto devista estático.

Esimportante destacar que, por esta misma razón, este diagrama noincluye la forma en la que se comportan a lo largo de la ejecuciónlos distintos elementos, esa función puede ser representada a travésde un diagrama de comportamiento, como por ejemplo un [diagramade secuencia](https://diagramasuml.com/secuencia/)oun [diagramade casos de uso](https://diagramasuml.com/casos-de-uso/).

El diagrama de clases es un **diagrama puramente orientado al modelo de programación orientado a objetos**,ya que define las clases que se utilizarán cuando se pase a la fase de construcción y la manera en que se relacionan las mismas. Se podría equiparar, salvando las distancias, al famoso diagrama de modelo Entidad-Relación (E/R), no recogido en UML, ya que tiene una utilidad similar: la representación de datos y su interacción. Ambos diagramas muestran el modelo lógico de los datos de unsistema.

El diagrama UML de clases está formado por dos elementos: clases,relaciones e interfaces.


### 1. Clases

Las clases son el elemento principal del diagrama y representa, como sunombre indica, una clase dentro del paradigma de la orientación aobjetos. Este tipo de elementos normalmente se utilizan pararepresentar conceptos o entidades del «negocio». Una clase defineun **grupode objetos **quecomparten características, condiciones y significado. La manera másrápida para encontrar clases sobre un enunciado, sobre una idea denegocio o, en general, sobre un tema concreto es buscar los**sustantivos**queaparecen en el mismo. Por poner algún ejemplo, algunas clasespodrían ser: Animal, Persona, Mensaje, Expediente… Es un conceptomuy amplio y **resultafundamental identificar de forma efectiva estas clases**,en caso de no hacerlo correctamente se obtendrán una serie deproblemas en etapas posteriores, teniendo que volver a hacer elanálisis y perdiendo parte o todo el trabajo que se ha hecho hastaese momento.

Bajandode nivel una clase está compuesta por tres elementos: **nombrede la clase, atributos, funciones. Estos elementos se incluyen en larepresentación **(ono, dependiendo del nivel de análisis).

Pararepresentar la clase con estos elementos se utiliza una caja que esdividida en tres zonas utilizando paraello lineas horizontales:

* La	primera de las zonas se utiliza para el nombre de la	clase. En caso de que la clase sea abstracta se utilizará su	nombre en cursiva.
* La	segunda de las zonas se utiliza para escribir los atributos	de la clase, uno por línea y utilizando el siguiente formato:

*visibilidadnombre_atributo : tipo = valor-inicial { propiedades }*

Aunqueesta es la forma «oficial» de escribirlas, es común simplificandoúnicamente poniendo el nombre y el tipo o únicamente el nombre.

* La	última de las zonas incluye cada una de las funciones que	ofrece la clase. De forma parecida a los atributos, sigue el	siguiente formato:

*visibilidadnombre_funcion { parametros } : tipo-devuelto { propiedades }*

Dela misma manera que con los atributos, se suele simplificar indicandoúnicamente el nombre de la función y, en ocasiones, el tipodevuelto.

Tantolos atributos como las funciones incluyen al principio de sudescripción la visibilidad que tendrá. Esta visibilidad seidentifica escribiendo un símbolo y podrá ser:

* **(+)	Pública. **Representa	que se puede acceder al atributo o función desde cualquier lugar de	la aplicación.
* **(-)	Privada. **Representa	que se puede acceder al atributo o función únicamente desde la	misma clase.
* **(#)	Protegida. **Representa	que el atributo o función puede ser accedida únicamente desde la	misma clase o desde las clases que hereden de ella (clases	derivadas).

Estostres tipos de visibilidad son los más comunes. No obstante, puedenincluirse otros en base al lenguaje de programación que se estéusando (no es muy común). Por ejemplo: (/) Derivado o (~) Paquete.

Unejemplo de clase podría ser el siguiente:

Encaso de que un atributo o función sea estático, se representa en eldiagrama subrayando su nombre. Una característica estática sedefine como aquella que es compartida por cada clase y no instanciadapara cada uno de los objetos de esa clase. Es un concepto muy común.

#### 2. Relaciones

Unarelación i**dentificauna dependencia**.Esta dependencia puede ser entre dos o más clases (más común) ouna clase hacía sí misma (menos común, pero existen), este últimotipo de dependencia se denomina *dependenciareflexiva*.Las relaciones se representan con una linea que une las clases, estalínea variará dependiendo del tipo de relación

Lasrelaciones en el diagrama de clases tienen varias propiedades, quedependiendo la profundidad que se quiera dar al diagrama serepresentarán o no. Estas propiedades son las siguientes:

* **Multiplicidad**.	Es decir, el número de elementos de una clase que participan en una	relación. Se puede indicar un número, un rango… Se utiliza*n	*o	* para identificar un número cualquiera.
* **Nombre	de la asociación. **En	ocasiones se escriba una indicación de la asociación que ayuda a	entender la relación que tienen dos clases. Suelen utilizarse	verbos como por ejemplo: «Una empresa contrata a n empleados»

#### Tiposde relaciones

Undiagrama de clases incluye los siguientes tipos de relaciones:

* **Asociación.**
* **Agregación.**
* **Composición.**
* **Dependencia.**
* **Implementación.**
* **Herencia.**

##### Asociación

Estetipo de relación es el más común y se utiliza para representardependencia semántica. Se representa con una simple linea continuaque une las clases que están incluidas en la asociación.

Unejemplo de asociación podría ser: «Una mascota pertenece a unapersona».

##### Agregación

Esuna representación jerárquica que indica a un objeto y las partesque componen ese objeto. Es decir, representa relaciones en las que**unobjeto es parte de otro**,pero aun así debe tener **existenciaen sí mismo**.

Serepresenta con una línea que tiene un rombo en la parte de la claseque es una agregación de la otra clase (es decir, en la clase quecontiene las otras).

Unejemplo de esta relación podría ser: «Las mesas están formadaspor tablas de madera y tornillos o, dicho de otra manera, lostornillos y las tablas forman parte de una mesa». Como ves, eltornillo podría formar parte de más objetos, por lo que interesaespecialmente su abstracción en otra clase.

##### Composición

Lacomposición es similar a la agregación, representa una **relaciónjerárquica entre un objeto y las partes que lo componen**,**perode una forma más fuerte**.En este caso, los elementos que forman parte no tienen sentido deexistencia cuando el primero no existe. Es decir, cuando el elementoque contiene los otros desaparece, deben desaparecer todos ya que notienen sentido por sí mismos sino que dependen del elemento quecomponen. Además, suelen tener los mismos tiempo de vida. Loscomponentes no se comparten entre varios elementos, esta es otra delas diferencias con la agregación.

Serepresenta con una linea continua con un rombo relleno en la claseque es compuesta.

Unejemplo de esta relación sería: «Un vuelo de una compañía aéreaestá compuesto por pasajeros, que es lo mismo que decir que unpasajero está asignado a un vuelo»

###### Diferenciaentre agregación y composición

Ladiferencia entre agregación y composición es semántica, por lo que**aveces no está del todo definida**.Ninguna de las dos tienen análogos en muchos lenguajes deprogramación (como por ejemplo Java).

Un«agregado» representa **untodo que comprende varias partes**;de esta manera, un Comité es un agregado de sus Miembros. Unareunión es un agregado de una agenda, una sala y los asistentes. Enel momento de la implementación, esta relación no es de contención.(Una reunión no contiene una sala). Del mismo modo, las partes delagregado podrían estar haciendo otras cosas en otras partes delprograma, por lo que podrían ser referenciadas por varios objetosque nada tienen que ver. En otras palabras, no existe una diferenciade nivel de implementación entre la agregación y una simplerelación de «usos». En ambos casos, un objeto tiene referencias aotros objetos. Aunque no existe una diferencia en la implementación,definitivamente vale la pena capturar la relación en el diagramaUML, tanto porque ayuda a comprender mejor el modelo de dominio, comoporque puede haber problemas de implementación que pueden pasardesapercibidos. Podría permitir relaciones de acoplamiento másestrictas en una agregación de lo que haría con un simple «uso»,por ejemplo.

Lacomposición, por otro lado, implica u**nacoplamiento aún más estricto que la agregación**,y definitivamente implica la contención. El requisito básico esque, si una clase de objetos (llamado «contenedor») se compone deotros objetos (llamados «elementos»), entonces los elementosaparecerán y también serán destruidos como un efecto secundario decrear o destruir el contenedor. Sería raro que un elemento no sedeclare como privado. Un ejemplo podría ser el nombre y la direccióndel Cliente. Un cliente sin nombre o dirección no tiene valor. Porla misma razón, cuando se destruye al cliente, no tiene sentidomantener el nombre y la dirección. (Compare esta situación con laagregación, donde destruir al Comité no debe causar la destrucciónde los miembros, ya que pueden ser miembros de otros Comités).

##### Dependencia

Seutiliza este tipo de relación para **representarque una clase requiere de otra para ofrecer sus funcionalidades**.Es muy sencilla y se representa con una flecha discontinua que vadesde la clase que necesita la utilidad de la otra flecha hasta estamisma.

Unejemplo de esta relación podría ser la siguiente:

##### Herencia

Otrarelación muy común en el diagrama de clases es la herencia. Estetipo de relaciones permiten que**unaclase****(clasehija o subclase) reciba los atributos y métodos de otra clase****(clasepadre o superclase)**.Estos atributos y métodos recibidos se suman a los que la clasetiene por sí misma. Se utiliza en relaciones «es un».

Unejemplo de esta relación podría ser la siguiente: Un pez, un perroy un gato son animales.

Eneste ejemplo, las tres clases (Pez, Perro, Gato) podrán utilizar lafunción respirar, ya que lo heredan de la clase animal, perosolamente la clase Pez podrá nadar, la clase Perro ladrar y la claseGato maullar. La clase Animal podría plantearse ser definidaabstracta, aunque no es necesario.

### Implementaciónde Interfaces

Unainterfaz es una entidad que declara una **seriede atributos, funciones y obligaciones. **Esuna especie de contrato donde toda instancia asociada a una interfazdebe de implementar los servicios que indica aquella interfaz.

Dadoque únicamente son declaraciones **nopueden ser instanciadas**.

Surepresentación es similar a las clases, pero indicando arriba lapalabra <<interface>>.

Lasinterfaces se asocian a clases. Una asociación entre una clase y unainterfaz representa que esa clase cumple con el contrato que indicala interfaz, es decir, incluye aquellas funciones y atributos queindica la interfaz. Portanto, esta es la últimarelación,y representa la implementación de esa interfaz por una clase. Estetipo de relaciones permiten que**unaclase****acepteel contrato definidos por ****losatributos y métodos de ****la****interfaz**.Estos atributos y métodos aceptadosdesde la interfaz deben implementarse y darle uso en la clase.Se utiliza en relaciones «Implementa»yse representa como se indica en el siguiente ejemplo:

## Cómodibujar un diagrama de clases

Losdiagramas de clase van de la mano con el diseño orientado a objetos.Por lo tanto, saber lo básico de este tipo de diseño es una parteclave para poder dibujar diagramas de clase eficaces.

Estetipo de diagramas son solicitados cuando se está describiendo lavista estática del sistema o sus funcionalidades. Unos pequeñospasos que puedes utilizar de guía para construir estos diagramas sonlos siguientes:

* **Identifica	**los	nombres de las clase
  El	primer paso es identificar los objetos primarios del sistema. Las	clases suelen corresponder a sustantivos dentro del dominio del	problema.
* **Distingue	**las	relaciones
  El	siguiente paso es determinar cómo cada una de las clases u objetos	están relacionados entre sí. Busca los puntos en común y las	abstracciones entre ellos; esto te ayudará a agruparlos al dibujar	el diagrama de clase.
* **Crea	**la	estructura
  Primero,	agrega los nombres de clase y vincúlalos con los conectores	apropiados, prestando especial atención a la cardinalidad o las	herencias. Deja los atributos y funciones para más tarde, una vez	que esté la estructura del diagrama resuelta.

## Buenasprácticas en la construcción del diagrama de clases

Terecomendamos seguir estas indicaciones o consejos, que, aunque no sonobligatorios, harán que tus diagramas de clases sean de mayorutilidad:

* Los	diagramas de clase **pueden	tender a volverse incoherentes **a	medida que se expanden y crecen. Es mejor evitar la creación de	diagramas grandes y **dividirlos	**en	otros más pequeños que se puedan vincular entre sí más adelante.
* Usando	la notación de clase simple, puedes crear rápidamente **una	visión general de alto nivel **de	su sistema. Se puede crear un diagrama detallado por separado según	sea necesario, e incluso vincularlo al primero para una referencia	fácil.
* Cuantas	más líneas se superpongan en sus diagramas de clase, más	abarrotado se vuelve y, por tanto, más se complica utilizarlo. El	lector se confundirá tratando de encontrar el camino. Asegúrate de	que **no	haya dos líneas cruzadas **entre	sí, a no ser que no haya más remedio.
* Usa	**colores	**para	agrupar módulos comunes. Diferentes colores en diferentes clases	ayudan al lector a diferenciar entre los diversos grupos.

## Ejemplosde diagrama de clases

### Diagramade clases clínica veterinaria

### Diagramade clases zoológico

### Diagramade clases de una tienda

### Diagramade clases gestión de biblioteca

### Diagramade clases centro educativo

### 

### Ejemplode clases para un diagrama de clases de una tienda web

Aquíte dejo un ejemplo de clases con sus atributos que podrías incluiren un diagrama de clases de una tienda online:

1. Usuario:

* idUsuario:		Identificador único del usuario.
* nombre:		Nombre completo del usuario.
* correoElectronico:		Dirección de correo electrónico del usuario.
* contraseña:		Contraseña del usuario.
* dirección:		Dirección de envío del usuario.
* métodoDePago:		Método de pago preferido por el usuario.

2. Producto:

* idProducto:		Identificador único del producto.
* nombre:		Nombre del producto.
* descripción:		Descripción detallada del producto.
* precio:		Precio del producto.
* stock:		Cantidad de unidades disponibles en el inventario.

3. Carrito	de Compras:

* idCarrito:		Identificador único del carrito de compras.
* productos:		Lista de productos que el usuario ha añadido al carrito.
* subtotal:		Monto total del carrito antes de aplicar impuestos y descuentos.
* impuestos:		Monto total de impuestos aplicados al carrito.

4. Orden	de compra:

* idOrden:		Identificador único de la orden de compra.
* productos:		Lista de productos comprados en la orden.
* subtotal:		Monto total de la orden antes de aplicar impuestos y descuentos.
* impuestos:		Monto total de impuestos aplicados a la orden.
* envío:		Monto del costo de envío de la orden.
* total:		Monto total de la orden incluyendo impuestos, descuentos y costo de		envío.

5. Categoría:

* idCategoría:		Identificador único de la categoría.
* nombre:		Nombre de la categoría.

6. Comentarios:

* idComentario:		Identificador único del comentario.
* producto:		Identificador del producto al que se refiere el comentario.
* usuario:		Identificador del usuario que escribió el comentario.
* comentario:		Contenido del comentario.
* fecha:		Fecha de creación del comentario.


## Fuente

Las fuentes utilizadas para desarrollar este contenido incluyen:

* [Página de diagramas UML](https://diagramasuml.com/)
* [Lista de herramientas UML](https://diagramasuml.com/herramientas-online/)
