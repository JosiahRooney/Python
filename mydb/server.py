from flask import Flask, request, redirect, render_template, session, flash
from mysql import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

app.secret_key = "983248g923fiohf3u29ifbiu"


@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', friends=friends)


@app.route('/friends/add', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<friend_id>')
def show_friend(friend_id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': friend_id}
    friends = mysql.query_db(query, data)
    if not friends:
        flash("No friend found with the ID of "+friend_id, 'error')
        return render_template('index.html')
    else:
        return render_template('index.html', friend=friends[0])


@app.route('/friends/update/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'occupation': request.form['occupation'],
        'id': friend_id
    }
    mysql.query_db(query, data)
    flash('Friend updated!', 'success')
    return redirect('/friends/'+friend_id)


@app.route('/friends/remove/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path))
    return render_template('404.html'), 4044

app.run(debug=True)
