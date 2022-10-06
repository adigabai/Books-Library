
from flask import Flask, render_template, request, redirect
from App.Data.data import get_data_from_db, get_row, add_book_to_data, search_by_book_name
from App.app_admin import admin_bp



app = Flask(__name__)
app.register_blueprint(admin_bp)


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


@app.route('/login')
def admin_login():
    return render_template('login_form.html')


@app.route('/search')
def search_a_book():
    book_name = request.args.get('search')
    results = search_by_book_name(book_name= book_name)
    return render_template('home.html', data= results)


if __name__ == "__main__":
    app.run(debug= True)

