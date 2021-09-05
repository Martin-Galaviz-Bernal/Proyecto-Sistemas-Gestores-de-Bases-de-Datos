--Crearemos las tablas de nuestra base de datos

--Tabla para cast.csv
CREATE TABLE casti
(
    id          INTEGER,
    name        CHAR(50),
    id_movie    INTEGER
);

--Tabla para crew.csv
CREATE TABLE crew
(
    id          INTEGER,
    name        CHAR(50),
    job         CHAR(60),
    id_movie    INTEGER
);

--Tabla para genero.csv
CREATE TABLE genero
(
    id          INTEGER not null,
    name        CHAR(16)
);

--Tabla para metadata.csv
CREATE TABLE metadata
(
    id              INTEGER not null,
    title           CHAR(110),
    original_title  CHAR(110),
    vote_average    FLOAT,
    vote_counts     FLOAT
);

--Tabla para asociacion_genero_movies.csv
CREATE TABLE asociacion_genero_movies
(
    id_gen  	INTEGER,
    id_movie    INTEGER
);
