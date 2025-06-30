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



if x > 0: 
    print("正數") 
else
    print("其他")

if x > 0:
print("正數")
elif x == 0: 
print("零")

if x > 0: 
    print("正數") 
elif x == 0: 
    print("零")

if x > 0 
    then print("正數")
elif x == 0
    then print("零")