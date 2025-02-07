#!/usr/bin/python
# -*- coding: utf8 -*-
# cp936

import logging
import traceback
import time
import functools


# 统计函数运行时间
def spend_time(func):
    @functools.wraps(func)
    def wrappedFunc(*args, **kargs):
        starttime = time.time()
        try:
            print("\nCalling: %s" % func.__name__)
            return func(*args, **kargs)
        finally:
            endtime = time.time()
            print("spend time: %.4fs, %.2fm" % (endtime - starttime, (endtime - starttime) / 60))

    return wrappedFunc


FORMAT = '%(asctime)-15s [%(levelname)s] %(message)s [%(name)s::%(funcName)s]'
logging.basicConfig(format=FORMAT, level=logging.INFO)

hku_logger_name = 'hikyuu'
hku_logger = logging.getLogger(hku_logger_name)


def get_default_logger():
    return logging.getLogger(hku_logger_name)


def class_logger(cls, enable=False):
    #logger = logging.getLogger("{}.{}".format(cls.__module__, cls.__name__))
    logger = logging.getLogger("{}".format(cls.__name__))
    if enable == 'debug':
        logger.setLevel(logging.DEBUG)
    elif enable == 'info':
        logger.setLevel(logging.INFO)
    cls._should_log_debug = logger.isEnabledFor(logging.DEBUG)
    cls._should_log_info = logger.isEnabledFor(logging.INFO)
    cls.logger = logger


def add_class_logger_handler(class_list, level=logging.INFO, handler=None):
    """为指定的类增加日志 handler，并设定级别

    :param class_list: 类列表
    :param level: 日志级别
    :param handler: logging handler
    """
    for cls in class_list:
        #logger = logging.getLogger("{}.{}".format(cls.__module__, cls.__name__))
        logger = logging.getLogger("{}".format(cls.__name__))
        if handler:
            logger.addHandler(handler)
        logger.setLevel(level)


def hku_debug(msg, *args, **kwargs):
    st = traceback.extract_stack()[-2]
    logger = kwargs.pop("logger") if "logger" in kwargs else None
    if logger:
        logger.debug("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
    else:
        hku_logger.debug("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))


hku_trace = hku_debug


def hku_info(msg, *args, **kwargs):
    st = traceback.extract_stack()[-2]
    logger = kwargs.pop("logger") if "logger" in kwargs else None
    if logger is not None:
        logger.info("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
    else:
        hku_logger.info("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))


def hku_warn(msg, *args, **kwargs):
    st = traceback.extract_stack()[-2]
    logger = kwargs.pop("logger") if "logger" in kwargs else None
    if logger:
        logger.warning("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
    else:
        hku_logger.warning("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))


def hku_error(msg, *args, **kwargs):
    st = traceback.extract_stack()[-2]
    logger = kwargs.pop("logger") if "logger" in kwargs else None
    if logger:
        logger.error("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
    else:
        hku_logger.error("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))


def hku_fatal(msg, *args, **kwargs):
    st = traceback.extract_stack()[-2]
    logger = kwargs.pop("logger") if "logger" in kwargs else None
    if logger:
        logger.critical("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
    else:
        hku_logger.critical("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))


def hku_debug_if(exp, msg, *args, **kwargs):
    if exp:
        st = traceback.extract_stack()[-2]
        logger = kwargs.pop("logger") if "logger" in kwargs else None
        callback = kwargs.pop("callback") if "callback" in kwargs else None
        if logger:
            logger.info("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        else:
            hku_logger.info("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        if callback:
            callback()


hku_trace_if = hku_debug_if


def hku_info_if(exp, msg, *args, **kwargs):
    if exp:
        st = traceback.extract_stack()[-2]
        logger = kwargs.pop("logger") if "logger" in kwargs else None
        callback = kwargs.pop("callback") if "callback" in kwargs else None
        if logger:
            logger.info("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        else:
            hku_logger.info("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        if callback:
            callback()


def hku_warn_if(exp, msg, *args, **kwargs):
    if exp:
        st = traceback.extract_stack()[-2]
        logger = kwargs.pop("logger") if "logger" in kwargs else None
        callback = kwargs.pop("callback") if "callback" in kwargs else None
        if logger:
            logger.warning("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        else:
            hku_logger.warning("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        if callback:
            callback()


def hku_error_if(exp, msg, *args, **kwargs):
    if exp:
        st = traceback.extract_stack()[-2]
        logger = kwargs.pop("logger") if "logger" in kwargs else None
        callback = kwargs.pop("callback") if "callback" in kwargs else None
        if logger:
            logger.error("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        else:
            hku_logger.error("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        if callback:
            callback()


def hku_fatal_if(exp, msg, *args, **kwargs):
    if exp:
        st = traceback.extract_stack()[-2]
        logger = kwargs.pop("logger") if "logger" in kwargs else None
        callback = kwargs.pop("callback") if "callback" in kwargs else None
        if logger:
            logger.critical("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        else:
            hku_logger.critical("{} [{}] ({}:{})".format(msg.format(*args, **kwargs), st.name, st.filename, st.lineno))
        if callback:
            callback()


# 跟踪函数运行
def with_trace(level=logging.INFO):
    def with_trace_wrap(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            hku_info('start run: %s' % func.__name__)
            result = func(*args, **kwargs)
            hku_info('completed: %s' % func.__name__)
            return result

        return wrapper

    return with_trace_wrap


def capture_multiprocess_all_logger(queue, level=None):
    """重设所有子进程中的 logger 输出指定的 queue，并重设level
    
    @param multiprocessing.Queue queue 指定的 mp Queue
    @param level 日志输出等级, None为保持原有等级
    """
    if queue is None:
        return
    qh = logging.handlers.QueueHandler(queue)
    for name in logging.Logger.manager.loggerDict.keys():
        logger = logging.getLogger(name)
        logger.addHandler(qh)
        if level is not None:
            logger.setLevel(level)

# Temporary change logger level
# https://docs.python.org/3/howto/logging-cookbook.html
class LoggingContext:
    def __init__(self, logger, level=None, handler=None, close=True):
        self.logger = logger
        self.level = level
        self.handler = handler
        self.close = close

    def __enter__(self):
        if self.level is not None:
            self.old_level = self.logger.level
            self.logger.setLevel(self.level)
        if self.handler:
            self.logger.addHandler(self.handler)

    def __exit__(self, et, ev, tb):
        if self.level is not None:
            self.logger.setLevel(self.old_level)
        if self.handler:
            self.logger.removeHandler(self.handler)
        if self.handler and self.close:
            self.handler.close()
