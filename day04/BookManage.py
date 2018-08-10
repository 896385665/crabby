import base64
import os

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'rty'
# 配置数据库链接地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user1:123456@127.0.0.1:3306/alchemy'
# 是否跟踪数据库的修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 初始化数据库操作对象
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'main page'


def generate_token():
    return base64.b64encode(os.urandom(48)).decode()


# 创建表单类，用来添加信息
class Appform(FlaskForm):
    csrf_token = generate_token()
    au_info = StringField(validators=[DataRequired()])
    bk_info = StringField(validators=[DataRequired()])
    submit = SubmitField('添加')


# 加载显示模板
@app.route('/bookdesk', methods=['GET', 'POST'])
def bookdesk():
    form = Appform()
    if request.method == 'POST':
        if form.validate():     #判断参数是否完整
            author_name = form.au_info.data
            book_name = form.bk_info.data
            # 判断要添加书籍的作者是否存在，如果存在只添加书籍，不存在先添加作者再加书籍
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                try:    # 执行添加作者和书籍的事物操作
                    au = Author(name=author_name)
                    # db.session.add(au)
                    # db.session.commit()
                    # book = Book(name=book_name, author_id=au.id)
                    book = Book(name=book_name)
                    book.author = au
                    db.session.add_all([au, book])
                    # db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    flash('作者、书籍添加失败')
                else:
                    print('作者、书籍添加成功')
                    flash('作者、书籍添加成功')
            else:
                booknames = Book.query.filter(Book.name==book_name, Book.author_id==author.id).first()
                if not booknames:
                    try:    # 执行添加书籍操作
                        book1 = Book(name=book_name, author_id=author.id)
                        db.session.add(book1)
                        db.session.commit()
                    except Exception as e:
                        print(e)
                        db.session.rollback()
                        flash('书籍添加失败')
                    else:
                        flash('书籍添加成功')
                else:
                    flash('该作者名下已存在相同的书籍')
        else:
            print('form表单数据不完整')
            flash('请完善数据')

    author = Author.query.all()
    book = Book.query.all()
    return render_template('au_book.html', author=author, book=book, form=form)


@app.route('/deleteBook/<int:book_id>')
def deleteBook(book_id):
    book = Book.query.get(book_id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
        except Exception as e:
            print(e)
            print('删除书籍失败！！！')
            db.session.rollback()
    else:
        flash('书籍不存在')

    return redirect(url_for('bookdesk'))


@app.route('/deleteAuthor/<int:author_id>')
def deleteAuthor(author_id):
    author = Author.query.get(author_id)
    if author:
        try:
            Book.query.filter(Book.author_id == author_id).delete()
            db.session.delete(author)
            db.session.commit()
        except Exception as e:
            print(e)
            print('删除作者失败！！！')
            db.session.rollback()
    else:
        flash('作者不存在')

    return redirect(url_for('bookdesk'))


# 定义模型类-作者
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    au_book = db.relationship('Book', backref='author')

    def __repr__(self):
        return '作者:%s' % self.name


# 定义模型类-书名
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64))
    author_id = db.Column(db.INTEGER, db.ForeignKey('author.id'))
    # author_id = db.relationship(db.INTEGER, db.foreign(Author.id)) # 作用同上

    def __str__(self):
        return '书名:%s' % self.name


def executive():
    try:
        db.drop_all()
        db.create_all()
        au1 = Author(name='老王')
        au2 = Author(name='老刘')
        au3 = Author(name='老尹')
        db.session.add_all([au1, au2, au3])
        db.session.commit()

        bk1 = Book(name='老王回忆录', author_id=au1.id)
        bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
        bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
        bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
        bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
        db.session.add_all([bk1, bk2, bk3, bk4, bk5])
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    else:
        print('succese')


if __name__ == '__main__':
    # executive()
    app.run(debug=True)

'''
1.创建模型
2.填充数据
3.渲染模板
4.form类
5.提交后，函数处理
'''