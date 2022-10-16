import os
from flask import Flask, flash, request, redirect, url_for,render_template, send_from_directory, current_app
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = r'.\App\static\books_images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'picture' not in request.files:
            flash('No file part')
            # return redirect(request.url)
        file = request.files['picture']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            # return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            # return redirect(url_for('download_file', name=filename))
    else:
        print('its not POST method')


# def check_a_file():









# @app.route('/uploads/<name>')
# def download_file(name):
    # return send_from_directory(current_app.config["UPLOAD_FOLDER"], name)


# app.run(debug=True)