# 自訂一個迭代器類別
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    # __iter__ 方法讓這個物件成為「可迭代物件」，必須回傳一個「迭代器物件」
    # 如果物件本身就是迭代器（像這個例子），可以 return self
    def __iter__(self):  
        return self

    # __next__ 方法定義「每次迭代時要回傳的值」
    # 當沒有值可回傳時必須 raise StopIteration
    def __next__(self):
        if self.current < self.end:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

# 使用自訂迭代器
for i in MyRange(0, 3):
    print(i)  # 依序印出 0, 1, 2
