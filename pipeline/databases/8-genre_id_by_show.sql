-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked
SELECT 
    a.title,
    b.genre_id
FROM tv_shows a
INNER JOIN tv_show_genres b on b.show_id = a.id
ORDER BY 1,2
;