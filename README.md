# Django_Crud
Renderizando contenido dinámico desde una base de datos PostgreSQL

Se obtienen datos de una base de datos preconstruida en postgresql, conecto django con psql.
Realizo querys solicitadas en pg admin4.
Se crea la vista principal para 'index.html' en la cuál se entregan los datos de los models Artist, Album, Track para lograr
mostrar en un select todos los artistas contenidos en la base de datos.
Al seleccionar una de las bandas el id es recibido por la views y realiza dos filtros para encontrar los albums de dicha banda y cada canción de cada album.

Esto se realiza a traves de lógica en la views
