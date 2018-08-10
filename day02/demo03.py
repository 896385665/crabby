from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


# 以装饰器的形式添加自定义过滤器
@app.template_filter('lireverse')
# 方式二 app.add_template_filter(do_lireverse, 'lireverse')第一个参数函数名，第二个参数过滤器名
def do_lireverse(value):
    tem_li = list(value)
    tem_li.reverse()
    return tem_li


# 渲染模板
@app.route('/demo1')
def demo1():
    urlstr = 'www.baidu.com'
    myint = 18
    mylist = [1, 2, 's', 'qwq', {'mame': 'laowang'}]
    mydict = {'name': 'hm', 'url': 'www.baidu.com'}
    return render_template('01-index.html', url_str=urlstr, url_int=myint, url_list=mylist, url_dict=mydict)


# 控制代码模块
@app.route('/demo2')
def demo2():
    my_list = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
            "id": 5,
            "value": "以梦为马，越骑越傻"
        }
    ]
    return render_template('03-temp.html', my_list=my_list)


if __name__ == '__main__':
    app.run(port='3333', debug=True)
