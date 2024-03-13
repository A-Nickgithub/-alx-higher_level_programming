-- write a script that lists all genres from the database and displays the number of shows linked to each genree
-- first column must be called genre
-- second column must be called number of shows
-- don't display any genre that does not have any show linked
-- result must be sorted in descending order
-- you can only use one select statement

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
