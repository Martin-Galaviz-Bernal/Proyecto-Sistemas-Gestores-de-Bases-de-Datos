\timing on
SELECT name
FROM(
    SELECT name, COUNT(name) as nombres
    FROM metadata,crew
    WHERE metadata.id=crew.id_movie AND job='Director' 
    GROUP BY name
    ORDER by nombres DESC
    limit 1) subconsulta
    ;