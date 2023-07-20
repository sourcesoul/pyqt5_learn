import sys,os
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QFileDialog,QRadioButton,QAbstractButton,QDialog,QMdiSubWindow
from PyQt5.QtCore import QObject,pyqtSignal,pyqtSlot,Qt,QTimer
from ui.demo import Ui_MainWindow
from PyQt5 import QtGui
import time 
import threading
import ui.PLT_Form as my_plt
import ui.MDI_Form as my_mdi
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QMainWindow, QWidget
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.buf = ""

    def write(self, string):
        try:
            self.buf += string
            if '\n' in self.buf:
                self.flush()
        except:
            pass

    def flush(self):
        try:
        # self.text_widget.append(self.buf)
            self.text_widget.insertPlainText(self.buf)
            self.text_widget.moveCursor(self.text_widget.textCursor().End)
            self.buf = ""
        except:
            pass

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
    
#QDialog是一种特殊的窗口，它在显示时会自动禁用父窗口，如果需要同时使用父窗口，使用QWidget
class PLT_Form(my_plt.Ui_Form,QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.addui()

    def addui(self):
        self.addmatplotlib()

    def addmatplotlib(self):
        self.drawing =False
        # 创建Matplotlib图形
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title("Curve")
        self.ax.set_xlabel('time/s')
        self.ax.set_ylabel('Temperature(℃)')
        self.ax.set_ylim([0, 320])
        self.ax.set_xlim([0, 520])
        self.ax.set_yticks(range(0, 340, 20))
        self.ax.set_xticks(range(0, 540, 20))
        self.ax.set_yticklabels(self.ax.get_yticks(), fontsize=6)
        self.ax.set_xticklabels(self.ax.get_xticks(), fontsize=6)
        self.ax.grid(ls='--', lw=0.5, c='grey')
        self.ax.margins(1)
        self.x_data,self.y_data=[],[]
        # 将Matplotlib图形作为QWidget添加到布局中
        self.canvas = FigureCanvas(self.fig)
        vbox = QVBoxLayout(self.widget)
        vbox.addWidget(self.canvas)
        # self.widget.setLayout(vbox)

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.startDraw_time=time.time()
        self.x_data.clear()
        self.y_data.clear()
        if self.drawing is False:
            self.task=threading.Thread(target=self.draw)
            self.task.daemon=True
            self.task.start()

    def draw(self):
        self.drawing=True
        while self.drawing:
            time.sleep(1)
            real_time=time.time()
            interval=real_time-self.startDraw_time
            temp=np.random.randint(0,300)
            self.x_data.append(interval)
            self.y_data.append(temp)
            self.ax.clear()
            self.ax.set_title("Curve")
            self.ax.set_xlabel('time/s')
            self.ax.set_ylabel('Temperature(℃)')
            self.ax.set_ylim([0, 320])
            self.ax.set_xlim([0, 100])
            self.ax.set_yticks(range(0, 340, 20))
            self.ax.set_xticks(range(0, 100, 10))
            self.ax.set_yticklabels(self.ax.get_yticks(), fontsize=6)
            self.ax.set_xticklabels(self.ax.get_xticks(), fontsize=6)
            self.ax.grid(ls='--', lw=0.5, c='grey')
            self.ax.plot(self.x_data,self.y_data,c='r',label='Temp 1')
            self.ax.legend(loc="upper right")
            self.fig.canvas.draw()
        
    @pyqtSlot() 
    def on_pushButton_4_clicked(self):
        # self.task.join(timeout=1)
        self.drawing=False
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.timer = QTimer(self)
        self.timer1=QTimer(self)
        self.timer.timeout.connect(self.updateLabel)
        self.timer1.singleShot(2000,self.updatebutton)
        self.label.setText('0')
        self.timer.start(1000)
    
    def updateLabel(self):
        self.label.setText(str(int(self.label.text())+1))

    def updatebutton(self):
        self.pushButton_2.setText('2s后触发')

class MDI_Form(my_mdi.Ui_Form,QWidget):
    check_changed = pyqtSignal(bool)
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.addui()

    def addui(self):
        self.Qsubwindow=QtWidgets.QMdiSubWindow()
        self.Qsubwindow.setWidget(self.subwindow)
        self.mdiArea.addSubWindow(self.Qsubwindow)
        self.Qsubwindow.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.subwindow = QtWidgets.QWidget()
        self.subwindow.setObjectName("subwindow")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.subwindow)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.subwindow)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.textEdit = QtWidgets.QTextEdit(self.subwindow)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.mdiArea)
        self.subwindow.setWindowTitle("文本框")
        self.pushButton_7.setText("清除")

        self.Qsubwindow=QtWidgets.QMdiSubWindow()
        self.Qsubwindow.setWidget(self.subwindow)
        self.mdiArea.addSubWindow(self.Qsubwindow)
        self.Qsubwindow.show()


    def closeEvent(self,event):
        self.check_changed.emit(False)
        super().closeEvent(event)    

