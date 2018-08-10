from flask import Flask, make_response, request

app = Flask(__name__)
print(request.method)

@app.route('/')
def index():
    name = request.cookies.get('name')
    print(name)
    return 'index'


@app.route('/set_cookie')
def set_cookie():
    reps = make_response('设置cookie')
    # 在响应里设置cookie
    reps.set_cookie('name', 'laowang')
    # 设置cookie并设置生命周期时间
    reps.set_cookie('class', 'python9', max_age=3600)
    return reps


@app.route('/del_cookie')
def del_cookie():
    reps = make_response('删除cookie')
    # 在响应里删除cookie
    reps.delete_cookie('name')  # 将到期时间设置为创建时间

    return reps


if __name__ == '__main__':
    app.run(debug=True)
