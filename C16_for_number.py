for num in range(1, 11):
    if num == 5:
        print("跳過 5")
        continue  # 跳過這次，進入下一輪

    if num == 8:
        print("遇到 8，停止迴圈")
        break  # 中止整個迴圈

    print("目前數字：", num)
