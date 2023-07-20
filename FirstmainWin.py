import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QWidget,QToolTip
from  PyQt5.QtGui import QIcon,QFont

class FirstMainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('第一个主窗口应用')
        self.resize(400,300)
        # self.status=self.statusBar()
        # self.status.showMessage('只存在5S的消息',5000)
        btn=QPushButton(self,text='haha')
        # QToolTip.setFont(QFont('SansSerif',12))
        btn.setToolTip('今天是<b>星期五<b>')
        btn.clicked.connect(self.onclick_btn)
    
    def onclick_btn(self):
        print('widget.x=%d' % self.x())
        print('widget.y=%d' % self.y())
    
if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./ico/1.ico'))
    main=FirstMainWin()
    main.show()
    sys.exit(app.exec_())
