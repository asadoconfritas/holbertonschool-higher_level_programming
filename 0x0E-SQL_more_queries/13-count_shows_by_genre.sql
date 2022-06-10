-- Number of shows by genre
-- lists all genres and displays the number of shows linked
SELECT g.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres AS g
INNER JOIN tv_show_genres AS s
ON s.genre_id = g.id
GROUP BY g.name
ORDER BY number_of_shows DESC;
