\timing on
SELECT title
FROM metadata
WHERE vote_average=(
    SELECT vote_average
    FROM metadata
    ORDER BY vote_average DESC
    limit 1)
;