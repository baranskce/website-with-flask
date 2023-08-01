DROP TABLE IF EXISTS songs;
DROP TABLE IF EXISTS my_playlist;

CREATE TABLE songs (
    song VARCHAR(50) NOT NULL,
    artist VARCHAR(50) NOT NULL,
    albüm VARCHAR(50)
);

CREATE TABLE my_playlist (
    song VARCHAR(50) NOT NULL,
    artist VARCHAR(50) NOT NULL,
    albüm VARCHAR(50)
);