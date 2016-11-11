# coding: utf8

import time
import datetime
import pycurl
from StringIO import StringIO


def get_html(url, user_agent, refer_url):
    """
    curl html
    :param url:
    :param user_agent:
    :param refer_url:
    :return:
    """
    curl = pycurl.Curl()
    curl.setopt(pycurl.USERAGENT, user_agent)
    curl.setopt(pycurl.REFERER, refer_url)

    buffers = StringIO()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEDATA, buffers)
    curl.perform()
    body = buffers.getvalue()
    buffers.close()
    curl.close()

    return body


def time_now_str(format_str="%Y-%m-%d"):
    """
    获取当天时间
    :param format_str:
    :return:
    """
    return time.strftime(format_str, time.localtime())


def datetime_to_str(dt, format_str="%Y-%m-%d"):
    """
    datetime转换字符串
    :param format_str:
    :param dt:
    :return:
    """
    return dt.strftime(format_str)


def get_c_datetime(timedelta=0):
    """
    获取当天之后的时间
    :param timedelta:
    :return:
    """
    date_now = datetime.datetime.now()
    return date_now + datetime.timedelta(days=timedelta)
