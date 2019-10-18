from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
import time

class Thread(QtCore.QThread):
    change_value = QtCore.pyqtSignal(int)   
    def run(self):
        cnt = 0
        while cnt <= 100:
            cnt += 1
            time.sleep(0.1)
            self.change_value.emit(cnt)            

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 270)
        MainWindow.setMaximumSize(QtCore.QSize(422, 270))
        icon = QtGui.QIcon.fromTheme(":/image/YouTube-icon.png")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")



        self.urlLabel = QtWidgets.QLabel(self.centralwidget)
        self.urlLabel.setGeometry(QtCore.QRect(20, 40, 111, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")



        self.url = QtWidgets.QLineEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(20, 70, 391, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.url.setFont(font)
        self.url.setObjectName("url")



        self.download = QtWidgets.QPushButton(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(160, 140, 101, 41))
        self.download.setObjectName("download")
        self.download.clicked.connect(self.downloadVideo)



        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 200, 371, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximum(100)
        self.progressBar.setMinimum(0)
        self.progressBar.setValue(0)




        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YTube Downloader"))
        self.urlLabel.setText(_translate("MainWindow", "Enter the URL"))
        self.download.setText(_translate("MainWindow", "Download"))


    def setProgressVal(self, val):
        self.progressBar.setValue(val)  
        if (self.progressBar.value()) == 100:             
            self.progressBar.reset() 
            msgDone = QtWidgets.QMessageBox()
            msgDone.setIcon(QtWidgets.QMessageBox.Information)
            msgDone.setWindowTitle("Done")
            msgDone.setText("Download Complete")
            msgDone.exec_()     
                

    def downloadVideo(self):
        try:      
            path = QtWidgets.QFileDialog.getExistingDirectory()
            print(path)                                
            link = self.url.text()            
            yt = YouTube(link)
            video = yt.streams.first()            
            video.download(path) 
            self.thread = Thread()
            self.thread.change_value.connect(self.setProgressVal)
            self.thread.start() 
        except:
            msgError = QtWidgets.QMessageBox()
            msgError.setIcon(QtWidgets.QMessageBox.Critical)
            msgError.setWindowTitle("Error")
            msgError.setText("Error!!")
            msgError.exec_()
            print("Connection Error.......") 

    
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
