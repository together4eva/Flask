
from flask import Flask, render_template

app = Flask(__name__, template_folder='view')

@app.route('/')
def index():
    html = render_template('index.html')
    return html

@app.route('/second')
def second():
    html = render_template('second.html')
    return html

@app.route('/third')
def third():
    html = render_template('third.html')
    return html

app.run(host='127.0.0.1', port=8080)












