import sqlite3

books_DB_path = r'App/Data/Books_DB.db'
# books_DB_path = r'App\Data\Books_DB.db'


def connect_to_db():
    # Connect
    con = sqlite3.connect(books_DB_path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    return con,cur


def get_data_from_db():
    # Connect
    con ,cur = connect_to_db()
    
    # get data
    result = cur.execute('SELECT * from Books').fetchall()    
    
    # close
    con.close()

    return result


def get_row(id_pk):
    # Connect
    con ,cur = connect_to_db()
    
    # get data
    result = cur.execute(f'SELECT * from Books WHERE id={id_pk}').fetchone()

    # close
    con.close()
    return result


def add_book_to_data(book, price, picture):
    # Connect
    con ,cur = connect_to_db()
    
    # add book
    cur.execute(f'INSERT INTO Books("Book", "Price", "Picture") VALUES("{book}","{price}","{picture}")')
    con.commit()

    # close
    con.close()


def search_by_book_name(book_name):
    # Connect
    con ,cur = connect_to_db()

    # search by book name
    results = cur.execute(f"SELECT *,rowid FROM Books WHERE Book LIKE '{book_name}%'").fetchall()
    print(results)

    # close
    con.close()

    return results


def del_book(id_pk):
    print("book DELETED")
    # Connect
    con ,cur = connect_to_db()
     
    # delete a book
    cur.execute(f'DELETE from Books WHERE rowid="{id_pk}"')
    con.commit()

    # close
    con.close()



def get_user(username):
    # Connect
    con ,cur = connect_to_db()
    
    # get data
    result = cur.execute(f'SELECT * from Users WHERE username="{username}"').fetchone()

    # close
    con.close()
    return result
    