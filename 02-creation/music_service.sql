CREATE TABLE genre (
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(30) UNIQUE NOT NULL 
    );


CREATE TABLE performer (
    performer_id SERIAL PRIMARY KEY,
    performer_name VARCHAR(30) UNIQUE NOT NULL
    );


CREATE TABLE genre_performers (
    id SERIAL PRIMARY KEY,
    genre_id INTEGER REFERENCES genre(genre_id),
    performer_id INTEGER REFERENCES performer(performer_id)
    );


CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    album_name VARCHAR(30) NOT NULL,
    release_date DATE
    );

    
CREATE TABLE album_performers (
    id SERIAL PRIMARY KEY,
    performer_id INTEGER REFERENCES performer(performer_id),
    album_id INTEGER REFERENCES albums(album_id)
    );


CREATE TABLE tracks (
    track_id SERIAL PRIMARY KEY,
    track_name VARCHAR(30) NOT NULL,
    album_id INTEGER REFERENCES albums(album_id),
    duration INTEGER 
    );


CREATE TABLE music_collections (
    id SERIAL PRIMARY KEY,
    collection_name VARCHAR(30) NOT NULL,
    release_date DATE,
    track_id INTEGER REFERENCES tracks(track_id)
    );


