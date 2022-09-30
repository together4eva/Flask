from flask import Flask, render_template

app = Flask(__name__, template_folder='view')

@app.route('/')
def index():
    html = render_template('index.html')
    return html

app.run(host='0.0.0.0', port=8080)