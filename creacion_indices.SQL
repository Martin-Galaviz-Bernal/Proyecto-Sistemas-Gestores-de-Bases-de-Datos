\timing on
--Se crean índices para consulta 1
CREATE INDEX  i_asociacion_genero_movies_id_movies on asociacion_genero_movies(id_movie);
CREATE INDEX  i_asociacion_genero_movies_id_gen on asociacion_genero_movies(id_gen);
--ALTER TABLE metadata ADD PRIMARY KEY (id);
--CREATE INDEX i_metadata_id on metadata(id);

--ALTER TABLE genero ADD PRIMARY KEY (id);
--CREATE INDEX i_genero_id on genero(id);


--Índices para consulta 2
CREATE INDEX i_casti_name on casti(name);

--Índices consulta 3
--ALTER TABLE casti ADD PRIMARY KEY (id);
CREATE INDEX  i_casti_id on casti(id);

--Índices consulta 4
CREATE INDEX i_crew_job on crew using hash(job);

CREATE INDEX  i_crew_id_movie on crew(id_movie);

--Índices consulta 5
CREATE INDEX  i_casti_id_movie on casti(id_movie);

--ALTER TABLE crew ADD PRIMARY KEY (id);
CREATE INDEX  i_crew_id on crew(id);

-- Índices consulta 6
CREATE INDEX i_metadata_vote_counts on metadata(vote_counts);

-- Índices consulta 7
CREATE INDEX i_metadata_vote_average on metadata(vote_average);
