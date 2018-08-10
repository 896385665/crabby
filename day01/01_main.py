from flask import Flask, render_template

# from config import DevConfig

app = Flask(__name__)
# 配置debug模式的3种方式
# 1.直接配置
# app.debug = True
# 2.从对象中加载配置
# class Config(object):
#     DEBUG = True
# app.config.from_object(Config)
# 3. 从文件中加载配置
app.config.from_pyfile('Config.ini')


@app.route('/', methods=['get', 'post'])
def index():
    return 'index'


# 通过传入参数，来加载不同的信息
# <>定义路由的参数 <>内加入参数
@app.route('/orders/<order_id>')
def get_order_id(order_id):
    return 'order_id: %s' % order_id


# 渲染模板
@app.route('/temm')
def getMytem():
    urlstr = 'www.baidu.com'
    myint = 18
    mylist = [1, 2, 's', 'qwq', {'mame': 'laowang'}]
    mydict = {'name': 'hm', 'url': 'www.baidu.com'}
    return render_template('01-index.html', url_str=urlstr, url_int=myint, url_list=mylist, url_dict=mydict)


# 以装饰器的形式添加自定义过滤器
@app.template_filter('lireverse')
# 方式二 app.add_template_filter(do_lireverse, 'lireverse')第一个参数函数名，第二个参数过滤器名
def do_lireverse(value):
    tem_li = list(value)
    tem_li.reverse()
    return tem_li


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0')
    # Rule 装饰器 到 函数的映射关系， url_map 多个Rule的集合
    '''
     Map([<Rule '/temm' (GET, HEAD, OPTIONS) -> getMytem>,
     <Rule '/' (GET, POST, HEAD, OPTIONS) -> index>,
     <Rule '/orders/<order_id>' (GET, HEAD, OPTIONS) -> get_order_id>,
     <Rule '/static/<filename>' (GET, HEAD, OPTIONS) -> static>])
    '''
