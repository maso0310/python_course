# 生成器函數：每次 yield 一個值
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# 呼叫生成器函數
gen = countdown(3)
print(gen) 
# <generator object countdown at 0x0000024025E96140>
# gen 會被組成一個可迭代物件

for num in gen:
    print(num)  
# 每次迴圈從 gen 取出一個值
# 依序印出 3, 2, 1

"""
1.生成器由 yield 與迴圈所組成，目標是遞迴性地生成性質類似的值或物件
2.生成器常被用來作為「資料逐筆釋放」用途，處理大量資料時使用
"""