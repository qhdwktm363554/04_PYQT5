import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QMainWindow, QAction, QMenu, QDialog, QStackedWidget

from PyQt5.QtCore import QCoreApplication

sys.path.append("d:\09.python\anaconda\pkgs")



class Option_window(QStackedWidget):
    def __init__(self):
        super().__init__()
        # 아래와 동일하다.
        # parent = super()
        # parent.__init__()

        # self.secondUI()
    def secondUI(self):
        # self.secondUI = secondUI
        btn = QPushButton('BS1', self)
        btn.setToolTip('let us get <b>placememt list from Pro<b/>')
        btn.resize(btn.sizeHint())
        btn.move(20, 30)
        self.setGeometry(400, 200, 400, 500)
        self.setWindowTitle('Line is selected')
        self.show()

class This_one_is_main_window (QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar()
        self.statusBar().showMessage("HI_bong")
        menu = self.menuBar()
        menu_file = menu.addMenu('File')
        menu_edit = menu.addMenu('edit')
        file_exit = QAction('Exit', self)   #Menu 객체를 생성한다.
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip("누르면 영원히 빠이")
        new_txt = QAction("txt file", self)
        new_py = QAction("python file", self)
        file_exit.triggered.connect(QCoreApplication.instance().quit)
        file_new = QMenu('New', self)       #sub group을 추가
        file_new.addAction(new_txt)         #sub menu를 추가
        file_new.addAction(new_py)
        menu_file.addMenu(file_new)         #주 menu 추가
        menu_file.addAction(file_exit)      #menu 등록


        btn = QPushButton('BS1', self)
        btn.setToolTip('let us get <b>placememt list from Pro<b/>')
        btn.resize(btn.sizeHint())
        btn.move(20,30)

        btn.clicked.connect(QCoreApplication.instance().quit)

        btn2 = QPushButton('BS2', self)
        btn2.setToolTip('let us get <b>placememt list from Pro<b/>')
        btn2.resize(btn.sizeHint())
        btn2.move(20,60)
        btn2.clicked.connect(self.clicked_option)

        self.setGeometry(300,300,400,500)
        self.setWindowTitle('To get placement list')
        # self.show()
    # def To_get_txt(self):
    #     text_1 = self.btn.QPushButton.text()
    #     return self.QPushButton.text()
    def clicked_option(self):
        # text_1 = self.btn2.QPushButton.text()
        self.line = "BS2"
        print("line is {}".format(self.line))
        Option_window()

        # self.secondUI()
    # def Option_window(self):
    #     # self.secondUI = secondUI
    #     btn = QPushButton('BS1', self)
    #     btn.setToolTip('let us get <b>placememt list from Pro<b/>')
    #     btn.resize(btn.sizeHint())
    #     btn.move(20, 30)
    #     self.setGeometry(400, 200, 400, 500)
    #     self.setWindowTitle('Line is selected')
    #     self.show()




    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "진짜 종료할거야?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



app = QApplication(sys.argv)        #event loop
print(sys.argv)
print(sys)
# app = QApplication([])
w = This_one_is_main_window()
w.show()
# app.exec_()
sys.exit(app.exec_())         #event loop를 실행시킨다. 