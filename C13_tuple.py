# 建立 tuple（有序、混合型別、可重複）
info = ("apple", 3.14, True, "apple")

# 使用索引與切片
print("索引 0：", info[0])      # apple
print("切片 [1:3]：", info[1:3])  # (3.14, True)

# 嘗試修改會出錯（不可變）
# info[1] = 100  # TypeError

# 使用 for 迴圈遍歷
for item in info:
    print("項目：", item)

"""
元組(Tuple)的特性：
1.有序
2.不可變
3.允許重覆
4.支援多類別
5.支援切片
6.操作多元
7.可迭代
"""