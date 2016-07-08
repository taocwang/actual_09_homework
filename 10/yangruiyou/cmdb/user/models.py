from dbutils import MySQLConnection


class User(object):
    def __init__(self, user_id, username, passwd, age):
        self.user_id = user_id
        self.username = username
        self.passwd = passwd
        self.age = age

    @classmethod
    def validate_login(cls, username, password):
        _columns = ('id', 'username')
        _sql = 'select * from user where username=%s and password=md5(%s)'
        _count, _rt_list = MySQLConnection.execute_sql(_sql, (username, password))
        return dict(zip(_columns, _rt_list[0])) if _count != 0 else None



    @classmethod
    def get_list(cls, wheres=[]):
        _columns = ('id', 'username', 'password', 'age')
        _sql = 'select * from user where 1=1'
        _args = []
        for _key, _value in wheres:
            _sql += 'AND {key} = %s'.format(key=_key)
            _args.append(_value)

        _count, _rt_list = MySQLConnection.execute_sql(_sql, _args)
        _rt = []
        for _line in _rt_list:
            _rt.append(dict(zip(_columns, _line)))
        return _rt




if __name__ == '__main__':
    print User.validate_login('kk', '123456')
