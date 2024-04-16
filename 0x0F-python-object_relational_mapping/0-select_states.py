#!/usr/bin/python3

'''a script that lists all states from the database hbtn_0e_0_usa'''

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=mysql_user,
                         passwd=mysql_password, db=mysql_db)
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
