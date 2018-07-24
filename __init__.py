# -*- coding:utf-8 -*-
# Time: 2018/6/12 09:53
import os

BASE_DIRNAME = os.path.abspath(os.path.dirname(__file__))

from DataSave.utils.log import debug_logger, error_logger
from DataSave.utils.tools import dir_exist
from DataSave.utils.config import load_config

path = os.path.join(BASE_DIRNAME, 'data/')
dir_exist(path)
# 因为cofing在core里多次被引用，所以config要在导入CsvFunc等之前先定义
config = load_config()

from DataSave.core.csv_func import CsvFunc
from DataSave.core.excel_func import ExcelFunc
from DataSave.core.mysql import MysqlFunc
from DataSave.core.mongo_func import MongoFunc


__all__ = [CsvFunc, ExcelFunc, MysqlFunc, config, MongoFunc]
