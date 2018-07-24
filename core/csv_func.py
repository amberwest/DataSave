# -*- coding:utf-8 -*-
# Time: 2018/6/14 09:47
import csv
import time

import sys

from DataSave import error_logger, path


class CsvFunc(object):
    """必须提供csv表头"""
    def __init__(self, columns=None, file_name=None):
        self.file_name = file_name
        if not self.file_name:
            file_name = path + '{}.csv'.format(time.strftime('%Y%m%d'))
        else:
            file_name = path + self.file_name
        file = open(file_name, 'w', newline='', encoding='utf-8')

        self.columns = columns
        if not self.columns:
            error_logger.logger.error("columns is None")
            print('column for csv file is needed')
            sys.exit(1)

        self.writer = csv.DictWriter(file, self.columns)
        self.writer.writeheader()

    def get_columns(self, data):
        """根据数据获取csv表头"""
        if isinstance(data, dict):
            return list(sorted(data.keys()))

    def save(self, data):
        """保存数据"""
        self.writer.writerow(data)