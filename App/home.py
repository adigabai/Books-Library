from flask import render_template, request, Blueprint
from App.Data.data import get_data_from_db, get_row, search_by_book_name
from App.login import login_required

home_bp = Blueprint('home', __name__, url_prefix='/home')



@home_bp.route("/")
def home():
    books = get_data_from_db()
    return render_template('home.html', data= books)


@home_bp.route("/book")
def book():
    id_pk = request.args.get('id')
    book = get_row(id_pk = id_pk)
    return render_template('book.html', data= book)


@home_bp.route('/search')
def search_a_book():
    book_name = request.args.get('search')
    results = search_by_book_name(book_name= book_name)
    return render_template('home.html', data= results)


