#!/usr/bin/python3
"""
This script joins the cities and states
table to produce a city with their repective state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    )

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
