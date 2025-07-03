def my_decorator(func):
    def wrapper():
        print("✨ 執行前的準備")
        func()
        print("✅ 執行後的清理")
    return wrapper

@my_decorator
def say_hello():
    print("👋 哈囉，Python！")

say_hello()
# ✨ 執行前的準備
# 👋 哈囉，Python！
# ✅ 執行後的清理

"""
1.裝飾器就是一個吃函數當參數的函數，是讓你把特定函數放在另一個函數內執行
2.裝飾器用 @ 外掛在目標函數上，使其被呼叫時在裝飾器內執行
"""