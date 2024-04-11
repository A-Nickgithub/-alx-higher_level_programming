#!/usr/bin/python3
"""
This script is implemented so at to avoid
sql injections
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
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
            (state_name,)
            )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
