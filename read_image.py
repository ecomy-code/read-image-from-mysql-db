from mysql.connector import MySQLConnection as MyDB, Error
def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)


def read_blob(author_id, filename):

    query = "SELECT photo FROM authors WHERE id = %s"

    try:
        # query blob data form the authors table
        conn = MyDB(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, (author_id,))
        photo = cursor.fetchone()[0]

        write_file(photo, filename)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

def main():
    read_blob(144,"output\garth_stein.jpg")

    
