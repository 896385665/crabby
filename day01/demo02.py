from flask import Flask, abort
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 自己定义一个转换器，继承与系统的BaseConverter
class rc(BaseConverter):
    # regex = '[a-z][0-9]{4}'
    def __init__(self, url_map, *args):
        super(rc, self).__init__(url_map)   # 调用父类
        self.regex = args[0]    #记录传入参数（正则)

    def to_python(self, values):
        # split方法就是去掉加号并返回list类型数据
        tmp = values.split('+')
        print('tmp: %s' % tmp)
        return 'tmp: %s' % tmp

# 把自定义的转换器添加到系统的转换器列表,并且指定转换器在使用的时候名字为aa
# url_map 视图函数和路由的映射关系的列表
app.url_map.converters['re'] = rc


@app.route('/')
def index():
    # a= 0
    # b = 10
    # c = b/a   # 除法错误的准备
    # abort(404)  # 主动强制抛出一个404错误
    return 'index'


@app.route('/user/<re("[a-z][0-9]{4}"):user_id>')
def demo1(user_id):
    return 'user_id %s' % user_id


@app.route('/card/<re("[a-z]{2}[0-9]{4}"):user_id>')
def demo2(user_id):
    return 'user_id %s' % user_id

# --------------以上是转换器部分------------------


# 捕获404错误，并返回一个友好提示(Register a function to handle errors by code or exception class)
@app.errorhandler(404)
def page_error(error):
    return '404-页面失踪了'


@app.errorhandler(ZeroDivisionError)
def zero_error(error):
    return '除法错误'


if __name__ == '__main__':
    app.run(debug=True)