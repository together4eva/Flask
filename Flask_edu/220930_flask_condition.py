from flask import Flask, render_template

app = Flask(__name__, template_folder='view')

@app.route('/hello_if/<age>')
def hello_if(age):
    value = int(age)
    return render_template('condition.html', data = value)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)