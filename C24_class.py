# 定義一個學生類別
class Student:
    def __init__(self, name, score):
        self.name = name        # 實例變數
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"

# 建立學生物件並呼叫方法
s1 = Student("Alice", 92)
s2 = Student("Bob", 75)

print(f"{s1.name} 的等級是 {s1.get_grade()}")  # Alice 的等級是 A
print(f"{s2.name} 的等級是 {s2.get_grade()}")  # Bob 的等級是 B
