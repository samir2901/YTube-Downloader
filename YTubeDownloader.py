from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 230)
        MainWindow.setMaximumSize(QtCore.QSize(422, 230))
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

    def downloadVideo(self):
        try:      
            path = QtWidgets.QFileDialog.getExistingDirectory()
            print(path)                                
            link = self.url.text()
            yt = YouTube(link)
            video = yt.streams.first()
            video.download(path)
            msgDone = QtWidgets.QMessageBox()
            msgDone.setIcon(QtWidgets.QMessageBox.Information)
            msgDone.setWindowTitle("Done")
            msgDone.setText("Download Complete")
            msgDone.exec_()           
            print("Download Done....")            
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
