# import psycopg2
#
# # Connect to DataBase:
# conn = psycopg2.connect(
#     host='localhost',
#     database='test',
#     user='cheatbarspin',
#     password='1053'
# )
#
# # Create Cursor
# cur = conn.cursor()
#
# # execute query
# # cur.execute("INSERT INTO user_account VALUES (%s, %s)", (3, 'Jon'))
# cur.executemany("INSERT INTO user_account VALUES (%s, %s)", [(4, 'Peter'), (5, 'Alice')])
# cur.execute("SELECT * FROM user_account")
# conn.commit()
#
# rows = cur.fetchall()
# # print(rows)
# for row in rows:
#     print(row)
#
# # Close cursor and connection
#
# cur.close()
# conn.close()
