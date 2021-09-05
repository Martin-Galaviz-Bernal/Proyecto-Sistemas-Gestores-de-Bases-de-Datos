\timing on
SELECT title
FROM metadata
WHERE vote_counts= (
    SELECT vote_counts
    FROM metadata
    ORDER BY vote_counts DESC
    limit 1)
;

