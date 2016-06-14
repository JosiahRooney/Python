from flask import Flask, request, redirect, render_template, session, flash
from mysql import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'full_friendsdb')

app.secret_key = "983248g923fiohf3u29idd21321"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', friends=friends)


@app.route('/friends/add', methods=['POST'])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    data = {}
    errors = False

    if len(first_name) == 0:
        flash('Please enter a first name', 'error')
        errors = True
    else:
        data['first_name'] = first_name

    if len(last_name) == 0:
        flash('Please enter a last name', 'error')
        errors = True
    else:
        data['last_name'] = last_name

    if not EMAIL_REGEX.match(email):
        flash('Please enter a valid email address', 'error')
        errors = True
    else:
        data['email'] = email

    if not errors:
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        mysql.query_db(query, data)
        flash('Friend added!', 'success')
        return redirect('/')
    else:
        return redirect('/')


@app.route('/friends/<friend_id>')
def show(friend_id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = {'id': friend_id}
    friend = mysql.query_db(query, data)
    if not friend:
        flash("There is no friend with the ID of "+friend_id,'error')
        return render_template('show.html')
    else:
        return render_template('show.html',single_friend=friend)


@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW()"
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    mysql.query_db(query, data)
    flash('Friend updated','success')
    return redirect('/friends/'+friend_id)


@app.route('/friends/<friend_id>/delete', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id':friend_id}
    mysql.query_db(query, data)
    flash("Friend removed!","success")
    return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path))
    return render_template('404.html'), 4044

app.run(debug=True)
