

import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash

from App.Data.data import connect_to_db, get_user




login_bp = Blueprint('login', __name__, url_prefix='/login')



@login_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        eml = request.form['email']
        pet_name = request.form['pet_name']
        password = request.form['password']

        con ,cur = connect_to_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                cur.execute(f"INSERT INTO Users ('username', 'email', 'pet_name', 'password') VALUES ('{username}', '{eml}', '{pet_name}', '{generate_password_hash(password)}')")
                con.commit()
                con.close()
                flash('User has been added', category='message')
            except Exception as ex:
                error = f"{ex}"
            else:
                return redirect(url_for("login.login"))

        flash(error, category='error')
    
    return render_template('register_form.html')





@login_bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = get_user(username)

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            flash('user connected', category='message')
            return redirect(url_for('home.home'))

        flash(error, category='error')
        
    return render_template('login_form.html')



@login_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.home'))



def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login.login'))

        return view(**kwargs)

    return wrapped_view
    
    
    
@login_bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    con ,cur = connect_to_db()
    if user_id is None:
        g.user = None
    else:

        g.user = cur.execute(f"SELECT * FROM Users WHERE id='{user_id}'").fetchone()