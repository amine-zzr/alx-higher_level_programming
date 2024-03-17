-- Select shows with at least one linked genre and display show title and genre ID
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
