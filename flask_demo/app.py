from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # 載入 HTML 頁面

if __name__ == "__main__":
    app.run(debug=True)

"""
常見的Python網頁框架有Flask、Django、FastAPI

回應速度:
Django < Flask < FastAPI

支援功能:
Django > Flask > FastAPI
"""