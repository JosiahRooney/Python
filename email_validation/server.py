from flask import Flask, request, redirect, render_template, session, flash
from mysql import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')

app.secret_key = "983248g923fiohf3u29idd21321"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM emails")
    return render_template('index.html', emails=emails)


@app.route('/emails/add', methods=['POST'])
def create():
    email = request.form['email']
    if not EMAIL_REGEX.match(email):
        flash('Please enter a valid email address', 'error')
        return redirect('/')
    else:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        flash('Email added!', 'success')
        return redirect('/')


@app.route('/emails/delete/<email_id>', methods=['POST'])
def delete(email_id):
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id':email_id}
    mysql.query_db(query, data)
    flash("Email removed!","success")
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path))
    return render_template('404.html'), 4044

app.run(debug=True)
