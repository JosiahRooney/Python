from flask import Flask, render_template, request, redirect, session, flash
from mysql import MySQLConnector
import re
from flask_bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'login_registerdb')

app.secret_key = "u0h931hf092hf0iwdfsoisdhfsdfh"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register/')
def register():
    return render_template('register.html')


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/success/')
def success():
    if not "user_logged_in" in session:
        return redirect('/')
    return render_template('success.html')


@app.route('/register/process/', methods=['POST'])
def register_process():

    first_name = request.form['first_name']
    if len(first_name) == 0:
        flash("Please enter your first name", "error")
        return redirect('/register/')

    last_name = request.form['last_name']
    if len(last_name) == 0:
        flash("Please enter your last name", "error")
        return redirect('/register/')

    email = request.form['email']
    if len(email) == 0:
        flash("Please enter your email", "error")
        return redirect('/register/')
    else:
        if not EMAIL_REGEX.match(email):
            # email isn't valid
            flash("Please enter a valid email", "error")
            return redirect('/register/')

    password = request.form['password']
    if len(password) == 0:
        flash("Please enter your password", "error")
        return redirect('/register/')
    else:
        if not PW_REGEX.match(password):
            flash("Please enter a valid password", "error")
            return redirect('/register/')

    username = request.form['username']
    if len(username) == 0:
        flash("Please enter a username", "error")
        return redirect('/register/')

    confirm_pw = request.form['confirm_password']
    if len(confirm_pw) == 0:
        flash("Please confirm your password", "error")
        return redirect('/register/')
    else:
        if confirm_pw != password:
            flash("Passwords don't match")
            return redirect('/register/')

    pw_hash = bcrypt.generate_password_hash(password)
    query = "INSERT INTO users (first_name, last_name, username, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :username, :email, :pw_hash, NOW(), NOW() )"
    data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "pw_hash": pw_hash,
        "username": username
    }
    mysql.query_db(query, data)

    select_query = "SELECT user_id FROM users WHERE email = :email"
    data = {"email": email}
    result = mysql.query_db(select_query, data)

    session['user_id'] = result[0]['user_id']
    session['user_logged_in'] = True
    session['username'] = username
    session['user_email'] = email

    return redirect('/success/')


@app.route('/login/process/', methods=['POST'])
def login_process():
    errors = False

    email = request.form['email']
    if len(email) == 0:
        flash("Please enter your email")
        errors = True

    password = request.form['password']
    if len(password) == 0:
        flash("Please enter your email")
        errors = True

    if errors:
        return redirect('/login/')

    query = "SELECT * FROM users where email = :email"
    data = {
        "email": email
    }
    users = mysql.query_db(query, data)

    if bcrypt.check_password_hash(users[0]['pw_hash'], password):
        # password matches
        return redirect('/success/')

    flash("Your email or password didn't match, please try again", "error")
    return redirect('/login/')


@app.route('/logout/', methods=['POST'])
def logout():
    session.clear()
    flash("You logged out!", "success")
    return redirect('/')

app.run(debug=True)