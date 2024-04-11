#!/usr/bin/python3
"""
This script joins the cities and states
table to produce a city with their repective state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
                "Usage: {} <username> <password> <database> <state_name>"
                .format(sys.argv[0])
                )
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )

    cursor = db.cursor()

    cursor.execute(
        "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities \
        JOIN states ON cities.state_id = states.id WHERE states.name = %s",
        (state_name,)
        )

    cities = cursor.fetchone()[0]

    if cities:
        print(cities)
    else:
        print("No cities found for the state:", state_name)

    cursor.close()
    db.close()
