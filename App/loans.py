
from flask import render_template, request, redirect, Blueprint, session
from App.login import login_required
from App.Data.data import get_row, add_loan_in_db
from datetime import date

loan_bp = Blueprint('loan', __name__, url_prefix='/loan')



@loan_bp.route('/', methods=['GET', 'POST'])
@login_required
def loan_a_book():
    # the relevant book
    book_id = request.args.get('id')
    book = get_row(id_pk = book_id)
    # ths relevant user
    user_id = session.get('user_id')

    
    if request.method == 'POST':
        # loan date
        loan_date = date.today()
        # return date
        return_date = request.form.get('return_date').split('-')
        return_date = date(int(return_date[0]), int(return_date[1]), int(return_date[2]))
        
        # days for loan
        diff = return_date - loan_date

        # add loan in DB
        add_loan_in_db(loan_date= loan_date, return_date= return_date, book_id= book_id, user_id= user_id, returned=False)
       
        print(f"{return_date} - {loan_date} = {diff.days}")
        return f"you loaned {book['Book']}"

    return render_template('loan_form.html',data= book)