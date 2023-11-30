import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from tool import Ui_MainWindow
import sys
from PyQt5.QtCore import Qt,QPoint,pyqtSignal,pyqtSlot
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget

class MyMainWindow(Ui_MainWindow,QMainWindow):  # 继承 QMainWindow类和 Ui_MainWindow界面类
  def __init__(self):
      super().__init__()  # 初始化父类
      self.setupUi(self)  # 继承 Ui_MainWindow 界面类  
      self.ui_add()

  def ui_add(self):
    # self.setFixedSize(500, 600)
    #设置无边框
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setAttribute(Qt.WA_TranslucentBackground)
    # 初始化鼠标按下的位置
    self.offset = QPoint()

  def mousePressEvent(self, event):
    # 记录鼠标按下时的位置
    self.offset = event.pos()

  def mouseMoveEvent(self, event):
    # 移动窗体位置
    if not self.isMaximized():
      self.move(self.pos() + event.pos() - self.offset)

  # def paintEvent(self, event):
  #     painter = QPainter(self)
  #     painter.setPen(Qt.NoPen)
  #     painter.setBrush(Qt.lightGray)
  #     painter.drawRoundedRect(self.rect(), 10, 10)

  @pyqtSlot()
  def on_pushButton_close_clicked(self):
    self.close()

if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWin = MyMainWindow()  
    myWin.show() 
    sys.exit(app.exec_())  
