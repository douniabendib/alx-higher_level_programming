#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
import sys

if __name = "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name
    LIKE BINARY '{}'".format(sys.argv[4]))
    row = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()