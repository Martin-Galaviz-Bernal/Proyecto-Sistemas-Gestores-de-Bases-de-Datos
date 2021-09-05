\timing on
SELECT metadata.title,genero.name
FROM metadata,asociacion_genero_movies,genero
WHERE 	asociacion_genero_movies.id_gen=genero.id AND 
	asociacion_genero_movies.id_movie=metadata.id
GROUP BY genero.name, metadata.title