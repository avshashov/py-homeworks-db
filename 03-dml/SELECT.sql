SELECT *
FROM albums
WHERE EXTRACT(YEAR FROM release_date) = 2018;


SELECT track_name, duration
FROM tracks
WHERE duration = (SELECT max(duration)
                    FROM tracks);
                    
                
SELECT track_name, duration
FROM tracks
WHERE duration >= '00:03:30';


SELECT collection_name
FROM music_collections
WHERE EXTRACT(YEAR FROM release_date) BETWEEN 2018 AND 2020;


SELECT performer_name 
FROM performer
WHERE performer_name NOT LIKE '% %';


SELECT track_name 
FROM tracks
WHERE track_name LIKE '%My%' OR track_name LIKE '%Мой%';


