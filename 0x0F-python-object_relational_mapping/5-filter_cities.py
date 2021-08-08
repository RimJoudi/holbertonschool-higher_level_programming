#!/usr/bin/python3
"""
states module
"""


import MySQLdb
import sys


def listcity_states():
    """"
    lists all cities of that state, using the database hbtn_0e_4_usa
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searchstate = sys.argv[4]
    cities = []

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    WHERE states.name=%s
    ORDER BY id ASC""", (searchstate,))
    rows = cur.fetchall()
    for row in rows:
        cities.append(row[1])
    print(', '.join(cities))
    cur.close()
    db.close()


if __name__ == "__main__":
    listcity_states()
