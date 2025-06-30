# 建立 set（自動去除重複）
fruits = {"apple", "banana", "apple", "cherry"}
print("原始集合：", fruits)  # {'banana', 'cherry', 'apple'}，順序可能不同

# 新增與刪除元素
fruits.add("durian")
fruits.remove("banana")
print("更新後集合：", fruits)

# 使用迴圈
for f in fruits:
    print("水果：", f)

# 集合運算
a = {1, 2, 3}
b = {2, 3, 4}
print("交集：", a & b)   # {2, 3}
print("聯集：", a | b)   # {1, 2, 3, 4}
print("差集：", a - b)   # {1}
print("對稱差集：", a ^ b)  # {1, 4}
