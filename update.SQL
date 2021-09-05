\timing on
UPDATE casti
SET name='Carlos'
WHERE id = 50000;
\timing on
UPDATE crew
SET name='Carlos'
WHERE id = 50000;
\timing on
UPDATE genero
SET name='Aburridas'
WHERE id = 50000;
\timing on
UPDATE metadata
SET title='Las Gamesa'
WHERE id = 50000;
\timing on
UPDATE asociacion_genero_movies
SET id_gen=50000
WHERE id_movie = 70000;