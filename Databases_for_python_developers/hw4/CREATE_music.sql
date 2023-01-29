CREATE TABLE IF NOT EXISTS Genre (
	id SERIAL PRIMARY KEY,
	genre_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Artist (
	id SERIAL PRIMARY KEY,
	name_artist VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Album (
	id SERIAL PRIMARY KEY,
	album_title VARCHAR(150),
	year_of_release INTEGER NOT NULL CHECK (year_of_release > 1900)
);

CREATE TABLE IF NOT EXISTS Track (
	id SERIAL PRIMARY KEY,
	track_name VARCHAR(150) NOT NULL,
	duration TIME NOT NULL CHECK (duration > '00:00:00' AND duration < '23:59:59'),
	album_id INTEGER NOT NULL REFERENCES Album(id)
);

CREATE TABLE IF NOT EXISTS Genre_Artist (
	genre_id INTEGER REFERENCES Genre(id),
	artist_id INTEGER REFERENCES Artist(id),
	CONSTRAINT pk PRIMARY KEY (genre_id, artist_id)
);

CREATE TABLE IF NOT EXISTS Artist_Album (
	artist_id INTEGER NOT NULL REFERENCES Artist(id),
	album_id INTEGER NOT NULL REFERENCES Album(id),
	CONSTRAINT sk PRIMARY KEY (artist_id, album_id)
);

CREATE TABLE IF NOT EXISTS Collection (
	id SERIAL PRIMARY KEY,
	name_collection VARCHAR(100) NOT NULL,
	year_of_release INTEGER NOT NULL CHECK (year_of_release > 1900)
);

CREATE TABLE IF NOT EXISTS Collection_track (
	track_id INTEGER NOT NULL REFERENCES Track(id),
 	collection_id INTEGER NOT NULL REFERENCES Collection(id),
 	CONSTRAINT rk PRIMARY KEY (track_id, collection_id)
 );