#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    """ Connect to the database """
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=dbname,
        port=3306
    )

    """ Create a cursor object """
    cursor = db.cursor()

    """ Execute the SQL query to retrieve all states """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """ Fetch all rows and print them """
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    """ Close the cursor and database connection """
    cursor.close()
    db.close()
