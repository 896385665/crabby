from flask import Flask,render_template

app = Flask(__name__)


@app.route('/', methods=['get', 'post'])
def index():
    return render_template('html/03-beat.html')


if __name__ == '__main__':
    app.run(port=9001)
