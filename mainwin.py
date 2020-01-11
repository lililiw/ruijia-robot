import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QApplication
# 以下五个文件为pyuic生成的.py文件，注意修改里面类的名字不要重复
from mwinsam1 import  sub1_MainWindow
from mwinsam2 import sub2_MainWindow
from mwinsam3 import sub3_MainWindow




# class MyMainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(MyMainWindow, self).__init__(parent)
#         self.setupUi(self)
#         self.center()
#     def center(self):
#         screen = QDesktopWidget().screenGeometry()
#         size = self.geometry()
#         self.move((screen.width() - size.width()) / 2,  (screen.height() - size.height()) / 2)

class Mywindow1(QMainWindow):
    def __init__(self):
        super(Mywindow1, self).__init__()
        self.ui = sub1_MainWindow()  # 这句话是实例化类
        self.ui.setupUi(self)  # 这句话相当于设置控件

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()
class Mywindow2(QMainWindow):
    def __init__(self):
        super(Mywindow2, self).__init__()
        self.ui = sub2_MainWindow()  # 这句话是实例化类
        self.ui.setupUi(self)  # 这句话相当于设置控件

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()

class Mywindow3(QMainWindow):
    def __init__(self):
        super(Mywindow3, self).__init__()
        self.ui = sub3_MainWindow()  # 这句话是实例化类
        self.ui.setupUi(self)  # 这句话相当于设置控件

    def open(self):  # 被调用的类需要再编写一个open函数
        self.show()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 实例化各个类
    w1 = Mywindow1()
    w2 = Mywindow2()
    w3 = Mywindow3()

    # 将主窗口进行展示调用
    w1.show()
    # 主窗口与子窗口1，2使用connect方法连接起来
    w1.ui.pushButton.clicked.connect(w2.open)
    w1.ui.pushButton_2.clicked.connect(w3.open)
    # 子窗口1与子窗口1-1使用connect方法连接起来

    sys.exit(app.exec_())

