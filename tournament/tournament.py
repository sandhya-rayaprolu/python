#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname=tournament")
        cursor = db.cursor()
        return db,cursor
    except:
        print("Error. Unable to connect to database.")



def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor.execute('DELETE from matches')
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute('DELETE from players')
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    cursor.execute('SELECT COUNT(*) FROM players')
    row = cursor.fetchone()
    db.close()
    return row[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    db, cursor = connect()
    cursor.execute('INSERT INTO players (name) VALUES (%s)', (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    """The view standings has the data needed in the correct format
    So, we retrieve all the data from view and return it
    """
    db, cursor = connect()
    cursor.execute('SELECT * from standings')
    rows = cursor.fetchall()
    db.close()
    return rows


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db,cursor = connect()
    cursor.execute(
        'INSERT INTO matches (winner, loser) VALUES (%s,%s)', (winner, loser,))
    db.commit()
    db.close()


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

    """Get each player's id and name, and since the view standings has
    the players ordered by wins, just pair them with the next player.
    This will get the players with the same/closest number of wins to pair up
    """

    db, cursor = connect()
    cursor.execute('SELECT id,name from standings')
    standings = cursor.fetchall()
    db.close()
    if len(standings)%2 != 0:
        print("Number of players not even, cannot pair them.")
        return
    pairings = []
    i = 0
    while i < len(standings):
        pairings.append(standings[i] + standings[i+1])
        i += 2
    return pairings
