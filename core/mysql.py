# -*- coding:utf-8 -*-
# Time: 2018/6/12 11:00
import pymysql
import sys
from pymysql.err import OperationalError, InternalError

from DataSave import config, debug_logger, error_logger


class MysqlFunc(object):
    """
    确保存放数据的数据库和表格都已经建立，传入的data类型是字典，关于数据库链接要在配置文件中进行修改
    最后要记得调用关闭函数
    """
    def __init__(self):
        self.user = config.get('sql_user')
        self.password = config.get('sql_password')
        self.host = config.get('sql_host')
        self.port = config.get('sql_port')
        self.database = config.get('sql_database')
        self.charset = config.get('sql_charset')
        self.table = config.get('sql_table')
        self.engine()

    def engine(self):
        """数据库连接失败时退出"""
        try:
            self.db = pymysql.connect(host=self.host, user=self.user, password=self.password, port=int(self.port),
                                      db=self.database, charset=self.charset)
            self.cursor = self.db.cursor()
            debug_logger.logger.debug('connect to mysql successfully')
        except OperationalError as e:
            error_logger.logger.error(e)
            sys.exit(1)

    def insert(self, data, table=None):
        """没有提供表名则使用默认的"""
        if not table:
            table = self.table
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
        update = ','.join([" {key} = %s".format(key=key) for key in data])
        sql += update
        try:
            self.cursor.execute(sql, tuple(data.values()) * 2)
            self.db.commit()
            debug_logger.logger.debug('Insert Successfully %s' % data)
        except Exception as e:
            debug_logger.logger.debug('Insert Failed', data)
            error_logger.logger.error(e)
            self.db.rollback()

    def edit(self, sql):
        """根据提供的sql语句进行更新或者删除"""
        try:
            self.cursor.execute(sql)
            debug_logger.logger.debug('Update Successfully')
            self.db.commit()
        except InternalError as e:
            debug_logger.logger.debug('Edit Failed')
            error_logger.logger.error(e)
            self.db.rollback()
        except Exception as e:
            error_logger.logger.error(e)

    def close(self):
        """关闭数据库"""
        self.db.close()

if __name__ == '__main__':
    m = MysqlFunc()
    d = {'id': 1445, 'name': '枇杷', 'images': "[{'small': 'https://youtube.com'}]"}
    m.insert(d)