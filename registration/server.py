from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "XwPp9xazJ0ku5CZnlmgAx2Dld8SHkAeTw"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'[a-zA-Z0-9\!\@\#\$\%\^\&\*\(\)\_\+\-\=\<\>\?\,\.\/\\\;\:]')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    # email
    if len(request.form['email']) == 0:
        flash('Please enter your email', 'email_error')
    else:
        if not EMAIL_REGEX.match(request.form['email']):
            flash('Please enter a valid email', 'email_error')
        else:
            session['email'] = request.form['email']

    # first name
    if len(request.form['first_name']) == 0:
        flash('Please enter your first name', 'fname_error')
    else:
        session['fname'] = request.form['first_name']

    # last name
    if len(request.form['last_name']) == 0:
        flash('Please enter your last name', 'lname_error')
    else:
        session['lname'] = request.form['last_name']

    # password
    password = request.form['password']
    if len(password) == 0:
        flash('Please enter a password', 'pw_error')
    else:
        if password.isalpha():
            flash('Please use at least one special character in your password', 'pw_error')
        elif not PASS_REGEX.match(password):
            flash('Please enter a valid password using the rules below', 'pw_error')
        else:
            session['password'] = request.form['password']

    # confirm password
    confirm = request.form['confirm_password']
    if len(confirm) == 0:
        flash('Please confirm your password', 'conf_error')
    else:
        if confirm != password:
            flash('Please enter the same password as above', 'conf_error')
        else:
            session['confirm_password'] = request.form['confirm_password']

    return redirect('/')

app.run(debug=True)