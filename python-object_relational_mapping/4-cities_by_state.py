#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
The results show city ID, city name, and state name.
"""
import MySQLdb
import sys


def main():
    """Connects to the database and retrieves cities with state names."""
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
