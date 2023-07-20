#安装PyQt5
# pip install PyQt5_tools
#然后在D:\learn\Lib\site-packages\qt5_applications\Qt\bin中找到designer.exe
#设计好了UI界面后保存.ui文件，然后cmd命令下pyuic5 -o name.py name.ui(其中name改成.ui的文件名)
#生成代码.py，然后我们在同一个目录下另外创建一个程序叫做“main.py”，作为程序入口
#安装PyQt5doc  即Qt帮助文档
#pip install PyQtdoc
#Qt designer/assistant.exe所在位置 ..\site-packages\qt5_applications\Qt\bin
#Qt assistant帮助文档添加：编辑/首选项/Add..   添加PyQtdoc下的所有qch文档


#sizePolicy:
# sizeHint():期望尺寸，即布局后的默认尺寸
# Fixed: 大小不能改变
# Minimum: 已经是最小, 不能再被缩小, 但能放大.
# Maximum: 已经是最大, 不能再被放大, 但能缩小.
# Preferred: 控件的sizeHint()是他的sizeHint, 能被缩小, 放大.
# Expanding: 控件可以自行增大或者缩小.
# Preferred与Expanding同时存在时，Expanding会变化，Preferred使用sizeHint()不变化


# 输入控件：
#   按钮：QPushButton（按键按钮），QToolButton（工具按钮），QRadioButton（单选框），QCheckButton（多选框），QCommandLinkButton（连接命令的按钮）
#   键盘输入控件：QlineEdit（单行输入），QTextEdit（多行输入），QPlainTextEdit（普通多行输入），QkeySequenceEdit（快捷键输入）
#   调节输入控件：QAbstractSpinBox（步长调节输入），QDateEdit（日期输入），QTimeEdit（时间输入），QDateTimeEdit（日期和时间输入）
#   数字调节框控件：QSpinBox（整型数字调节框），QDoubleSpinBox（浮点数字调节框）
#   滑动输入控件：QDial（旋转拖滑输入），QSlider（直线拖动输入），QScrollBar（滚动条），QRubberBand（橡皮筋拖拽）
#   下拉输入控件：QComboBox（组合框下拉选项），QSlider（直线拖动输入），QScrollBar（滚动条），QRubberBand（橡皮筋拖拽）
#   对话框输入控件：QDialog（对话框），QColorDialog（颜色对话框），QFileDialog（文件对话框），QFontDialog（字体对话框），QInputDialog（输入对话框）
#   日历控件：QCalendarWidget（日期选择部件）
# 显示控件：
#   内容显示控件：QLabel（显示框），QLCDNumber（液晶显示器），QProgressBar（进度条）
#   对话框显示控件：QMessageBox（信息提示框），QErrorMessage（错误提示框），QProgressDialog（进度提示框）
# 高级控件：
#   容器控件：QToolBox，QDialogButtonBox，QGroupBox，QMdiSubWindow
#   结构控件：QMainWindow，QTabwidget，QStackedWidget，QSplitter，QDockWidget
#   滚动控件：QTextBrowser，QScrollArea，QAbstractItemView，QMdiarea，QGraphicsView
#   辅助控件：QFocusFrame，QSizeGrip，QDesktopWidget

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
# from ui.ImageProcess import Ui_MainWindow
from ui.test import Ui_MainWindow
from PyQt5 import QtGui
from datetime import datetime

class MyMainWindow(QMainWindow, Ui_MainWindow):  # 继承 QMainWindow类和 Ui_MainWindow界面类
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类
        self.subwindow.show()
        self.subwindow.show()
        # self.label.setPixmap(QtGui.QPixmap("D:\learn\pythonPractice\PyQt_learn\PyQt5_practice\image\JPEG.png"))
        
    def click_quit(self):
        self.close()

    def trigger_actHelp(self):  # 动作 actHelp 触发
        QMessageBox.about(self, "About","""数字图像处理工具箱 v1.0\nCopyright YouCans, XUPT 2021""")
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 在 QApplication 方法中使用，创建应用程序对象
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口

    # myWin = QMainWindow()
    # ui=Ui_MainWindow()
    # ui.setupUi(myWin)

    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 结束进程，退出程序





