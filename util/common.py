# coding: utf8

import time
import datetime
import json
import requests
import pycurl
from StringIO import StringIO

from share import const

mail_conf = json.load(open(const.CONF_FOLDER + "/" + const.CONF_FILE, "r"))


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


def send_mail(match_data):
    """
    发送邮件通知
    :param match_data:
    :return:
    """
    email = mail_conf["mail_to"]
    nickname = email.split("@")[0]
    request_date = datetime_to_str(datetime.datetime.now())
    # 发送邮件
    sub_vars = {
        'to': [email],
        'sub': {
            "%nickname%": [nickname],
            "%match_data%": [match_data],
            "%send_date%": [request_date]
        }
    }
    params = {
        "api_user": const.SEND_CLOUD_API_USER,
        "api_key": const.SEND_CLOUD_API_KEY,
        "template_invoke_name": "nba_match_query",
        "substitution_vars": json.dumps(sub_vars),
        "from": mail_conf["mail_from"],
        "resp_email_id": "true",
    }

    r = requests.post(const.SEND_CLOUD_API_URL, data=params)
    response = json.loads(r.text.encode('utf8'))
    if response['message'] == 'success':
        return True
    print('send_mail_fail:', r.text)
    return False
