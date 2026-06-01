-- List all genres from hbtn_0d_tvshows and 
-- display the number of shows linked to each
SELECT 
    c.name AS genre,
    COUNT(DISTINCT a.id) AS number_of_shows
FROM hbtn_0d.tv_shows a
INNER JOIN hbtn_0d.tv_shows_genres b ON b.show_id = a.id
INNER JOIN hbtn_0d.tv_genres c ON c.id = b.genre_id
GROUP BY c.name
ORDER BY 2 DESC
;