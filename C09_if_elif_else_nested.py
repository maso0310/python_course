# 讓使用者輸入所在國家
country = input("你住在哪一個國家？ ")

# 第一層條件：若國家是加拿大（不分大小寫）
if country.lower() == 'canada':
    # 讓使用者輸入省份
    province = input("請輸入你住的省份或州名： ")

    # 第二層條件：根據不同省份給稅率
    if province in ('Alberta', 'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    # 如果不是加拿大，就不收稅
    tax = 0.0

# 印出稅率
print(tax)

"""
1.若有多層判斷式，則縮排部分也需要多一層來表示
2.加入 elif 可以建立多個判斷條件
"""