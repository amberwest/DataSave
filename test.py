# -*- coding:utf-8 -*-
# Time: 2018/6/8 17:54

from DataSave import MysqlFunc, CsvFunc, ExcelFunc, MongoFunc


if __name__ == '__main__':
    d = {'id': 1447, 'name': '枇杷测试3', 'images': "[{'small': 'https://youtube.com'}]"}

    # m = MysqlFunc()
    # m.insert(d)

    e = ExcelFunc()
    e.save(d)