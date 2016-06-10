from flask import Flask, render_template, request, redirect, session
import random
from time import gmtime, strftime

app = Flask(__name__)
app.secret_key = "JQ;hcF1AZ59>mO^S7xhrXXK?c|Z3N&Siu(BT'[tp;DFw]YA%g't;|Oa>hv"

@app.route('/')
def index():
    # session['gold'] = 0
    # session.pop('response')
    if not session['gold']:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/gold', methods=['POST'])
def gold():
    d = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    try:
        session['response'] = session['response']
    except KeyError:
        session['response'] = []

    gold_amount = request.form['gold_amount']

    if gold_amount == "farm":
        gold_amount = random.randrange(10, 20)
        session['response'].append("You earned "+str(gold_amount)+" from the farm's harvest! "+str(d))

    elif gold_amount == "cave":
        gold_amount = random.randrange(5, 10)
        session['response'].append("You earned "+str(gold_amount)+" from the cave's hidden treasure! "+str(d))

    elif gold_amount == "forest":
        gold_amount = random.randrange(2, 5)
        session['response'].append("You earned "+str(gold_amount)+" from the forest's lumber! "+str(d))

    elif gold_amount == "casino":
        gold_amount = random.randrange(-50, 50)
        if gold_amount < 0:
            session['response'].append("You lost "+str(gold_amount)+" from gambling in the casino! "+str(d))
        else:
            session['response'].append("You won "+str(gold_amount)+" from gambling in the casino! "+str(d))

    session['gold'] += gold_amount

    if len(session['response']) > 10:
        session['response'].pop(0)

    return redirect('/')


app.run(debug=True)