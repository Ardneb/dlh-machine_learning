-- List all genres in the database
-- hbtn_0d_tvshows_rate by their rating.
SELECT 
    c.name,
    SUM(d.rate) AS rating
FROM tv_shows a
INNER JOIN tv_show_genres b ON b.show_id = a.id
INNER JOIN tv_genres c ON c.id = b.genre_id
INNER JOIN tv_show_ratings d ON d.show_id = a.id
GROUP BY c.name
ORDER BY 2 DESC
;