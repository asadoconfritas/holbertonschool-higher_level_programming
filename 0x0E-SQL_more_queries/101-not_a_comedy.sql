-- No Comedy tonight!
-- script that lists all shows without the genre Comedy
SELECT title FROM tv_shows
WHERE title NOT IN(
	SELECT title FROM tv_shows
	JOIN tv_show_genres ON tv_shows.id=tv_show_genres.show_id
	JOIN tv_genres ON tv_show_genres.genre.id=tv_genres.id
	WHERE tv_genres.name='Comedy'
	ORDER BY title)
ORDER BY title ASC
