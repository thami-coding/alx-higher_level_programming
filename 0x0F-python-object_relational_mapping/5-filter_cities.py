#!/usr/bin/python3
"""
script that takes in the name of a state as
an argument and lists all cities of that state
"""


import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv)-1 == 4:
        state = sys.argv[4]
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], port=3306)
        c = db.cursor()
        c.execute(
                """
                SELECT
                name
                FROM cities
                WHERE cities.state_id =
                (
                SELECT id
                FROM states
                WHERE BINARY name = '{}'
                ORDER BY cities.id ASC
                LIMIT 1
                )
                """.format(state)
                )
        cities = c.fetchall()
        num_cities = len(cities)-1
        i = 0
        for city in cities:
            if i != num_cities:
                print(city[0], end=', ')
                i += 1
            else:
                print(city[0])
