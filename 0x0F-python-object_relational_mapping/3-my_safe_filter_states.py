#!/usr/bin/python3
"""script that takes in arguments and displays all values"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = db.cursor()
    s_name = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s",(s_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
