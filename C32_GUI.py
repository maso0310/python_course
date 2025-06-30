# 匯入 tkinter 模組，tk 是它的簡寫別名
import tkinter as tk

# 定義一個函式，按下按鈕時執行，會讀取輸入框的文字並顯示出來
def greet():
    label.config(text="Hello, " + entry.get())

window = tk.Tk()                 # 建立一個主視窗
window.title("簡易互動視窗")      # 設定視窗標題

entry = tk.Entry(window)         # 建立一個輸入框元件，放到視窗中
entry.pack()                     # 自動排列（pack）進視窗

button = tk.Button(window, text="打招呼", command=greet) 
button.pack()                    # 建立一個按鈕，按下時會執行 greet 函式


label = tk.Label(window, text="")# 建立一個標籤元件，用來顯示打招呼的文字
label.pack()

window.mainloop()                # 啟動主事件迴圈，讓視窗保持開啟狀態
