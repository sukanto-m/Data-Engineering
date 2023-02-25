# DROP TABLES

SONGPLAY_TABLE_DROP = "DROP TABLE IF EXISTS songplays"
USER_TABLE_DROP = "DROP TABLE IF EXISTS users"
SONG_TABLE_DROP = "DROP TABLE IF EXISTS songs"
ARTIST_TABLE_DROP = "DROP TABLE IF EXISTS artists"
TIME_TABLE_DROP = "DROP TABLE IF EXISTS time"

# CREATE TABLES

SONGPLAY_TABLE_CREATE = (""" CREATE TABLE IF NOT EXISTS songplays
(songplay_id serial PRIMARY KEY, start_time 
TIMESTAMP NOT NULL 
REFERENCES time (start_time), 
user_id INT NOT NULL 
REFERENCES users (user_id), 
level text, song_id text 
REFERENCES songs (song_id), 
artist_id text REFERENCES artists (artist_id), 
session_id INT, location text, user_agent text)
""")

USER_TABLE_CREATE = (""" CREATE TABLE IF NOT EXISTS  
users(user_id  INT PRIMARY KEY, 
first_name text not null, last_name  text not null, 
gender text, level text
)""")

SONG_TABLE_CREATE = (""" CREATE TABLE  IF NOT EXISTS 
songs(song_id text PRIMARY KEY, title  text not null, 
artist_id  text not null, 
year int, duration FLOAT not null)
""")

ARTIST_TABLE_CREATE = (""" CREATE TABLE IF NOT EXISTS artists 
(artist_id text PRIMARY KEY, name text not null, 
location text, latitude float, longitude float)
""")

TIME_TABLE_CREATE = (""" CREATE TABLE IF NOT EXISTS time 
(start_time timestamp NOT NULL PRIMARY KEY, 
hour int NOT NULL, day int NOT NULL, 
week int NOT NULL, month int NOT NULL, 
year int NOT NULL, weekday text NOT NULL);
""")

# INSERT RECORDS

SONGPLAY_TABLE_INSERT = (""" INSERT INTO songplays 
(start_time, user_id, level, song_id, artist_id, session_id, 
location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT (songplay_id) DO NOTHING
""")

USER_TABLE_INSERT = (""" INSERT INTO users 
(user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) 
DO UPDATE SET level = EXCLUDED.level
""")

SONG_TABLE_INSERT = (""" INSERT INTO songs 
(song_id, title, artist_id, year, duration) 
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING
""")

ARTIST_TABLE_INSERT = (""" INSERT INTO artists 
(artist_id, name, location, latitude, longitude) 
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) 
DO UPDATE SET location = EXCLUDED.location, 
latitude = EXCLUDED.latitude, 
longitude = EXCLUDED.longitude
""")


TIME_TABLE_INSERT = (""" INSERT INTO time 
VALUES (%s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = (""" SELECT song_id, artists.artist_id
    FROM songs JOIN artists 
    ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [USER_TABLE_CREATE, SONG_TABLE_CREATE, 
                        ARTIST_TABLE_CREATE, TIME_TABLE_CREATE, 
                        SONGPLAY_TABLE_CREATE]
drop_table_queries = [SONGPLAY_TABLE_DROP, USER_TABLE_DROP, 
                      SONG_TABLE_DROP, ARTIST_TABLE_DROP, 
                      TIME_TABLE_DROP]