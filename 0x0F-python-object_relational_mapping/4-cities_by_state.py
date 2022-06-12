#!/usr/bin/python3
"""
states module
"""


import MySQLdb
import sys


def cities_states():
    """"
    lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states ON\
            cities.state_id = states.id ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    cities_states()
