--- ПРЕДЫДУЩЕЕ ДЗ

SELECT album_title, year_of_release FROM Album
WHERE year_of_release = 2018;

SELECT track_name, duration FROM track
WHERE duration = (SELECT MAX(duration) FROM track);

SELECT track_name FROM track
WHERE duration > '00:03:30';

SELECT name_collection FROM collection
WHERE year_of_release BETWEEN 2018 AND 2020;

SELECT name_artist FROM artist
WHERE name_artist NOT LIKE '% %';

SELECT track_name FROM track
WHERE track_name LIKE '%Мой%';

-- АКТУАЛЬНОЕ ДЗ

-- 1) количество исполнителей в каждом жанре;
SELECT genre_id, COUNT(*) FROM Genre_Artist
GROUP BY genre_id
ORDER BY COUNT(*) DESC;

-- 2) количество треков, вошедших в альбомы 2017-2018 годов;
SELECT COUNT(track_name) FROM Album a
LEFT JOIN Track t ON a.id = t.album_id
WHERE year_of_release BETWEEN 2017 AND 2018;

-- 3) средняя продолжительность треков по каждому альбому;
SELECT album_id, AVG(duration) FROM Track
GROUP BY album_id
ORDER BY AVG(duration);

-- 4) все исполнители, которые не выпустили альбомы в 2018 году;
SELECT DISTINCT name_artist FROM Artist a
JOIN Artist_Album aa ON a.id = aa.artist_id
JOIN Album al ON al.id = aa.album_id
WHERE al.year_of_release NOT IN (SELECT DISTINCT al.year_of_release FROM Artist a
JOIN Artist_Album aa ON a.id = aa.artist_id
JOIN Album al ON al.id = aa.album_id WHERE al.year_of_release = 2018); 

-- 5) названия сборников, в которых присутствует конкретный исполнитель (Найк Борзов);
SELECT name_collection, name_artist FROM Collection c
JOIN Collection_track ct ON c.id = ct.track_id
JOIN Track t ON ct.track_id = t.id
JOIN Album a ON t.album_id = a.id
JOIN Artist_Album aa ON a.id = aa.album_id
JOIN Artist ar ON aa.artist_id = ar.id 
WHERE name_artist = 'Найк Борзов';

-- 6) название альбомов, в которых присутствуют исполнители более 1 жанра;
SELECT DISTINCT album_title FROM album a 
JOIN Artist_Album aa ON a.id = aa.album_id 
JOIN Genre_Artist ga ON aa.artist_id = ga.artist_id
GROUP BY album_title, ga.artist_id
HAVING COUNT(ga.genre_id) > 1;

-- 7) наименование треков, которые не входят в сборники;
SELECT  track_name FROM Track t
LEFT JOIN Collection_track ct ON t.id = ct.track_id
WHERE ct.collection_id IS NULL;

-- 8) исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
SELECT name_artist, duration FROM Track t
JOIN Artist_Album a ON t.album_id = a.album_id
JOIN Artist ar ON a.artist_id = ar.id
WHERE duration = (SELECT MIN(duration) FROM track);

-- 9) название альбомов, содержащих наименьшее количество треков.
SELECT album_title, COUNT(track_name) FROM Album al
JOIN Track t ON al.id = t.album_id
GROUP BY al.album_title
HAVING COUNT(track_name) = (SELECT COUNT(track_name) FROM Album al
JOIN Track t ON al.id = t.album_id
GROUP BY album_title ORDER BY COUNT(track_name) ASC LIMIT 1);