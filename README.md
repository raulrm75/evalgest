evalgest
========

Objetivos
---------
* Construir una proyecto django para gestionar de manera distribuida aspectos relacionados con el proceso de evaluación del alumnado.
* Se van a implementar las siguientes aplicaciones:
    * preeval: para gestionar las preevaluaciones (prenotas).
    * calcompe: para calcular la calificación de las competencias básicas a partir de las calificaciones de las evaluaciones ordinaria o extraordinaria.

ToDo (preeval)
--------------
* [X] Crear esqueleto django.
* [X] Crear modelos.
* [X] Añadir interfaz admin a los modelos.
* [ ] Modificar interfaz admin de datos para carga masiva desde Séneca.
* [ ] Diseñar estructura url y vistas asociadas.
* [ ] Crear la estructura url y las vistas asociadas.
* [ ] Añadir vistas para generar los informes de preevaluación.
* [ ] Añadir distintos permisos para cada perfil: profesor, tutor, directivo y administrador (de menos a más "poderes").
* [ ] Modificar para usar datos MySQL
* [ ] Colocar en servidor de producción.
* [ ] Crear opciones para crear y restaurar copias de seguridad de los datos.
