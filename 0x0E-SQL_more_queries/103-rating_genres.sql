-- this scripts list all genres in the database by their rating
-- each record should display tv_genres.name and rating sum
-- result must be sorted in descending order by their rating
-- you can only use select statement

SELECT tv_genres.name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
