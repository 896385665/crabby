import unittest
from day04.BookManage import db, app, Author
import time

# 目标：测试数据库
class databaseTest(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user1:123456@127.0.0.1:3306/alchemy_test'
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.testing = True
        db.create_all()

    def tearDown(self):
        # 关闭数据库和移除所有表
        db.session.remove()
        db.drop_all()

    def test_add_Author(self):
        # 　创建模型对象并提交到数据库
        au1 = Author(name='老宋')
        db.session.add(au1)
        db.session.commit()

        time.sleep(15)

        aut = Author.query.filter(Author.name == '老宋').first()
        self.assertIsNotNone(aut, '添加失败')

    def test_add_book(self):
        print('qwer')

if __name__ == '__main__':
    unittest.main()