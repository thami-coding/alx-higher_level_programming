#!/usr/bin/python3
""" script that lists all states from
    the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    pattern = sys.argv[4]
    db = MySQLdb.connect(user=username, passwd=password, db=database,
                         host="localhost", port=3306)
    c = db.cursor()
    c.execute(
                """
                SELECT * FROM states
                WHERE BINARY name = '{}'
                ORDER BY states.id
                """.format(pattern)
             )

    for row in c.fetchall():
        print(row)
