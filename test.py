from PyQt5 import QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.mdi_area = QtWidgets.QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # 创建第一个子窗口
        sub_window_1 = QtWidgets.QMdiSubWindow()
        widget=QtWidgets.QWidget()
        self.verticalLayout = QtWidgets.QVBoxLayout(widget)
        self.label=QtWidgets.QLabel(widget)
        self.label.setText('Sub Window 1')
        self.textEdit=QtWidgets.QTextEdit(widget)
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.textEdit)
        sub_window_1.setWidget(widget)
        # sub_window_1.setWidget(QtWidgets.QLabel('Sub Window 1'))
        self.mdi_area.addSubWindow(sub_window_1)

        # 创建第二个子窗口
        sub_window_2 = QtWidgets.QMdiSubWindow()
        sub_window_2.setWidget(QtWidgets.QLabel('Sub Window 2'))
        self.mdi_area.addSubWindow(sub_window_2)

        # 显示主窗口和子窗口
        self.show()
        sub_window_1.show()
        sub_window_2.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    app.exec_()
