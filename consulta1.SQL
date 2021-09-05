\timing on
SELECT genero.name,COUNT(genero.name) as numero
FROM genero,asociacion_genero_movies
WHERE genero.id=asociacion_genero_movies.id_gen 
GROUP BY genero.name;
