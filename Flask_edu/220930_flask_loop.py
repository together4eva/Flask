from flask import Flask, render_template

app = Flask(__name__, template_folder='view')

@app.route('/hello_loop')
def hello_loop():
    value_list = ['박문수', '김윤아', '한철호']
    return render_template('loop.html', values=value_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
    
    