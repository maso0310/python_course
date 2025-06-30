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
