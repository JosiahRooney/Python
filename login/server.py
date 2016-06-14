from flask import Flask, request, redirect, render_template, session, flash
from mysql import MySQLConnector
import re
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'logindb')

app.secret_key = "983248gdssd923w2198321e21348g923w21"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login_process():
    return render_template('login.html')


@app.route('/login/process', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    errors = False
    query_data = {
        'username':username
    }

    if len(username) == 0:
        flash("Please enter your username", 'username_error')
        errors = True
    else:
        query_data['username'] = username

    if len(password) == 0:
        flash("Please enter your password", 'password_error')
        errors = True

    if errors:
        return redirect('/login')
    else:
        select_query = "SELECT * FROM users WHERE username = :username LIMIT 1"
        user = mysql.query_db(select_query, query_data)
        if user:
            if bcrypt.check_password_hash(user[0]['pw_hash'], password):
                flash("Logged in!", 'success')
                session['user_logged_in'] = True
                return redirect('/')
            else:
                flash("The username or password didn't seem to work, please try again.", 'error')
                return redirect('/login')
        else:
            flash("The username or password didn't seem to work, please try again.", 'error')
            return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('user_logged_in')
    flash("You have logged out", 'success')
    return redirect('/')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register/process', methods=['POST'])
def register_process():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    query_data = {
        'username': username,
        'email': email,
        'pw_hash': ''
    }
    errors = False

    if len(email) == 0:
        flash('Please enter your email', 'error')
        print("You didn't enter an email")
        errors = True

    if len(username) == 0:
        flash('Please enter a username', 'error')
        print("You didn't enter a username")
        errors = True

    if len(password) < 8:
        flash('Please enter a password of at least 8 characters', 'error')
        print("Password isnt long enough")
        errors = True
    else:
        if password == confirm_password:
            if PW_REGEX.match(password):
                pw_hash = bcrypt.generate_password_hash(password)
                query_data['pw_hash'] = pw_hash
            else:
                flash("Please use at least one lowercase letter, one uppercase letter, and one special character in your password", 'error')
                print("Your password didn't meet the criteria")
                errors = True
        else:
            flash("Please enter the same password twice", 'error')
            print("Password didn't match")
            errors = True

    if errors:
        print('There were errors')
        return redirect('/register')
    else:
        print(query_data)
        insert_query = "INSERT INTO users (username, pw_hash, email, created_at, updated_at) VALUES (:username, :pw_hash, :email, NOW(), NOW())"
        mysql.query_db(insert_query, query_data)
        flash('Account successfully created!', 'success')
        return redirect('/')





@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', request.path)
    return render_template('404.html'), 4044

app.run(debug=True)
