-- No Comedy tonight!
-- script that lists all shows without the genre Comedy
SELECT s.title FROM tv_shows AS s
WHERE s.title NOT IN (
	SELECT s.title FROM tv_shows AS s
	LEFT JOIN tv_show_genres AS sg
	ON sg.show_id = s.id
	LEFT JOIN tv_genres AS g
	ON g.id = sg.genre_id
	WHERE g.name = "Comedy"
)
ORDER BY s.title;
