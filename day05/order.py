from flask import Blueprint
# 初始化蓝图
order_blue = Blueprint('order', __name__)


# 使用蓝图注册路由
@order_blue.route('/order/<order_id>')
def order_info(order_id):
    return "查询订单信息 %s" % order_id

