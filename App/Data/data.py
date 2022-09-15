
import sqlite3

books_DB_path = r'App/Data/Books_DB.db'
# books_DB_path = r'App\Data\Books_DB.db'

def get_data_from_db():
    # Connect
    con = sqlite3.connect(books_DB_path)
    cur = con.cursor()
    
    # get data
    result = cur.execute('SELECT *,rowid from Books').fetchall()    
    
    # close
    con.close()

    return result


def get_row(rowid):
    # Connect
    con = sqlite3.connect(books_DB_path)
    cur = con.cursor()
    
    # get data
    result = []
    result = cur.execute(f'SELECT * from Books WHERE rowid={rowid}').fetchall()

    # close
    con.close()
    return result



def add_book_to_data(book, price, picture):
    # Connect
    con = sqlite3.connect(books_DB_path)
    cur = con.cursor()
    
    # add book
    cur.execute(f'INSERT INTO Books("Book", "Price", "Picture") VALUES("{book}","{price}","{picture}")')
    con.commit()

    # close
    con.close()



def search_by_book_name(book_name):

    # Connect
    con = sqlite3.connect(books_DB_path)
    cur = con.cursor()

    # search by book name
    results = cur.execute(f"SELECT *,rowid FROM Books WHERE Book LIKE '{book_name}%'").fetchall()
    print(results)

    # close
    con.close()

    return results








#######################################################################################################

# def insert_data_into_db(data):
#     for d in data:
#         cur.execute(f'INSERT INTO Books VALUES("{d[0]}", "{d[1]}", "{d[2]}")')
#     con.commit()



# def get_data():
#     headers = {}
#     data = []
#     with open("C:\\Users\\Amit Hauzer\\Desktop\\VS_Projects\\John Bryce\\flask\\Flask_with_CSV_file\\Data\\books.csv", "r") as file:
#         for header in file.readline()[:-1].split(','):
#             headers[header] = []

#         lines = file.readlines()
#         for i in lines:
#             i = i[:-1].split(',')
            
#             data.append(i)

#     # convert_to_tuple(data)
    
#     return data, headers


# # def convert_to_tuple(data):
# #     for i,d in enumerate(data):
# #         data[i] = tuple(d)
    
# #     return data


# if __name__ == "__main__":
#     con = sqlite3.connect(r'C:\Users\Amit Hauzer\Desktop\VS_Projects\John Bryce\flask\Flask_with_db\Data\Books_DB.db')
#     cur = con.cursor()
#     cur.execute('CREATE TABLE Books (Book Name, Price, Picture)')

#     # data, header = get_data()
#     # insert_data_into_db(data)