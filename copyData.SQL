\timing on
--Copiar los datos de cast.csv
\COPY casti(id,name,id_movie) FROM ./cast.csv WITH (FORMAT csv, DELIMITER ',',NULL 'NA',HEADER)

--Copiar los datos de crew.csv
\COPY crew(id,name,job,id_movie) FROM ./crew.csv WITH (FORMAT csv, DELIMITER ',',NULL 'NA',HEADER)

--Copiar los datos de genero.csv
\COPY genero(id,name) FROM ./genero.csv WITH (FORMAT csv, DELIMITER ',',NULL 'NA',HEADER)

--Copiar los datos de metadata.csv
\COPY metadata(id,title,original_title,vote_average,vote_counts) FROM ./metadata.csv WITH (FORMAT csv, DELIMITER ',',NULL 'NA',HEADER)

--Copiar los datos de asociacion_genero_movies.csv
\COPY asociacion_genero_movies(id_movie,id_gen) FROM ./asociacion_genero_movies.csv WITH (FORMAT csv, DELIMITER ',',NULL 'NA',HEADER)