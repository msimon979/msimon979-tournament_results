-- players: name, id, and current tournament
DROP TABLE IF EXISTS players CASCADE;
CREATE TABLE players(
id SERIAL PRIMARY KEY,
name TEXT
);

-- matches: stores the tournament, round, participants and outcome
DROP TABLE IF EXISTS matches CASCADE;
CREATE TABLE matches (
id SERIAL PRIMARY KEY,
winner INT REFERENCES players(id),
loser INT REFERENCES players(id)
);

-- standings: player rankings, including names and # of matches
DROP VIEW IF EXISTS standings;
CREATE VIEW standings AS
SELECT p.id,
    p.name,
    (SELECT COUNT(*) FROM matches m WHERE p.id = m.winner) AS wins,
    (SELECT COUNT(*) FROM matches m WHERE p.id = m.winner OR p.id = m.loser) AS matches
FROM players p
ORDER BY wins DESC;