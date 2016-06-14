from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'euPRJ563DSXn2l69zdFxmI02sxXB50zzw6axi5kEwx6suTHaZks6'


@app.route('/')
def index():
    # session.pop('error')
    # session.pop('response')
    return render_template('index.html')


@app.route('/create', methods=['POST'])
def create_user():
    session['error'] = False

    if len(request.form['name']) < 1:
        flash("Name cannot be empty.")
        session['name'] = request.form['name']
        session['error'] = True
    else:
        session['name'] = request.form['name']

    if len(request.form['location']) < 1:
        flash("Please choose a location.")
        session['location'] = request.form['location']
        session['error'] = True
    else:
        session['location'] = request.form['location']

    if len(request.form['language']) < 1:
        flash("Please choose a language.")
        session['language'] = request.form['language']
        session['error'] = True
    else:
        session['language'] = request.form['language']

    if len(request.form['comments']) < 1:
        flash("Please leave a comment")
        session['comments'] = request.form['comments']
        session['error'] = True
    elif len(request.form['comments']) > 120:
        flash("Comments may only be 120 characters long")
        session['comments'] = request.form['comments']
        session['error'] = True
    else:
        session['comments'] = request.form['comments']

    return redirect('/')


app.run(debug=True)
