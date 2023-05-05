import psycopg2

# Connect to DataBase:

conn = psycopg2.connect(host='localhost', database='test', user='cheatbarspin', password='1053')
try:
    with conn:
        with conn.cursor() as cur:
            # execute query
            cur.execute("INSERT INTO user_account VALUES (%s, %s)", (7, 'Wolfgang'))
            cur.execute("SELECT * FROM user_account")

            rows = cur.fetchall()
            # print(rows)
            for row in rows:
                print(row)
finally:
    # Close connection
    conn.close()
