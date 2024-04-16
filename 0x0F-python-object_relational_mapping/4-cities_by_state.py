#!/usr/bin/python3

'''a script that lists all cities from the database hbtn_0e_4_usa'''

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_user,
                         passwd=mysql_password, db=mysql_db)
    cursor = db.cursor()

    cursor.execute("""
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    db.close()
