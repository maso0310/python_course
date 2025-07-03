# 取得使用者輸入的 GPA 和最低分數，並轉為浮點數
gpa = float(input('請輸入你的 GPA（平均成績）：'))
lowest_grade = float(input('請輸入你這學期的最低分數：'))

# 檢查是否符合「榮譽榜」的資格
# 條件是 GPA >= 0.85 且最低分 >= 0.7
if gpa >= 0.85 and lowest_grade >= 0.70:
    honour_roll = True  # 布林值：符合資格
else:
    honour_roll = False  # 布林值：不符合資格

# 如果是 True，就印出通過訊息
if honour_roll:
    print('你進入了榮譽榜！')

"""
1.布林值： True(真)、False(假)，開頭大寫
2.實際上，所有條件式都會轉換成布林值
"""