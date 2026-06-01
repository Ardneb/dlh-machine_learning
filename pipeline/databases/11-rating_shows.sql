-- List all shows from hbtn_0d_tvshows_rate 
-- by their rating
SELECT 
    a.title,
    SUM(b.rate) AS 'rating sum'
FROM tv_shows a
INNER JOIN tv_show_ratings b ON b.show_id = a.id
GROUP BY a.title
ORDER BY 2 DESC
;