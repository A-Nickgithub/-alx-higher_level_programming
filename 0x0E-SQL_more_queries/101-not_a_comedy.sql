-- write a script that list all shows without the genre comedy in the database

SELECT tv_shows.title
FROM tv_shows
LEFT JOIN
  (SELECT DISTINCT tv_shows.id
	   FROM tv_shows
	   JOIN tv_genres
	   ON tv_shows.id = tv_genres.id
	   WHERE tv_genres.name = 'Comedy') AS comedy_shows
ON tv_shows.id = comedy_shows.id
WHERE comedy_shows.id IS NULL
ORDER BY tv_shows.title;
