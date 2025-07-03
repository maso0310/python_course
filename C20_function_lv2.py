def total_score(*args):
    return sum(args)

print(total_score(80, 90, 70))  # 240

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}：{value}")

show_info(name="Alice", age=20) # name：Alice # age：20

"""
1.參數使用單星號 * ，代表可接收不固定數量的參數，全部都會被包成一整個tuple
2.使用雙星號 ** 代表接受由呼叫端鍵值定義的多個參數
"""