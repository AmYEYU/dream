'''

__author__ = Dc

'''

import pymysql

from utils.settings import DATABASE


class MySqlPipline(object):
    def __init__(self):
        self.host = DATABASE.get('HOST')
        self.port = DATABASE.get('PORT')
        self.username = DATABASE.get('USER')
        self.password = DATABASE.get('PASSWORD')
        self.database = DATABASE.get('NAME')
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, charset='utf8',
                                  port=self.port)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.cursor.close()
        self.db.close()

    def select(self, sql):
        '''
        :param sql:
        :return: tuple
        '''
        try:
            self.cursor.execute(sql)
            fetall = list(self.cursor.fetchall())
            return fetall
        except Exception as e:
            self.db.rollback()
            print(e)

    def _executes(self, sql, item):
        '''

        :param sql:
        :param item:
        if item as list:
            executemany
        else:
            execute
        :return: result
        '''
        if isinstance(item, list):
            result = self.cursor.executemany(sql, item)
        else:
            result = self.cursor.execute(sql, item)
        self.db.commit()
        return result

    def execute_sql(self, sql, item):
        '''
        insert or update or delete
        :param sql:
        :param item:
        :return:
        '''
        try:
            result = self._executes(sql, item)
            return result >= 1
        except Exception as e:
            self.db.rollback()
            print(e)





if __name__ == '__main__':
    pipSql = MySqlPipline()
    pass

