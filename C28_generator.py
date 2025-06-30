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
