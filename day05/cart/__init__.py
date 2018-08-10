from flask import Blueprint

# 初始化蓝图 # 蓝图默认没有设置静态文件夹和模板文件夹，需要自己手动指定
# url_prefix='/cart' 指定static前缀，否则会使用flask默认的根目录static
cart_blue = Blueprint('cart', __name__, static_folder='static', template_folder='templates', url_prefix='/cart')
# 如果蓝图模块下的模板文件名与项目根目录下的模板文件存在同名的话，那么在渲染的时候，会使用项目根目录下的模板文件


from .views import *