from flask import Flask, render_template, request

app = Flask(__name__, template_folder='view')

@app.route('/')
def index():
    html = render_template('index2.html')
    return html

@app.route('/second', methods=['GET', 'POST'])
def second():
    data3 = request.values.get('data2')  # request.values : post, get 상관없이 값을 받는다.
    
    if request.method == 'POST':
        data1 = request.form['data1']  # post로 넘어온 값을 받는 경우 : request.form
        data2 = request.form.get('data2')
        return "POST => data1 : {}, data2 : {}, data3 : {}".format(data1, data2, data3)
    
    elif request.method == 'GET':
        data1 = request.args['data1']  # get로 넘어온 값을 받는 경우 : request.args
        data2 = request.args.get('data2')
        return "GET => data1 : {}, data2 : {}, data3 : {}".format(data1, data2, data3)
    
    return 'hello world'

app.run(host='127.0.0.1', port=8080)



# request (get, post) - web server에 source script를 전송해 달라고 요청..
# request.get(url)
# request.post(url, data=data)

# get
# request할 때 전달할 파라미터 값을 url에 붙여서 전송하는 방식
# 255글자 이내 - 속도가 빠르다
# 문제 - 보안

# post
# request할 때 전달할 파라미터 값을 별도의 데이터 형식으로 전달...(json, xml, 암호화...)
# 문제 - 데이터가 추가가 되어서 속도도 느리고 메모리 비용이 크다
# 장점 - 보안, 데이터 양에 제한이 없다..