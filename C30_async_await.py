import asyncio

async def task(name, delay):
    print(f"🔧 開始任務：{name}")
    await asyncio.sleep(delay)  # 模擬等待的時間（不阻塞整體流程）
    print(f"✅ 完成任務：{name}，花費 {delay} 秒")

async def main():
    # 同時啟動三個協程任務
    await asyncio.gather(
        task("下載圖片", 3),
        task("讀取資料庫", 2),
        task("寫入日誌", 1)
    )

asyncio.run(main())
# 🔧 開始任務：下載圖片
# 🔧 開始任務：讀取資料庫
# 🔧 開始任務：寫入日誌
# ✅ 完成任務：寫入日誌，花費 1 秒
# ✅ 完成任務：讀取資料庫，花費 2 秒
# ✅ 完成任務：下載圖片，花費 3 秒
