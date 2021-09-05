\timing on
INSERT INTO casti(id,name,id_movie)
    VALUES
            (50000,'Martin Galaviz',12345);
--\timing on
INSERT INTO crew(id,name,job,id_movie)
    VALUES
            (50000,'Martin Galaviz','Camarografo',12345);
--\timing on
INSERT INTO genero(id,name)
    VALUES
            (50000,'Rancheras');
--\timing on
INSERT INTO metadata(id,title,original_title,vote_average,vote_counts)
    VALUES
            (50000,'Galletas','Las Oreo',8.6,1234);
--\timing on
INSERT INTO asociacion_genero_movies(id_gen,id_movie)
    VALUES
            (50000,60000);