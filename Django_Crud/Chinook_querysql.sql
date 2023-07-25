-- Seleccionar todos los Géneros
SELECT * FROM "Genre";
SELECT * FROM "Album";
SELECT * FROM "Artist";
SELECT * FROM "Customer";
SELECT * FROM "Employee";
SELECT * FROM "Invoice";
SELECT * FROM "InvoiceLine";
SELECT * FROM "MediaType";
SELECT * FROM "Playlist";
SELECT * FROM "PlaylistTrack";
SELECT * FROM "Track";


-- La canción más larga
SELECT "TrackId", "Name", "Milliseconds" FROM "Track" ORDER BY "Milliseconds" DESC LIMIT 1;

-- Listar todos los albumes de audioslave con nombre de la banda y nombre del albúm .
SELECT a."ArtistId", a."Name", al."Title" FROM "Artist" a
JOIN "Album" al ON a."ArtistId" = al."ArtistId"
WHERE a."Name" = 'Audioslave';


-- Listar todas las canciones por album de metalica monstrando nombre de la banda, nombre del album, nombre de la cancion
-- género y duración en minutos.
SELECT a."Name" AS "Nombre de la banda", al."Title" AS "Nombre del albúm", t."Name" AS "Nombre de la Canción", g."Name" AS "Género", t."Milliseconds" AS "Duración"
FROM "Artist" a
JOIN "Album" al ON a."ArtistId" = al."ArtistId"
JOIN "Track" t ON al."AlbumId" = t."AlbumId"
JOIN "Genre" g ON t."GenreId" = g."GenreId"
WHERE a."Name" = 'Metallica';

-- La banda con la mayor cantidad de álbumes
SELECT a."ArtistId", a."Name", COUNT(al."AlbumId") AS "Cantidad de álbumes"
FROM "Artist" a
JOIN "Album" al ON a."ArtistId" = al."ArtistId"
GROUP BY a."ArtistId", a."Name"
ORDER BY "Cantidad de álbumes" DESC
LIMIT 1;