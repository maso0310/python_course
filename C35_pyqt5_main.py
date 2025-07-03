import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from C34_pyqt5_ui import Ui_MainWindow  # 匯入剛才產生的 UI 類別

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()         # 建立 UI 實例
        self.ui.setupUi(self)             # 初始化 UI 畫面（將元件放到視窗上）

        # 加入你自己的邏輯，例如按鈕點擊事件
        self.ui.pushButton.clicked.connect(self.say_hello)

    def say_hello(self):
        QMessageBox.information(self, "提示", "你點了按鈕！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
