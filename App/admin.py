from flask import flash, render_template, request, redirect, Blueprint, g, url_for
from App.login import login_required
from App.upload_file import upload_file
from App.Data.data import add_book_to_data, del_book, get_data_from_db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')



@admin_bp.route('/home')
@login_required
def home_admin():
    if check_if_admin():
        books = get_data_from_db()
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
