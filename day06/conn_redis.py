from redis import StrictRedis


def connec():
    # 创建连接到redis数据库的StrictRedis对象
    sr = StrictRedis(host='127.0.0.1', port=6379, db=0, password=123456)
    return sr


def add():
    sr = connec()
    try:
        # 使用sr对象调用操作string类型数据的方法（方法和终端命令几乎一样）
        # 保存、增加 set key value
        if sr.exists('name'):
            reslut = sr.get('name')
            print('查询：', reslut)
        else:
            sr.set('name', 'dfg')
            reslut = sr.get('name')
            print('新增：', reslut)

    except Exception as e:
        print(e)


def mof():
    sr = connec()
    try:
        # 使用sr对象调用操作string类型数据的方法（方法和终端命令几乎一样）
        # 保存、增加 set key value
        if sr.exists('name'):
            reslut1 = sr.get('name')
            print('修改前：', reslut1)
            sr.set('name', 'after')
            reslut2 = sr.get('name')
            print('修改后：', reslut2)
        else:
            sr.set('name', 'dfg')
            reslut = sr.get('name')
            print('新增：', reslut)
    except Exception as e:
        print(e)


def dele():
    sr = connec()
    try:
        if sr.exists('name'):
            result = sr.delete('name')
            # 输出响应结果，如果删除成功则返回受影响的键数，否则则返回0
            print('已删除', result)
        else:
            print('name 不存在')
    except Exception as e:
        print(e)


def select_allkeys():
    sr = connec()
    try:
        # 获取所有的键
        result = sr.keys()
        # 输出响应结果，所有的键构成⼀个列表，如果没有键则返回空列表
        print(result)
        list_key = []
        for i in result:
            j = i.decode()
            list_key.append(j)
        print(list_key)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    select_allkeys()
    # add()
    # mof()
    # dele()