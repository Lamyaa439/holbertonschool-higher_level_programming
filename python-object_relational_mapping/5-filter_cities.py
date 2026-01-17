#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def main():
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=db_user,
        passwd=db_password,
        db=db_name
    )

    cursor = db.cursor()
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
