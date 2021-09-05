\timing on
SELECT subconsulta.name
FROM(
    SELECT name, COUNT(name) AS total
            FROM casti
            GROUP BY name
            ORDER BY total DESC
            limit 1 ) subconsulta
;
