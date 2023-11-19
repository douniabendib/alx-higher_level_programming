#!/usr/bin/python3
"""lists all cities of that state,using the database hbtn_0e_4_usa"""
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
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN 
    states ON states.id=cities.state_id WHERE states.name = %s""",
    (s_name, ))
    rows = cursor.fetchall()
    i = list(row[0] for row in rows)
    print(*i, sep=", ")
    cursor.close()
    db.close()
