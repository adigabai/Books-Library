
from flask import Flask, render_template, request, redirect
from App.Data.data import get_data_from_db, get_row, add_book_to_data, search_by_book_name



app = Flask(__name__)


@app.route("/")
def home():
    books = get_data_from_db()
    return render_template('home.html', data= books)


@app.route("/book")
def book():
    book = []
    rowid = request.args.get('id')
    book = get_row(rowid = rowid)
    return render_template('book.html', data= book)


@app.route("/addbook")
def add_book():
    return render_template("add_book_form.html")


@app.route("/addbookin_db", methods=['POST'])
def add_book_in_db():
    book = request.form.get('bookname')
    price = request.form.get('price')
    picture = request.form.get('picture')
    print(f"{book},{price},{picture}")
    add_book_to_data(book=book, price=price, picture=picture)
    return redirect('/?massage=book added')


@app.route('/search')
def search_a_book():
    book_name = request.args.get('search')
    results = search_by_book_name(book_name= book_name)
    return render_template('home.html', data= results)



app.run(debug= True)

