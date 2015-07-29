-- Table definitions for the tournament project.

-- Drop the database and all the tables and views in it if they already exists
DROP DATABASE tournament;
CREATE DATABASE tournament;

-- Connect to the tournament database
\c tournament;

-- Table to hold the player data
CREATE TABLE players (
     id    serial PRIMARY KEY,
     name   text NOT NULL
);

-- Table to hold the match data
CREATE TABLE matches (
     id       serial PRIMARY KEY,
     winner   int references players(id),
     loser    int references players(id)
);

-- View to hold the Standings data formatted as needed
CREATE VIEW standings (id,name,wins,matches) AS
    SELECT players.id AS id, 
           players.name AS name,
           (SELECT COUNT(*) from matches WHERE players.id = winner) AS wins,
           (SELECT COUNT(*) from matches WHERE players.id = winner OR 
            players.id=loser) AS matches FROM players ORDER BY wins DESC;


