#导入模块
import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == '__main__':
    #创建QApplication类的实例
    app = QApplication(sys.argv)
    #创建一个窗口
    w = QWidget()
    #窗口尺寸
    w.resize(300,150)
    #移动窗口
    w.move(300,300)

    #窗口标题
    w.setWindowTitle('第一个桌面应用')
    w.show()

    #进入程序的主循环,通过exit函数确保安全结束
    sys.exit(app.exec_())