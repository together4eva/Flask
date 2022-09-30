from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='view')

@app.route('/login_process')
def login():
    username = request.args.get('user_name')
    if username == 'dave':
        return_data = {'auth': 'success'}
    else:
        return_data = {'auth': 'failed'}
    return jsonify(return_data)

@app.route('/login')
def hello_html():
    return render_template('login.html')

app.run(host='127.0.0.1', port=8080)