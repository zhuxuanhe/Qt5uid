import sys

from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget

from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        #set title
        self.setWindowTitle('标题')

        self.resize(400,300)

        self.status = self.statusBar()
        self.status.showMessage('xiaoxi',5000)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        
        size = self.geometry()
        newLeft = int((screen.width()-size.width())/2)
        newTop = int((screen.height()-size.height())/2)
        self.move(newLeft,newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./img/favicon.ico'))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())