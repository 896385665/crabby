from flask import Flask, request, json, jsonify, redirect, url_for

app = Flask(__name__)


# 规定传入的参数是int类型
@app.route('/user/<int:user_id>')
def demo1(user_id):
    return 'user_id %s' % user_id


@app.route('/demo2', methods=['GET', 'POST'])
def demo2():
    return 'demo2 请求方式：%s' % request.method


#  返回 json字符串
@app.route('/json')
def demo3():
    tem_dict = {
        'name': 'laowangba',
        'age': 23
    }
    # json_str = json.dumps(tem_dict)
    json_str = jsonify(tem_dict)  # jsonify相比于json.dumps，都能返回json，但是jsonify生成响应，设置 content-type为 application/json
    return json_str


# 重定向
@app.route('/redirect')
def demo4():
    # 重定向到网络地址
    # return redirect('http://www.baidu.com')
    # 重定向到已有视图函数; url_for 传入函数名字，生成函数所对应的路由地址
    return redirect(url_for('demo1', user_id=3456))  # url_for生成指定视图函数名所对应的路路由,第一个参数函数名，第二个参数是函数需要的参数


# 自定义状态码
@app.route('/demo5')
def demo5():
    return '指定状态码', 665


@app.route('/<any(about, help, imprint, class, "foo,bar"):prams>')
def demo6(prams):
    return prams


if __name__ == '__main__':
    # print(app.url_map)
    '''
      Map([<Rule '/redirect' (GET, OPTIONS, HEAD) -> demo4>,
     <Rule '/demo2' (GET, OPTIONS, POST, HEAD) -> demo2>,
     <Rule '/demo5' (GET, OPTIONS, HEAD) -> demo5>,
     <Rule '/json' (GET, OPTIONS, HEAD) -> demo3>,
     <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>,
     <Rule '/user/<user_id>' (GET, OPTIONS, HEAD) -> demo1>,
     <Rule '/<prams>' (GET, OPTIONS, HEAD) -> demo6>])
     '''
    app.run(debug=True)
