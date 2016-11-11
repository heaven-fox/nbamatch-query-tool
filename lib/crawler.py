# coding: utf8

from util.common import *


def get_matches(target_team, period=1, is_subscribe=False):
    """
    获取目标球队的比赛日程
    :param target_team: 目标球队
    :param period: 查询范围(默认查询当天的比赛信息)
    :param is_subscribe: 是否邮件订阅
    :return:
    """
    team_info = json.load(open(const.DATA_FOLDER + "/" + const.TEAM_FILE, "r"))
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
    m_day = time_now_str()
    c_month = time_now_str("%Y-%m")
    m_c = None
    if period == const.QUERY_PERIOD["WEEK"]:
        m_c = datetime_to_str(get_c_datetime(timedelta=7))
    elif period == const.QUERY_PERIOD["MONTH"]:
        m_c = datetime_to_str(get_c_datetime(timedelta=30))
    m_result = list()
    m_search_times = 0
    is_finish = False
    match_data = ""
    print("*" * 80)
    for matches in match_info:
        match_month = matches[0].encode("utf8")
        if cmp(c_month, match_month) > 0:
            continue
        for a_match in matches[1]:
            match_day = a_match["startTime"][:10]
            if cmp(m_day, match_day) > 0:
                continue
            if period == const.QUERY_PERIOD["ALL"]:
                m_result.append((a_match["startTime"], a_match['rightName'], a_match["leftName"]))
            elif period == const.QUERY_PERIOD["DAY"]:
                m_search_times += 1
                if cmp(m_day, match_day) == 0:
                    m_result.append((a_match["startTime"], a_match['rightName'], a_match["leftName"]))
                    break
                elif cmp(m_day, match_day) < 0:
                    break
            elif period in (const.QUERY_PERIOD["WEEK"], const.QUERY_PERIOD["MONTH"]):
                m_search_times += 1
                if cmp(m_c, match_day) < 0:
                    break
                elif cmp(m_day, match_day) <= 0 and cmp(m_c, match_day) >= 0:
                    m_result.append((a_match["startTime"], a_match['rightName'], a_match["leftName"]))

        if period == const.QUERY_PERIOD["DAY"]:
            if m_search_times >= 1:
                is_finish = True
        elif period in (const.QUERY_PERIOD["WEEK"], const.QUERY_PERIOD["MONTH"]):
            if m_search_times >= 2:
                is_finish = True
        if m_result:
            print("比赛月份: " + matches[0].encode("utf8"))
            print("开始时间\t\t主队\t\t客队")
            match_data += "比赛月份: " + matches[0].encode("utf8") + "\n"
            match_data += "开始时间\t\t主队\t\t客队" + "\n"
            for a_info in m_result:
                print(a_info[0] + "\t\t" + a_info[1] + "\t\t" + a_info[2])
                match_data += "\t\t".join(a_info).encode("utf8") + "\n"
        m_result[:] = list()
        if is_finish:
            break
    print("*" * 80)
    # 是否订阅
    if is_subscribe and match_data:
        send_mail(match_data)


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
