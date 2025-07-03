# 若要取得目前的日期與時間，我們需要使用 datetime 套件
from datetime import datetime

# now() 函式會回傳目前的日期與時間
today = datetime.now()

# 使用 day, month, year, hour, minute, second 屬性
# 可以只顯示日期或時間的一部分
# 這些屬性會回傳整數
# 在與其他字串結合前，需先轉換為字串格式
print('日期（日）: ' + str(today.day))
print('月份（月）: ' + str(today.month))
print('年份（年）: ' + str(today.year))

print('時間（時）: ' + str(today.hour))
print('分鐘（分）: ' + str(today.minute))
print('秒數（秒）: ' + str(today.second))

"""
1.python當中可用 . 來呼叫特定變數或物件內的屬性值
"""