from flask import Flask, render_template, request

app = Flask(__name__, template_folder='view')

@app.route('/')
def index():
    html = render_template('index1.html')
    return html

@app.route('/second', methods=['GET', 'POST'])  # request 종류를 규제, get이나 post나 모두 허용
def second():
    print('요청방식 :', {request.method})  # request.method : request 방식을 확인
    html = render_template('second1.html')
    return html

app.run(host='127.0.0.1', port=8080)