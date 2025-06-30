# 匯入 datetime 模組中的 datetime 類別與 timedelta 類別
from datetime import datetime, timedelta

# 取得目前的日期與時間
today = datetime.now()
print('今天是：' + str(today))

# 建立一個代表一天的時間差物件
one_day = timedelta(days=1)
# 今天減一天，就是昨天
yesterday = today - one_day
print('昨天是：' + str(yesterday))

# 建立一個代表一週的時間差物件
one_week = timedelta(weeks=1)
# 今天減一週，就是上週同一天
last_week = today - one_week
print('上週的今天是：' + str(last_week))
