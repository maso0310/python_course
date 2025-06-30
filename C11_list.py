# 建立一個列表（有序、可重複、混合型別）
data = ["apple", "banana", "apple", 42, True]

# 可透過索引與切片存取
print("索引 0：", data[0])        # apple
print("切片 [1:4]：", data[1:4])  # ['banana', 'apple', 42]

# 可修改、可新增、可刪除
data[1] = "grape"
data.append("new")
data.remove(42)
print("修改後的列表：", data)

# 可用迴圈逐一列出
for item in data:
    print("項目：", item)
