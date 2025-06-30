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
