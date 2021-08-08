#!/usr/bin/python3
"""
states module
"""


import MySQLdb
import sys


def create_states():
    """"
    creates a states table
    in hbtn_0e_0_usa with some data
    module
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    create_states()
