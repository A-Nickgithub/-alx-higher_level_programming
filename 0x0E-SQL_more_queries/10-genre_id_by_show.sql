-- import databse dump from hbtn_0d_tvshows
-- write a script that lists all shows contained in hbtn_0d_tvshows
-- each record should display tv_show.title and tv_show_genre.genre_id
-- sort in asending order by title and genre_id
-- use only on select statement

SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
