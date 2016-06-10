from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello_world():
    times = 50
    return render_template('index.html', name="Josiah", times=times)


@app.route('/about')

def about():
    return render_template('about.html')








app.run(debug=True)