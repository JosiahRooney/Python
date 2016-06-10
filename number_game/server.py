from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "8d9f8o29h9d9f823f"


@app.route('/')
def index():
    session['number'] = random.randrange(1, 100)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) > session['number']:
        session['response'] = "Your guess was too high!"
        return redirect('/game')
    elif int(request.form['guess']) < session['number']:
        session['response'] = "Your guess was too low!"
        return redirect('/game')
    else:
        session.pop('response')
        return render_template('win.html')

@app.route('/game')
def game():
    return render_template('index.html')

app.run(debug=True)
