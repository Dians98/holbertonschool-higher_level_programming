#!/usr/bin/python3
"""
CITIES BY STATE
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # db = MySQLdb.connect(
    #     host="localhost",
    #     port=3308,
    #     user="root",
    #     passwd="root",
    #     db="hbtn_0e_0_usa"
    # )
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],

    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
