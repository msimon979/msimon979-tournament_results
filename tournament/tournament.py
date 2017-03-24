#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    sql = "DELETE FROM matches"
    c.execute(sql)
    DB.commit()
    DB.close


def deletePlayers():
    """Remove all the player records from the database."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    sql = "DELETE FROM players"
    c.execute(sql)
    DB.commit()
    DB.close


def countPlayers():
    """Returns the number of players currently registered."""
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    sql = "SELECT count(*) FROM players"
    c.execute(sql)
    count = c.fetchone()
    DB.close
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    sql = "insert into players(name) values ('%s')" % name
    c.execute(sql)
    DB.commit()
    DB.close


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    sql = "SELECT * FROM standings"
    c.execute(sql)
    count = c.fetchall()
    DB.close
    return count


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    sql = "INSERT INTO matches(winner, loser) VALUES (%s, %s)" % (winner,loser)
    c.execute(sql)
    DB.commit()
    DB.close


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = psycopg2.connect("dbname=tournament")
    c = DB.cursor()
    c.execute("select id from standings order by Wins;")
    ids = c.fetchall()
    c.execute("select p.name from players p join standings s on p.id = s.id order by wins;")
    names = c.fetchall()
    standings = playerStandings()

    pair1 = zip(ids[0],names[0], ids[1], names[1])
    pair2 = zip(ids[2],names[2], ids[3],names[3])
    pair3 = zip(ids[4],names[4], ids[5],names[5])
    pair4 = zip(ids[6],names[6], ids[7],names[7])

    tuples = pair1 + pair2 + pair3 + pair4
    return tuples
    DB.close


