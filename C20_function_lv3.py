# 定義函數：計算價格，折扣預設為 0.9（即 9 折）
def calculate_price(original_price, discount=0.9):
    final_price = original_price * discount
    return final_price

# 呼叫範例
print("原價 100，預設折扣：", calculate_price(100))         # 90.0
print("原價 200，自訂 8 折：", calculate_price(200, 0.8))   # 160.0
