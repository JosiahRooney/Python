from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "XwPp9xazJ0ku5CZnlmgAx2Dld8SHkAeT"


@app.route('/')
def index():
    all_ninjas = False
    return render_template('index.html', all_ninjas=all_ninjas)

@app.route('/ninja/')
def ninja():
    all_ninjas = True
    return render_template('index.html', all_ninjas=all_ninjas)


@app.route('/ninja/<turtle>')
def ninjas(turtle):
    all_ninjas = False
    if turtle in ['leonardo','donatello','michelangelo','raphael']:
        ninja = turtle
        return render_template('index.html', ninja=ninja,all_ninjas=all_ninjas)
    else:
        return render_template('index.html', april=True)


app.run(debug=True)