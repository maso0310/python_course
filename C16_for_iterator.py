fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("我喜歡吃：", fruit)


# 我喜歡吃： apple
# 我喜歡吃： banana
# 我喜歡吃： cherry

info = {"name": "Alice", "age": 25}

for key, value in info.items():
    print(f"{key}：{value}")

# name：Alice
# age：25


"""
1.in 之後要放「可迭代物件」，for 之後是自定義的「迭代變數」
2.每次迭代會自動取出下一個，直到沒有下一個物件為止
"""