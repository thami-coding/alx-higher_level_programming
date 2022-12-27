#!/usr/bin/python3

"""
lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys


if len(sys.argv)-1 == 3:
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    c = db.cursor()

    c.execute(
                """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                """
             )

    for city in c.fetchall():
        print(city)
