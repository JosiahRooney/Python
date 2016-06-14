from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "LYFXr$enHXy?KQjOyMrk853ovSWr0R9Op8!szX7KixKMBxTr7tU^TioX3%"

def session_counter():
    try:
        session['count'] += 1
    except KeyError:
        session['count'] = 1


@app.route('/')
def index():
    session_counter()
    return render_template('index.html', count=session['count'])


@app.route('/reset', methods=['POST'])
def reset():
    session['count'] = 0
    return redirect('/')


@app.route('/ninja', methods=['POST'])
def ninja():
    session['count'] += 1
    return redirect('/')

app.run(debug=True)