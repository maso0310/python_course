count = 0

while count < 10:
    count += 1

    if count == 5:
        print("跳過 5")
        continue  # 跳過這次，不印出 5

    if count == 8:
        print("遇到 8，結束迴圈")
        break  # 直接終止整個迴圈

    print("目前數字：", count)
