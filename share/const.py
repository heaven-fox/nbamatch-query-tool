# coding: utf8

BASE_FOLDER = "out"
DATA_FOLDER = "data"
CONF_FOLDER = "conf"
TEAM_FILE = "team.json"
CONF_FILE = "conf.json"

JSON_TEAM_URL = "http://matchweb.sports.qq.com/rank/team?competitionId=100000&from=NBA_PC"
JSON_MATCH_URL = "http://mat1.gtimg.com/apps/hpage2/nbateammatchlist_%d.json"

REFER_URL = "http://nba.stats.qq.com/nba"
USER_AGENT = "Mozilla/5.0(iPad; U; CPU iPhone OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10" \
             " (KHTML, like Gecko) Version/4.0.4 Mobile/7B314 Safari/531.21.10"

# SendCloud API
SEND_CLOUD_API_URL = "http://www.sendcloud.net/webapi/mail.send_template.json"
# SendCloud API_USER
SEND_CLOUD_API_USER = "cls1991_test_BmQKl0"
# SendCloud API_KEY
SEND_CLOUD_API_KEY = "iwJnOYQZzEo3R6GS"

# 查询范围
QUERY_PERIOD = {
    "ALL": 0,             # 全部
    "DAY": 1,             # 当天
    "WEEK": 2,            # 今天开始的一周
    "MONTH": 3            # 今天开始的一个月
}
