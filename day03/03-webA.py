from flask import Flask, render_template, request, make_response, redirect, url_for, flash
import base64
import os

app = Flask(__name__)
app.secret_key = 'sdfg'


def generate_token():
    return base64.b64encode(os.urandom(48)).decode()


# 根节点-登录页
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            flash("请输入用户名和密码")
            return render_template("html/03-login.html")
        # 判断用户名和密码是否正确
        if username != "laowang" or password != "123456":
            flash("用户名和密码错误")
            return render_template("html/03-login.html")
        resp = make_response(redirect(url_for('transfer')))
        resp.set_cookie('username', username)
        return resp
    return render_template('html/03-login.html')


# /transfer 转账页面
@app.route('/transfer', methods=["GET", "POST"])
def transfer():
    # if判断：如果没有登录，重定向到登录页
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('index'))
    if request.method == 'POST':
        # 去做转账的逻辑
        # 取出参数
        to_account = request.form.get('to_account')
        money = request.form.get('money')
        # 从表单中取出来隐藏随机值
        form_token = request.form.get('token')
        # 再从 cookie 中取出随机值
        cookie_token = request.cookies.get('cookie_token')
        if not all([to_account, money]):
            flash("请完整输入参数")
            return render_template('html/03-transfer.html')
        if form_token != cookie_token:
            return '非法请求'
        # 执行转账操作
        print("假装执行转账操作，转给 %s, 转 %s" % (to_account, money))
        return "假装执行转账操作，转给 %s, 转 %s" % (to_account, money)
    # 生成随机值
    token = generate_token()
    # 将渲染模板的操作封装成响应
    resp = make_response(render_template('html/03-transfer.html', token=token))
    # 再存一份到 webB 不能取到的地方
    resp.set_cookie('cookie_token', token)
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
