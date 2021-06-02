import sys

from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget,QHBoxLayout, QPushButton,QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.setWindowTitle('标题')

        self.resize(400,300)

        self.button1 = QPushButton('退出应用')
        self.button1.clicked.connect(self.onClick_Button)
        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'123')
        app=QApplication.instance()
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)

   
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())