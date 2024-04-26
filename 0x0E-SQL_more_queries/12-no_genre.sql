-- this script will list all shows contained in hbtn_0d_tvshows without a genre linked
-- each record should display tv_shows.title, tv_shows_genres.genre_id
-- the result must be sorted in ascending order by title and genre_id
-- you can only use one select statement

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
