SELECT genre_name, COUNT(performer_id)
FROM genre
         JOIN genre_performers USING (genre_id)
GROUP BY genre_name;


SELECT COUNT(track_name)
FROM tracks
         JOIN albums USING (album_id)
WHERE EXTRACT(YEAR FROM release_date) IN (2019, 2020);


SELECT album_name, TO_CHAR(AVG(duration), 'MI:SS')
FROM tracks
         JOIN albums USING (album_id)
GROUP BY album_name;


SELECT DISTINCT performer_name
FROM performers
         JOIN album_performers USING (performer_id)
         JOIN albums USING (album_id)
WHERE EXTRACT(YEAR FROM release_date) != 2020;


SELECT collection_name
FROM music_collections
         JOIN collection_tracks USING (id)
         JOIN tracks USING (track_id)
         JOIN albums USING (album_id)
         JOIN album_performers USING (album_id)
         JOIN performers USING (performer_id)
WHERE performer_name = 'Bones';


SELECT album_name
FROM albums
         JOIN album_performers USING (album_id)
         JOIN performers USING (performer_id)
         JOIN genre_performers USING (performer_id)
         JOIN genre USING (genre_id)
GROUP BY album_name
HAVING COUNT(genre_name) > 1;


SELECT track_name
FROM tracks
         LEFT JOIN collection_tracks USING (track_id)
WHERE collection_id IS NULL;


SELECT performer_name, track_name, duration
FROM performers
         JOIN album_performers USING (performer_id)
         JOIN albums USING (album_id)
         JOIN tracks USING (album_id)
WHERE duration = (SELECT MIN(duration)
                  FROM tracks);


SELECT album_name AS Альбом, COUNT(track_name) AS Количество_треков
FROM albums
         JOIN tracks USING (album_id)
GROUP BY album_name
HAVING COUNT(track_name) = (SELECT MIN(Количество_треков)
                            FROM (SELECT COUNT(track_name) AS Количество_треков
                                  FROM tracks
                                  GROUP BY album_id) AS query_in);

