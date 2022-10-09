from flask import Flask, render_template, request, redirect, Blueprint
from App.upload_file import upload_file
from App.Data.data import add_book_to_data, del_book, get_data_from_db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


# LOGIN
# @admin_bp.route('/checklogin', methods=['POST'])
# def admin_login():
#     user_name = "Amit"
#     password = "ADMiNLOGiN"
    
#     u = request.form.get('username')
#     p = request.form.get('password')

#     if user_name == u and password == p:
#         return redirect('/admin/home')
#     else:
#         return "bad pass/user"


@admin_bp.route('/home')
def home_admin():
    books = get_data_from_db()
    return render_template('home_admin.html', data= books)

# add book
@admin_bp.route("/addbook")
def add_book():
    return render_template("add_book_form.html")


@admin_bp.route('/add_a_book', methods=['POST'])
def add_book_in_db():
    book = request.form.get('bookname')
    price = request.form.get('price')
    picture = request.files.get('picture')
    upload_file()
    print(f"{book},{price},{picture}")
    add_book_to_data(book=book, price=price, picture=picture.filename)
    return redirect('/admin/home')


# delete book
@admin_bp.route('/delete_a_book')
def delete_book_from_db():
    rowid = request.args.get('id')
    del_book(id_pk= rowid)
    return redirect('/admin/home')