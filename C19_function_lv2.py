def total_score(*args):
    return sum(args)

print(total_score(80, 90, 70))  # 240

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}：{value}")

show_info(name="Alice", age=20) # name：Alice # age：20

