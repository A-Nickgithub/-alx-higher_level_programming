#!/usr/bin/python3
"""
We will use MySQLdb module to connect to our database
and the create a cursor that we will use to execute our queries
and then carry out our query to select all the states from the table states
then order them in ascending order by id
from there we will fetch the result of the query and print each on its ows line
finally we will close the connection
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()
