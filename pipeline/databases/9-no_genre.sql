-- List all shows contained in hbtn_0d_tvshows
-- without a genre linked
SELECT 
    a.title,
    b.genre_id
FROM tv_shows a
LEFT JOIN tv_show_genres b on b.show_id = a.id
WHERE b.genre_id IS NULL
ORDER BY 1,2
;