-- Genre ID by show
-- Import the database, write a script that lists all shows
SELECT title, genre_id FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id=tv_show_genres.show_id
ORDER BY title, genre_id
