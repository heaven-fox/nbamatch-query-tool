# coding: utf8

import os
# 切换工作目录到项目根目录
project = os.path.split(os.path.realpath(__file__))[0]
os.chdir(project)

import lib.crawler as cl


if __name__ == '__main__':
    # 测试用例
    # 当天是否有赛程
    target_team = u"勇士"
    cl.get_matches(target_team, period=1)
