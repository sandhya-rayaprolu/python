Code for Udacity Full Stack Developer Nanodegree - Project 2 - Swiss Pairings
==============================================================================
Python and SQL code for pairing up players based on the Swiss pairing system

tournament.sql file contains the code to create the tournament database, 
with the players and matches tables, we also use a view called standings 
for generating the player standings, and this is also created here.
This file needs to be run first, before executing any python code.

tournament.py file contains the code to add/delete/modify/view data in the 
player and matches tables. The functions in this file are defined by Udacity
and the code inside the functions is coded by students like me.

tournament_test.py file contains the tests to check if tournament.py is
behaving properly. This file is provided by Udacity

To Run
=======
1. Execute the tournament.sql file to create the database and tables
2. Execute the tournament_test.py to test whether tournament.py correctly
   adds/deletes players, registers match results, generates player standings
   and pairs up the players with the closest number of wins.


