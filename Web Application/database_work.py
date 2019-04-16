import psycopg2


def save_data(text, sum, id):
    print(type(sum))
    # Connect to the db
    con = psycopg2.connect(
        host='localhost',
        database='press',
        user='postgres',
        password='060800Bodia')

    # cursor creating
    cursor = con.cursor()
    cursor.execute('INSERT INTO text(text, user_id) VALUES (%s, %s)',
                   (text, id))
    text_id = cursor.execute('SELECT LAST_INSERT_ID(table)')
    cursor.execute('INSERT INTO summary(sum, text_id, user_id)'
                   ' VALUES (%s, %s, %s)',
                   (sum, text_id, id))

    con.commit()
    # Close the connection
    con.close()
