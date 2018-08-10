from flask import Flask
from werkzeug.routing import BaseConverter
import flask

app = Flask(__name__)  # type:Flask
app.debug = True

'''其中to_python方法的作用就是将你传过去的参数转换成对应类型的数据，比如你设置传参是uuid类型数据，那么当你传参以后，就会调用to_python方法，将参数转换为对应的uuid类型。'''
# 根目录
@app.route('/')
def hello_world():
    return 'Hello World!'


class ListConverter(BaseConverter):

    def to_python(self, values):
        """
        将url中的参数转换为我们需要的数据类型
        """
        # split方法就是去掉加号并返回list类型数据
        tmp = values.split('+')
        print('tmp: %s' % tmp)
        return tmp

    def to_url(self, values):
        """
        将[1,2,3]转换成1+2+3
        """
        # 遍历列表values中的数据，以+连接，最后tmp1的值即1+2+3
        # BaseConverter.to_url是对url进行编码
        tmp1 = '+'.join([BaseConverter.to_url(self, value) for value in values])
        print('tmp1:%s' % tmp1)
        return tmp1


# 将写好的类注册到DEFAULT_CONVERTERS
app.url_map.converters['list'] = ListConverter


@app.route('/detail/<list:params>/')
def detail(params):
    print('parmas:%s' % params)
    return 'success for url'


with app.test_request_context():
    print('detail函数的url是:%s' % flask.url_for('detail', params=[1, 2, 3]))


if __name__ == '__main__':
    app.run()