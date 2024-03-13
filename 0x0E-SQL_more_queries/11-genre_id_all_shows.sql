-- this script will list all shows in the database hbtn_0d_tvshows
-- each record should display tv_shows.title, and tv_show_genres.genre_id
-- if a show does not have a genre display NULL
-- You can only use one select statement

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres 
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id
