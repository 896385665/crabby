'''请求勾子'''
from flask import Flask, abort

# 假如函数 A 提供了一个勾子函数，那么在 A 执行的过程中根据情况就会去执行这个勾子函数
# 而勾子函数中的实现可能是我们自己的代码
app = Flask(__name__)


@app.route('/')
def index():
    a = 0
    b = 10 / a
    return 'index'


@app.route('/a')
def index1():
    return 'index1'


# 在第一次请求之前会调用这个装饰器所修饰的函数，只会执行一次
# 可以在这个函数里面做一些数据库链接，或者其他的一些准备
@app.before_first_request
def before_first_request():
    print('before_first_request')
    return 'before_first_request'


# 在每一次请求之前会被调用
# 应用场景：接口是否合法的检验
@app.before_request
def before_request():
    print('before_request')
    # a = True
    # if a:
    #     return '不合法'


# 在请求之后，响应真正返回给客户端之前会调用
# 并且会接收到视图函数所生成响应
@app.after_request
def after_request(req):  # req:对请求的响应
    print('after_request')
    # req.headers['Content-Type'] = 'application/json'  # 可以对响应做最一后一步处理
    return req


# 在请求销毁的时候会执行，如果在请求的过程中，有错误抛出的话，那么会将该错误传递到当前函数中
# 可以用于监听所有的视图函数产生的错误
@app.teardown_request
def teardown_request(error):
    print('teardown_request %s' % error)


if __name__ == '__main__':
    app.run(debug=True)
