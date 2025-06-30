def decorator_one(func):
    def wrapper():
        print("🟠 裝飾器一：前置作業")
        func()
        print("🟠 裝飾器一：後置清理")
    return wrapper

def decorator_two(func):
    def wrapper():
        print("🔵 裝飾器二：開始執行")
        func()
        print("🔵 裝飾器二：執行結束")
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("👋 哈囉，Python 世界！")

greet()
# 🟠 裝飾器一：前置作業
# 🔵 裝飾器二：開始執行
# 👋 哈囉，Python 世界！
# 🔵 裝飾器二：執行結束
# 🟠 裝飾器一：後置清理
