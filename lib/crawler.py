# coding: utf8

import json

from share import const
from util.common import *


def get_matches(target_team):
    """
    获取目标球队的比赛日程
    :param target_team: 目标球队
    :return:
    """
    team_info = json.load(open(const.DATA_FOLDER + "/" + const.TEAM_FILE))
    team_id = 0
    for a_team in team_info:
        if target_team == a_team["name"]:
            team_id = int(a_team["teamId"])
            break
    if not team_id:
        return
    # 获取球队赛程信息
    html = get_html(const.JSON_MATCH_URL % team_id, const.USER_AGENT, const.REFER_URL)
    m1 = html[12:-1]
    match_info = json.loads(m1)
    match_info = sorted(match_info.iteritems(), key=lambda x: x[0])
    print("*" * 40)
    for matches in match_info:
        print("比赛月份: " + matches[0].encode("utf8"))
        print("开始时间\t\t主队\t\t客队")
        for a_match in matches[1]:
            print(a_match["startTime"] + "\t\t" + a_match['rightName'] + "\t\t" + a_match["leftName"])
    print("*" * 40)


def generate_team_data():
    """
    生成球队索引表(teamId, enName, name三元组)
    :return:
    """
    data = json.loads(get_html(const.JSON_TEAM_URL, const.USER_AGENT, const.REFER_URL))
    if data:
        result = list()
        for teams in data[1].values():
            for item in teams:
                if isinstance(item, dict):
                    result.append({
                        "teamId": item["teamId"],
                        "enName": item["enName"],
                        "name": item["name"]
                    })
        if result:
            with open(const.DATA_FOLDER + "/" + const.TEAM_FILE, "w") as f:
                f.write(json.dumps(result))
