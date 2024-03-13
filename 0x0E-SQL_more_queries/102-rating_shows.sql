-- this script lists all the shows from the database by their rating
-- each record shpuld display show.title and rating sum
-- you can only use one select statement

SELECT tv_shows.title, sum(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
