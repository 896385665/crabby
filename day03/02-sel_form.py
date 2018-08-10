from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.secret_key = 'bvdhkbdvskhbvdsh'  # 这个值随意输入
'''
/根节点是普通表单、 demo1是WTF表单，使用两种表单提交，验证其过程。
'''


# 表单类
class RegisterForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    password2 = PasswordField('确认密码:', validators=[DataRequired(), EqualTo('password', '密码填入的不一致')])
    submit = SubmitField('提交')


@app.route('/demo1', methods=["get", "post"])
def demo1():
    regist_form = RegisterForm()
    if regist_form.validate_on_submit():  # 内置校验，关联RegisterForm类中的validators属性的所有验证
        # 1. 取到注册所对应的数据
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get('password2')
        # 2. 执行注册操作
        print("%s %s %s" % (username, password, password2))
        return "注册成功"
    else:
        if request.method == 'POST':
            return '获得post请求'
    return render_template('html/04-tempWTF.html', form=regist_form)


@app.route('/', methods=['GET', 'POST'])
def get_form():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        refirmpwd = request.form.get('refirmpwd')
        print(username)
        if not all([username, password, refirmpwd]):
            flash('参数不完整')
        elif password != refirmpwd:
            flash('密码不一致')
        else:
            return 'success'
    return render_template('html/02-form.html')


if __name__ == '__main__':
    app.run(debug=True)
