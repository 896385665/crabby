from flask import Flask, request, session

app = Flask(__name__)

# 用于加密
app.config['SECRET_KEY'] = 'qwer'


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    # username = request.form.get('username')  # 正常情况下获取请求数据
    # password = request.form.get('password')
    # 自己设置数据
    session['username'] = '老王'
    session['password'] = 'qwert'
    return 'login succesce'


@app.route('/user_info')
def user_info():
    username = session.get('username')
    password = session.get('password')
    print(username)
    print(password)
    return 'user_info'


if __name__ == '__main__':
    app.run(debug=True)
