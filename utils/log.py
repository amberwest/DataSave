# -*- coding:utf-8 -*-
# Time: 2018/6/12 09:09
import logging
import logging.config

import os

from DataSave import BASE_DIRNAME

class LoggerConfig(object):
    LOG_BASE_DIRNAME = os.path.join(BASE_DIRNAME, 'log')
    if not os.path.exists(LOG_BASE_DIRNAME):
        os.mkdir(LOG_BASE_DIRNAME)

    # 定义日志输出格式
    DATEFMT = '%Y-%m-%d %H:%M:%S'
    STANDARD_FORMAT = '%(asctime)s %(filename)s-[line:%(lineno)d] %(levelname)s %(message)s'

    # log配置字典handlers，filters，formatters和loggers四大组件
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        # 配置formatter
        'formatters': {
            'standard': {
                'format': STANDARD_FORMAT,
                'datefmt': DATEFMT,
            }
        },

        # 配置filters
        'filters': {},

        # 配置handlers
        'handlers': {
            # 打印到终端的日志
            'console': {
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler'
            },
            'debug': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join(LOG_BASE_DIRNAME, 'debug.log'),
                'encoding': 'utf8',
                'maxBytes': 10 * 1024 * 1024,
                'backupCount': 2
            },
            'error': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'standard',
                'filename': os.path.join(LOG_BASE_DIRNAME, 'error.log'),
                'encoding': 'utf8',
                'maxBytes': 10 * 1024 * 1024, 'backupCount': 2
            }
        },

        # 配置logger
        'loggers': {
            'base_debug': {
                # 调用base_debug，不仅会将调试信息写入文件还会输出到控制台
                'handlers': ['console', 'debug'],
                'level': 'DEBUG',
            },
            'base_error': {
                'handlers': ['error'],
                'level': 'ERROR',
            }
        },

    }

class Logger(object):
    def __init__(self, logger_name):
        logging.config.dictConfig(LoggerConfig.LOGGING)
        self.logger = logging.getLogger(logger_name)

debug_logger = Logger('base_debug')
error_logger = Logger('base_error')

if __name__ == '__main__':
    debug_logger.logger.info('*****test******')
