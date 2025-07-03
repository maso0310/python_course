def divide(a, b):
    return a / b

# 測試資料
x = 10
y = 0  # 故意設為 0 來觸發錯誤

try:
    result = divide(x, y)
except ZeroDivisionError:
    print("❗ 錯誤：除數不能為 0")
else:
    print(f"✅ 結果是：{result}")
finally:
    print("🔚 程式執行完畢")

"""
1.try區域為可能出錯的程式
2.except為錯誤發生後的執行程序
3.else為沒有錯誤發生的執行程序
4.finally為不論如何都接著執行
"""