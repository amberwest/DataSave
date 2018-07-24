# -*- coding:utf-8 -*-
# Time: 2018/6/12 10:46
import os

def load_config():
    config_path = os.path.join('/Users/amber/Projects/PycharmProject/DataSave', 'config.txt')

    with open(config_path, encoding='utf8') as f:
        config = f.readlines()

    config_list = [x for x in config if "=" in x]

    return {
        x.split('=')[0]: x.split('=')[1].strip() for x in config_list
    }
