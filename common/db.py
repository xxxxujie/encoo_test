import pymysql


class DataBase:
    def __init__(self, host=None, port=None, user=None, password=None, database=None):
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    database=database)

    def query_one(self, sql):
        cursor = self.conn.cursor()
        # 执行sql语句
        cursor.execute(sql)
        one = cursor.fetchone()
        cursor.close()
        return one

    def query_all(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    from config.setting import Config

    db_config = Config.db
    db = DataBase(
        db_config['host'],
        db_config['port'],
        db_config['user'],
        db_config['password'],
        db_config['database']
    )
    sql = ''
    result = db.query_one(sql)
