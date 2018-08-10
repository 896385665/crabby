from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


# name='老王'&age=18
@app.route('/demo1', methods=['GET', 'POST'])
def demo1():
    print(request.args)
    print(request.args.get('name'))
    # print(request.args.get('age'))
    print('捕获表单', request.form)
    print('捕获data', request.data)
    return '控制台'


@app.route('/upload', methods=['POST'])
def demo2():
    pic = request.files.get('pic')
    pic.save('./static/aaa.png')
    return '保存成功'


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
