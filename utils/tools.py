# -*- coding:utf-8 -*-
# Time: 2018/6/12 16:00
import os

def dir_exist(path):
    if not os.path.exists(path):
        os.mkdir(path)