class MyMainWindow(QMainWindow, Ui_MainWindow):  # 继承 QMainWindow类和 Ui_MainWindow界面类
    progress_changed =pyqtSignal(int)
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)  # 初始化父类
        self.setupUi(self)  # 继承 Ui_MainWindow 界面类       
        self.ui_add()
        self.init_value()
        # 重定向标准输出流
        # sys.stdout = StdoutRedirector(self.textEdit)

    def ui_add(self):
        self.progressBar.setRange(0,10)
        self.buttonGroup.setId(self.radioButton,1)
        self.buttonGroup.setId(self.radioButton_2,2)
        self.lineEdit_2.setPlaceholderText('输入以快速查找')
        # self.comboBox.setEditable(True)
        # self.comboBox.view().setFocusPolicy(Qt.NoFocus)

    def init_value(self):
        self.content=[]
        self.progress_flag=0
        # self.progress_Re=0
        self.update_linnedit_2=True
        self.mdi_window=None

    @pyqtSlot()
    def on_toolButton_clicked(self):
        print('test')
        # default_dir=os.path.join(os.path.expanduser("~"), 'Desktop')

        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # filename=QFileDialog.getOpenFileName(self,caption="打开文件",directory=default_dir,filter="All Files (*);;Text Files (*.txt)",initialFilter="Text Files (*.txt)",options=options)
        
        filename, _=QFileDialog.getOpenFileName(self,caption="Open file",filter="All Files (*);;Text Files (*.txt)")
        self.lineEdit.setText(filename)
        try:
            with open(filename,'r') as file:
                self.content=file.readlines()
            self.comboBox.addItems(self.content)
            # print(self.content)
        except :
            pass
            
    # @pyqtSlot(QAbstractButton)  #如果不指定传递参数，则会依次传递buttonClicked下具有的所有参数
    @pyqtSlot(int)
    def on_buttonGroup_buttonClicked(self,button_id):
        # print(self.buttonGroup.checkedButton().text())#按钮的内容
        print(button_id)     
        self.progress_changed.connect(self.update_progress_bar)
        if button_id==1:
            if self.progress_flag==0:         
                a=threading.Thread(target=self.emit_signal)
                a.daemon=True
                a.start()
            else:
                self.progress_flag=0
                a=threading.Thread(target=self.emit_signal)
                a.daemon=True
                a.start()
        else:
            self.progress_flag=0   

    def emit_signal(self):
        self.progress_flag=1
        # self.lineEdit.setText('hahahha')
        # self.progressBar.setValue(8)
        for i in range(11):
            if self.progress_flag:
                # self.progressBar.setValue(i)
                time.sleep(1)
                self.progress_changed.emit(i)
            else:
                break

    def update_progress_bar(self, value):
        self.progressBar.setValue(value)
    
    @pyqtSlot(str)
    def on_lineEdit_2_textChanged(self,text):
        text=text.strip()
        self.comboBox.clear()       
        for c in self.content:
            if text==c[0:len(text)]:
                self.comboBox.addItem(c)
        # self.comboBox.showPopup()
        # self.comboBox.setFocusPolicy(Qt.NoFocus)  # 设置combobox不获取焦点
        # self.comboBox.setView(self.comboBox.view())
        # self.comboBox.view().setFocusPolicy(Qt.NoFocus)
        # self.lineEdit_2.setFocus()

    # @pyqtSlot(int)
    @pyqtSlot(str)
    def on_comboBox_currentIndexChanged(self,text):
        # print(self.comboBox.currentText())
        pass

    @pyqtSlot(bool)
    def on_checkBox_toggled(self,bool):  # 动作 actHelp 触发
        if bool:
            self.plt_window=PLT_Form()
            if self.plt_window.exec_()==0: #用于显示对话框窗口并等待用户响应,会阻塞调用它的线程
                self.checkBox.setChecked(False)
            # self.setDisabled(True)   

    @pyqtSlot(bool)
    def on_checkBox_2_toggled(self,bool):
        if bool:
            self.mdi_window=MDI_Form()
            self.mdi_window.show()
            self.mdi_window.check_changed.connect(self.check_MDIWindow)
        else:
            self.mdi_window.close()
            # self.mdi_window.destroy()
            # self.mdi_window=None
 
    def check_MDIWindow(self,bool):
        self.checkBox_2.setChecked(bool)

    def closeEvent(self,event):
        if self.mdi_window:
            self.mdi_window.close()
        super().closeEvent(event)
         
if __name__ == "__main__":
    app=QApplication(sys.argv)
    myWin = MyMainWindow()  # 实例化 MyMainWindow 类，创建主窗口
    myWin.show()  # 在桌面显示控件 myWin
    sys.exit(app.exec_())  # 结束进程，退出程序
