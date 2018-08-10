from flask import Flask
from day05.order import order_blue
from day05.cart import cart_blue

app = Flask(__name__)
# app注册蓝图(修改app的url_map值)
app.register_blueprint(order_blue)
app.register_blueprint(cart_blue)


@app.route('/')
def index():
    return 'index'


# 以下代码抽取到 order.py 中
# @app.route('/order/<order_id>')
# def order_info(order_id):
#     return "查询订单信息 %s" % order_id


# 以下代码抽取到 cart 模块中
# @app.route('/cart/list')
# def cart_list():
#     return "返回购物车列表"


@app.route('/user/info')
def user_info():
    return "用户信息"


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
