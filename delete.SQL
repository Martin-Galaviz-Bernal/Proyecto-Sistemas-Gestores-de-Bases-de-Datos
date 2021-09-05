\timing on
DELETE FROM casti
WHERE id=50000;

\timing on
DELETE FROM crew
WHERE id=50000;

\timing on
DELETE FROM genero
WHERE id=50000;

\timing on
DELETE FROM metadata
WHERE id=50000;

\timing on
DELETE FROM asociacion_genero_movies
WHERE id_gen=50000;