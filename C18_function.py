# 定義函數：傳入學生姓名與分數，回傳評語字串
def evaluate_student(name, score):
    if score >= 90:
        grade = "優秀"
    elif score >= 75:
        grade = "良好"
    elif score >= 60:
        grade = "及格"
    else:
        grade = "需要加強"
    
    return f"{name} 的分數是 {score}，表現：{grade}"

# 呼叫函數（可以重複使用）
print(evaluate_student("Alice", 92))
print(evaluate_student("Bob", 78))
print(evaluate_student("Charlie", 59))
