\timing on
SELECT name
FROM(
    SELECT casti.name,COUNT(casti.name) as frecuencia
    FROM crew,casti,metadata
    WHERE 	casti.id=crew.id AND 
		job='Director' AND 
		casti.id_movie=metadata.id AND 
		crew.id_movie=metadata.id
    GROUP BY casti.name
    ORDER BY frecuencia DESC) subconsulta
;