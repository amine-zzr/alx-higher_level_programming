#!/usr/bin/python3

'''
    a script that takes in the name of a state as an argument and
    lists all cities of that state
    using the database hbtn_0e_4_usa
'''

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_user,
                         passwd=mysql_password, db=mysql_db)
    cursor = db.cursor()

    query = """
            SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchone()

    if cities and cities[0] is not None:
        print(cities[0])
    else:
        print()

    db.close()
