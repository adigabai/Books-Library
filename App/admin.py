from datetime import date
from flask import flash, render_template, request, redirect, Blueprint, g, url_for
from App.login import login_required
from App.upload_file import delete_file, upload_file
from App.Data.data import add_book_to_data, del_book, get_a_book_from_db, get_all_books_from_db, return_loans_of_deleted_book

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')



@admin_bp.route('/home')
@login_required
def home_admin():
    if check_if_admin():
        books = get_all_books_from_db()
        return render_template('home_admin.html', data= books)
    else:
        return redirect(url_for('login.login'))



# add a book
@admin_bp.route('/addbook', methods=['GET','POST'])
@login_required
def add_book():
    if check_if_admin():
        if request.method == 'POST':
            book = request.form.get('bookname')
            price = request.form.get('price')
            picture = request.files.get('picture')
            upload_file()
            print(f"{book},{price},{picture}")
            add_book_to_data(book=book, price=price, picture=picture.filename)
            return redirect('/admin/home')
        return render_template("add_book_form.html")
    else:
        return redirect(url_for('login.login'))



# delete book
@admin_bp.route('/delete_a_book')
@login_required
def delete_book_from_db():
    if check_if_admin():
        id_pk = request.args.get('id')
        book = get_a_book_from_db(id_pk = id_pk)
        # delete the book's file.
        delete_file(book_picture=book['Picture'])
        # returns all the loans of this book.
        return_loans_of_deleted_book(book_id= book['id'], return_date= date.today(), returned=True)
        # delete the book from db.
        del_book(id_pk= id_pk)
        return redirect('/admin/home')
    else:
        return redirect(url_for('login.login'))



def check_if_admin():
    permission = 'admin'
    # user_permissions = session.get('permissions')
    if g.user['permissions'] == permission:
        print('the user is admin')
        return True
    else:
        flash('Error!', category='error')
        return False
