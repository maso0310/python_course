# 建立字典（包含姓名與年齡）
person = {"name": "Alice", "age": 25}

# 存取 value（用 key）
print("姓名：", person["name"])   # Alice

# 新增鍵值對
person["city"] = "Taipei"

# 修改 value
person["age"] = 26

# 刪除鍵值對
del person["city"]

# 使用迴圈
for key, value in person.items():
    print(f"{key}：{value}")
