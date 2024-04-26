#!/usr/bin/python3
"""
This script filters the states in the
hbtn_0e_0_usa database by matching their
name with the name provided in the argv[4]
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
            "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
            (state_name,)
            )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
