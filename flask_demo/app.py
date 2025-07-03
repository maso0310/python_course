from flask import Flask, render_template
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,                                           # 用於知道目前程式的所在位置，作為找相對路徑的基準點
    static_folder=os.path.join(BASE_DIR, 'static'),     # 實際檔案所在的資料夾
    static_url_path='/static',                          # 對外提供的URL路徑
    template_folder=os.path.join(BASE_DIR, 'templates') # HTML模板所在資料夾路徑
)

@app.route("/")
def home():
    return render_template("index.html")                # 載入 index.html 頁面

if __name__ == "__main__":
    app.run(debug=True)







"""
常見的Python網頁框架有Flask、Django、FastAPI

回應速度:
Django < Flask < FastAPI

支援功能:
Django > Flask > FastAPI
"""