\timing on
SELECT title
FROM(
    SELECT metadata.id, COUNT(metadata.id) as titulos
    FROM metadata,casti
    WHERE metadata.id=casti.id_movie
    GROUP BY metadata.id
    ORDER by titulos DESC
    limit 1) subconsulta,
    metadata
WHERE subconsulta.id=metadata.id;
