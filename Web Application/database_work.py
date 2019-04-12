import psycopg2


def save_data(user_id, text, sum):
    print(type(sum))
    # Connect to the db
    con = psycopg2.connect(
        host='127.0.0.1',
        database='postgres',
        user='bohdan',
        password='060800Bodia')

    # cursor creating
    cursor = con.cursor()
    SQL = "SELECT MAX(text_id) FROM text"
    cursor.execute(SQL)
    next_id = cursor.fetchone()[0] + 1
    cursor.execute('INSERT INTO text(text, text_id,  user_id) VALUES (%s, %s, %s)', (text, next_id, user_id))
    cursor.execute('INSERT INTO summary(sum_id, sum, text_id, user_id) VALUES (%s, %s, %s, %s)', (next_id, sum, next_id, user_id))

    con.commit()
    # Close the connection
    con.close()
