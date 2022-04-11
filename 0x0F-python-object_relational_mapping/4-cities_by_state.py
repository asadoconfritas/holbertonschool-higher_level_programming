#!/usr/bin/python3
"""mod doc"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM states \
            JOIN cities \
            ON cities.state_id = states.id \
            ORDER BY cities.id")
    result = cur.fetchall()
    for i in result:
        print(i)
