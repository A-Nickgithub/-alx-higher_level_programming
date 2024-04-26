#!/usr/bin/python3
"""
This module connects to the database at localhost throught
port 3306 and filters the table states by listing the states that
starts with the letter "N"
and orders them by id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database,
        port=3306
        )

    cur = db.cursor()
    cur.execute("SELECT DISTINCT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    query_results = cur.fetchall()
    for row in query_results:
        print(row)

    cur.close()
