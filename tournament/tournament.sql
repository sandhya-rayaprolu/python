-- Table definitions for the tournament project.

-- Drop the database and all the tables and views in it if they already exists
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to the tournament database
\c tournament;

-- Table to hold the player data
CREATE TABLE players (
     id    SERIAL PRIMARY KEY,
     name   TEXT NOT NULL
);

-- Table to hold the match data
CREATE TABLE matches (
     id       SERIAL PRIMARY KEY,
     winner   INT references players(id),
     loser    INT references players(id)
);

-- View to hold the Standings data formatted as needed
CREATE VIEW standings (id,name,wins,matches) AS
    SELECT players.id AS id, 
           players.name AS name,
           (SELECT COUNT(*) from matches WHERE players.id = winner) AS wins,
           (SELECT COUNT(*) from matches WHERE players.id = winner OR 
            players.id=loser) AS matches FROM players ORDER BY wins DESC;


