# Python 3.10+ 才支援此語法
command = "start"

match command:
    case "start":
        print("開始執行程式")
    case "stop":
        print("停止程式")
    case "pause":
        print("暫停中")
    case _:
        print("未知指令")



"""
1.每個case都是一個條件判斷式，也都需要加上冒號 ： 
2.match-case是3.10版之後的功能
"""