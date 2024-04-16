#!/usr/bin/python3

'''a script that takes in an argument and displays all values
    in the states table of
    hbtn_0e_0_usa where name matches the argument'''

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

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
